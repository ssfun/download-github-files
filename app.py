import os
import tempfile
from flask import Flask, render_template, request, send_file, flash
from git import Repo
import shutil
import zipfile
import re

app = Flask(__name__)

def download_github_files(repo_url, file_paths, github_token=None):
    """从GitHub仓库下载指定路径的文件，并打包成zip。"""
    try:
        temp_dir = tempfile.mkdtemp()
        repo_name = repo_url.split('/')[-1].replace(".git", "")
        local_repo_path = os.path.join(temp_dir, repo_name)
        
        # 克隆仓库
        if github_token:
            repo_url_with_token = repo_url.replace("https://", f"https://{github_token}@")
            Repo.clone_from(repo_url_with_token, local_repo_path)
        else:
            Repo.clone_from(repo_url, local_repo_path)

        zip_file_path = os.path.join(temp_dir, f"{repo_name}_files.zip")
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for file_path in file_paths:
                abs_file_path = os.path.join(local_repo_path, file_path)
                if os.path.exists(abs_file_path) and os.path.isfile(abs_file_path):
                    zf.write(abs_file_path, os.path.basename(abs_file_path))
                elif os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
                    for root, dirs, files in os.walk(abs_file_path):
                        for file in files:
                            file_abs_path = os.path.join(root, file)
                            zf.write(file_abs_path, os.path.relpath(file_abs_path, local_repo_path))

        shutil.rmtree(local_repo_path)
        if os.path.exists(zip_file_path) and os.path.getsize(zip_file_path) > 0:
            return zip_file_path, f"{repo_name}_files.zip"
        else:
            return None, None
    except Exception:
        return None, None

def parse_github_url(url):
    """解析 GitHub URL，提取仓库 URL 和文件路径。"""
    match = re.match(r'https://github\.com/([^/]+)/([^/]+)/tree/([^/]+)(.*)', url)
    if match:
        owner, repo, branch, path = match.groups()
        repo_url = f'https://github.com/{owner}/{repo}.git'
        file_paths = [path.lstrip('/')] if path else []
        return repo_url, file_paths
    else:
        return None, None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        repo_path = request.form.get('repo_path')
        github_token = request.form.get('github_token')
        if not repo_path:
            flash('请提供 GitHub 链接', 'error')
            return render_template('index.html')

        repo_url, file_paths = parse_github_url(repo_path)
        if not repo_url:
             flash('无效的 GitHub 链接', 'error')
             return render_template('index.html')

        zip_path, zip_filename = download_github_files(repo_url, file_paths, github_token)
        if zip_path:
            return send_file(zip_path, as_attachment=True, download_name=zip_filename)
        else:
            flash('下载失败，请检查链接和文件路径。', 'error')
            return render_template('index.html')

    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000)) # 获取环境变量 PORT，默认为 5000
    app.run(debug=False, host="0.0.0.0", port=port)
