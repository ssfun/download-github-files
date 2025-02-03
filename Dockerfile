FROM python:3.9-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y git

RUN pip install --no-cache-dir Flask requests gitpython

COPY . .

EXPOSE 3000

CMD ["python", "app.py"]
