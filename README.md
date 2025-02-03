# GitHub 文件下载器

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个基于 Python Flask 的 Web 应用，用于从 GitHub 仓库下载指定路径的文件或目录，并打包成 ZIP 文件。支持公开和私有仓库。

## 项目简介

这个项目提供了一个简单的 Web 界面，允许用户输入 GitHub 仓库的链接（包括分支和文件路径），然后下载该路径下的文件或目录。如果仓库是私有的，用户可以提供 GitHub Personal Access Token 进行身份验证。

**隐私声明：** 本项目不会记录用户的任何信息，包括 GitHub 链接、Personal Access Token 以及下载的文件内容。所有操作均在本地完成，不存储任何数据。

## 功能特性

*   **支持公开和私有仓库:** 可以下载公开和私有 GitHub 仓库的文件。
*   **指定路径下载:**  可以指定仓库中的文件或目录路径进行下载。
*   **打包成 ZIP 文件:** 下载的文件会被打包成 ZIP 文件，方便用户下载。
*   **基于 Web 界面:** 提供一个简单的 Web 界面，方便用户操作。
*   **使用 Flask 构建:** 使用 Python Flask 框架构建，易于部署和扩展。

## 使用方法

1.  **克隆仓库:**
    ```bash
    git clone https://github.com/ssfun/github-file-downloader.git
    cd github-file-downloader
    ```

2.  **安装依赖:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **运行应用:**
    ```bash
    python app.py
    ```
    或者使用 Docker 运行：
    ```bash
    docker build -t github-file-downloader .
    docker run -p 5000:5000 github-file-downloader
    ```

4.  **访问应用:** 在浏览器中打开 `http://localhost:5000` (或者你的 Docker 主机地址).

5.  **输入 GitHub 链接:** 在输入框中粘贴 GitHub 仓库的链接，例如：`https://github.com/ssfun/download-github-files/tree/main/templates`。

6.  **输入 GitHub Personal Access Token (可选):** 如果是私有仓库，请在第二个输入框中输入你的 GitHub Personal Access Token。

7.  **点击“下载”按钮。**

## 示例

*   **公开仓库:**
    *   输入 GitHub 链接： `https://github.com/ssfun/download-github-files/tree/main/templates`
    *   点击“下载”按钮，即可下载 `lade` 目录及其中的文件。
*   **私有仓库:**
    *   输入 GitHub 链接： `https://github.com/your-username/your-private-repo/tree/main/your-file.txt`
    *   输入 GitHub Personal Access Token
    *   点击“下载”按钮，即可下载 `your-file.txt` 文件。

## 贡献

欢迎提交 issue 和 pull request!

## 许可证

本项目使用 MIT 许可证，详情请查看 [LICENSE](LICENSE) 文件。

## 联系方式

*   GitHub: [https://github.com/ssfun](https://github.com/ssfun)
