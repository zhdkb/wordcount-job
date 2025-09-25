# 选择基础镜像（轻量推荐）
FROM python:3.10-slim

# 设置容器内的工作目录
WORKDIR /app

# 复制整个项目到容器内
COPY . .

# 设置默认启动命令
CMD ["python", "main.py"]
