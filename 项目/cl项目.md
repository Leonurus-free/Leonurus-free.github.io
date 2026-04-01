# CL部署

## 本地部署

本地部署是为了能够快捷的提供本地 API 服务



### 构建后端前期准备

#### dockerfile

~~~
# Select the image to build based on SERVER_TYPE, defaulting to fastapi_server, or docker-compose build args
ARG SERVER_TYPE=fastapi_server

# === Python environment from uv ===
FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim AS builder

# Used for build Python packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . /cl_luo

WORKDIR /cl_luo

# Configure uv environment
ENV UV_COMPILE_BYTECODE=1 \
    UV_NO_CACHE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/usr/local

# Install dependencies with cache
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-default-groups --group server

# === Runtime base server image ===
FROM python:3.11-slim AS base_server

# 设置时区为北京时间
ENV TZ=Asia/Shanghai

RUN apt-get update \
    && apt-get install -y --no-install-recommends supervisor \
    && apt-get install -y tzdata \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /cl_luo /cl_luo

COPY --from=builder /usr/local /usr/local

COPY deploy/backend/supervisord.conf /etc/supervisor/supervisord.conf

WORKDIR /cl_luo/backend

# === FastAPI server image ===
FROM base_server AS fastapi_server

COPY deploy/backend/fastapi_server.conf /etc/supervisor/conf.d/

RUN mkdir -p /var/log/fastapi_server

EXPOSE 8101

CMD ["/usr/local/bin/granian", "main:app", "--interface", "asgi", "--host", "0.0.0.0", "--port","8101"]

# === Celery server image ===
FROM base_server AS celery

COPY deploy/backend/celery.conf /etc/supervisor/conf.d/

RUN mkdir -p /var/log/celery

RUN chmod +x celery-start.sh

EXPOSE 8102

CMD ["./celery-start.sh"]

# Build image
FROM ${SERVER_TYPE}

~~~

#### fastapi_server.conf

~~~
[program:fastapi_server]
directory=/cl_luo/backend
command=/usr/local/bin/granian main:app --interface asgi --host 0.0.0.0 --port 8101 --workers 1 --backlog 1024 --workers-kill-timeout 120 --backpressure 2000 --pid-file /var/run/granian.pid --log --log-level debug
user=root
autostart=true
autorestart=true
startretries=5
redirect_stderr=true
stdout_logfile=/var/log/fastapi_server/cl_luo_server.log
stdout_logfile_maxbytes=5MB
stdout_logfile_backups=5
~~~

#### .env.server

~~~
# Env: dev、pro
ENVIRONMENT='dev'
# Database
DATABASE_TYPE='mysql'
DATABASE_HOST='cl_luo_mysql'
DATABASE_PORT=3306
DATABASE_USER='root'
DATABASE_PASSWORD='1qaz2wsx'
# Redis
REDIS_HOST='cl_luo_redis'
REDIS_PORT=6379
REDIS_PASSWORD=''
REDIS_DATABASE=0
# Token
TOKEN_SECRET_KEY='1VkVF75nsNABBjK_7-qz7GtzNy3AMvktc9TCPwKczCk'
# Opera Log
OPERA_LOG_ENCRYPT_SECRET_KEY='d77b25790a804c2b4a339dd0207941e4cefa5751935a33735bc73bb7071a005b'
# Admin
# OAuth2
OAUTH2_GITHUB_CLIENT_ID='test'
OAUTH2_GITHUB_CLIENT_SECRET='test'
OAUTH2_LINUX_DO_CLIENT_ID='test'
OAUTH2_LINUX_DO_CLIENT_SECRET='test'
# Task
# Celery
CELERY_BROKER_REDIS_DATABASE=1
# Rabbitmq
CELERY_RABBITMQ_HOST='cl_luo_rabbitmq'
CELERY_RABBITMQ_PORT=5672
CELERY_RABBITMQ_USERNAME='cl_luo'
CELERY_RABBITMQ_PASSWORD='1qaz2wsx'

~~~

#### .env.docker

~~~
CONTAINER_VERSION=20250729
~~~

#### celery.conf

~~~
[program:celery_worker]
directory=/cl_luo/backend
command=/usr/local/bin/celery -A app.task.celery worker -P gevent -c 1000 --loglevel=INFO
user=root
autostart=true
autorestart=true
startretries=5
redirect_stderr=true
stdout_logfile=/var/log/celery/cl_luo_celery_worker.log
stdout_logfile_maxbytes=5MB
stdout_logfile_backups=5

[program:celery_beat]
directory=/cl_luo/backend
command=/usr/local/bin/celery -A app.task.celery beat --loglevel=INFO
user=root
autostart=true
autorestart=true
startretries=5
redirect_stderr=true
stdout_logfile=/var/log/celery/cl_luo_celery_beat.log
stdout_logfile_maxbytes=5MB
stdout_logfile_backups=5

[program:celery_flower]
directory=/cl_luo/backend
command=/usr/local/bin/celery -A app.task.celery flower --port=8102 --url-prefix=flower --basic-auth=admin:123456
user=root
autostart=true
autorestart=true
startretries=5
redirect_stderr=true
stdout_logfile=/var/log/celery/cl_luo_celery_flower.log
stdout_logfile_maxbytes=5MB
stdout_logfile_backups=5

~~~

#### supervisord.conf



### 构建后端镜像

```
docker build -t cl_luo_server:20250809 -f Dockerfile .
```

命令的解释：

- `docker build`: 构建 Docker 镜像的命令
- `-t cl_luo_server:20250729`: 指定镜像的名称和标签
- `-f Dockerfile`: 指定使用的 Dockerfile 文件（如果 Dockerfile 在当前目录且名为"Dockerfile"，这个参数可以省略）
- `.`: 表示构建上下文为当前目录



### 构建celery镜像

~~~
docker build -t cl_luo_celery:20250809 --build-arg SERVER_TYPE=celery -f Dockerfile .
~~~

命令解析：

- `docker build`：构建 Docker 镜像
- `-t cl_luo_celery:20250729`：指定镜像名称和标签
- `--build-arg SERVER_TYPE=celery`：传递构建参数 `SERVER_TYPE`，值为 `celery`（Dockerfile 中可能需要用它区分服务类型）
- `-f Dockerfile`：指定 Dockerfile 路径（如果文件名为 `Dockerfile` 且在当前目录，可省略）
- `.`：构建上下文为当前目录



### 构建前端前期准备

#### dockerfile

~~~
FROM guergeiro/pnpm:lts-latest-slim AS build

WORKDIR /cl_luo_ui

COPY . .

RUN pnpm install \
    && pnpm build

FROM nginx

# 设置时区为北京时间
ENV TZ=Asia/Shanghai

RUN apt-get update \
    && apt-get install -y tzdata \
    && rm -rf /var/lib/apt/lists/*

COPY scripts/deploy/nginx.conf /etc/nginx/nginx.conf

COPY --from=build /cl_luo_ui/apps/web-antd/dist /var/www/cl_luo_ui

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

~~~

#### nginx

~~~
worker_processes auto;
pid /run/nginx.pid;
error_log /var/log/nginx/error.log;

# Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 8192;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    sendfile on;
    client_max_body_size 5M;
    client_body_buffer_size 5M;

    gzip on;
    gzip_comp_level 2;
    gzip_types text/plain text/css text/javascript application/javascript application/x-javascript application/xml application/x-httpd-php image/jpeg image/gif image/png;
    gzip_vary on;

    keepalive_timeout 300;

    access_log /var/log/nginx/access.log;

    server {
        listen 80;
        listen [::]:80;
        server_name _;

        # listen 443 ssl;
        # ssl_certificate /etc/ssl/xxx.pem;
        # ssl_certificate_key /etc/ssl/xxx.key;
        # ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
        # ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        # ssl_prefer_server_ciphers on;

        client_max_body_size   5m;

        root /var/www/cl_luo_ui;

        location / {
            try_files $uri $uri/ /index.html;
        }

        # 处理API请求
        location /api/v1/ {
            proxy_pass http://cl_luo_server:8101;

            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_connect_timeout 300s;
            proxy_send_timeout 300s;
            proxy_read_timeout 300s;
        }

        # 处理翻译词典请求
        location /TranslationGlossary/ {
            proxy_pass http://cl_luo_translation_server:8103;

            # 必须的流式支持配置
            proxy_http_version 1.1;          # 使用 HTTP/1.1 以支持 chunked 传输
            proxy_buffering off;             # 禁用缓冲
            proxy_cache off;                 # 禁用缓存
            chunked_transfer_encoding on;    # 启用分块传输编码

            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_connect_timeout 300s;
            proxy_send_timeout 300s;
            proxy_read_timeout 300s;

            # 可选：确保连接保持活动状态（对长时间流有用）
            proxy_set_header Connection '';
        }

        # 处理翻译引擎静态文件
        location /static/OutputFile/ {
            proxy_pass http://cl_luo_translation_server:8103;

            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_connect_timeout 300s;
            proxy_send_timeout 300s;
            proxy_read_timeout 300s;
        }

        location /static/InputFile/ {
            proxy_pass http://cl_luo_translation_server:8103;

            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_connect_timeout 300s;
            proxy_send_timeout 300s;
            proxy_read_timeout 300s;
        }

        # 处理WebSocket连接
        location /ws/socket.io/ {
            proxy_pass http://cl_luo_server:8101/ws/socket.io/;

            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_read_timeout 86400s;
            proxy_send_timeout 86400s;

            # WebSocket 支持
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_buffering off;
        }

        # 处理Flower监控
        location /flower/ {
            proxy_pass http://cl_luo_server:8102;

            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_connect_timeout 300s;
            proxy_send_timeout 300s;
            proxy_read_timeout 300s;
            proxy_redirect off;

            # WebSocket 支持
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
        }

        # 处理静态文件
        location /static/ {
            alias /var/www/cl_luo_server/backend/static;
        }

        location /static/upload/ {
            alias /var/www/cl_luo_server/backend/static/upload;
        }

        error_page 500 502 503 504 /50x.html;

        location = /50x.html {
            root /usr/share/nginx/html;
        }
    }
}


~~~



### 构建前端镜像

~~~
docker build -t cl_luo_ui:20250729 -f Dockerfile .
~~~





### **使用 Docker Compose 命令行设置变量**：

- 如果你不希望通过 `.env` 文件来设置 `HOST_IP`，你也可以在命令行启动时覆盖它：

  ```
  Linux:
  CONTAINER_VERSION=20250729 docker-compose up -d
  win:
  $env:CONTAINER_VERSION="20250729"
  docker compose up -d
  ```

- 前端变量在构建后的`_app.config.js`文件中修改

### 版本更新

~~~
前端
pnpm build
然后将dist复制到F:\projectDockerCompose\cl_luo\cl_luo_frontend\dist。并按需修改_app.config.js文件内容

后端
将项目文件直接复制到F:\projectDockerCompose\cl_luo\cl_luo_backend\cl_luo_project_files
注意不能包含.venv文件夹
如果有包的更新需要进行离线化更新，或者重新打包镜像
~~~





后端：8101->18101

前端：使用nginx  80->15666

celery:8102->18102

mysql:3306->13306

redis:6379->16379

rabbitmq:15672:->15672  \# 管理界面

rabbitmq:5672:->15673  \# AMQP 通信

翻译服务：8103->18103





## minio测试

~~~
docker exec -it cl_luo_server bash
~~~



~~~
python -c "
from minio import Minio
import time
for i in range(10):
    try:
        client = Minio('cl_luo_minio:9000', access_key='root', secret_key='1qaz2wsx', secure=False)
        client.list_buckets()
        print('✅ MinIO 连接成功')
        break
    except Exception as e:
        print(f'❌ MinIO 连接尝试 {i+1}/10 失败: {e}')
        time.sleep(3)
"

python3 -c "
import socket
import requests
import time

# 1. 测试TCP连接
print('1. 测试TCP连接...')
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex(('cl_luo_minio', 9000))
    sock.close()
    if result == 0:
        print('✅ TCP连接成功')
    else:
        print('❌ TCP连接失败')
        exit(1)
except Exception as e:
    print(f'❌ TCP测试失败：{e}')
    exit(1)

# 2. 测试HTTP连接
print('2. 测试HTTP连接...')
try:
    import urllib.request
    response = urllib.request.urlopen('http://cl_luo_minio:9000', timeout=10)
    print(f'✅ HTTP连接成功，状态码：{response.status}')
    print(f'   响应头：{dict(response.headers)}')
except Exception as e:
    print(f'❌ HTTP连接失败：{e}')

# 3. 测试MinIO健康检查
print('3. 测试MinIO健康检查...')
try:
    health_response = urllib.request.urlopen('http://cl_luo_minio:9000/minio/health/live', timeout=10)
    print(f'✅ MinIO健康检查成功，状态：{health_response.status}')
except Exception as e:
    print(f'❌ MinIO健康检查失败：{e}')
"
~~~

## format_content格式

~~~
format_content按照以下格式

 format_content:{
        "extracted_content": {
            "侧边页": "从 /div 提取的内容",
            "222": "从 /name 提取的内容"
        },
        "extraction_rules": [
            {"xpath": "/div", "name": "侧边页"},
            {"xpath": "/name", "name": "222"}
        ],
        "metadata": {
            "archive_time": "2025-08-12T10:00:00",
            "original_url": "https://example.com"
        }
    }



{
"parse_params": {
	"max_retries": 3,
	"use_javascript": True,
	"is_iframe": False
},
"extraction_rules": [
{
    "xpath": "/div",
    "name": "侧边页",
},
{
    "xpath": "/name",
    "name": "222",
},
]
}

{
    "/div": "内容",
    "/name": 侧边页,
    ...
}
~~~





请先阅读整个项目，再阅读backend/app/sync现有结构。我想在这个文件夹中实现mysql和minio数据外网导出增量 → 内网拉取导入功能。     

请注意：**内网和外网不能直接通信**

### **思路**

1. **外网机器**：定期导出数据（增量）到一个文件。

   mysql数据库您需要同步的是cl_luo_db数据库中的rss_feed、rss_category、rss_user、rss_article四个表。为了以后更方面新增，请预先设计好接口，便于后续新增表。您可以将有修改的数据生成.sql文件。数据库的连接您可以参考backend/database/db.py文件

   minio是根据 MinIO 的 `list_objects`。用 MinIO SDK 获取最近 5 分钟内新增的对象。然后把这些文件**打包**：minio_export_20250901.tar.gz，再上传到ftp中。

   **外网端：导出增量**

   1. 导出 MySQL 增量 → `data_20250901.csv`
   2. 根据 MySQL 中的 `minio_id` 去拉取文件 → 打包成 `minio_export_20250901.tar.gz`
   3. 上传 `csv` 和 `tar.gz` 到ftp指定文件夹

   **内网端：导入增量**

   1. 从共享区拉取最新 `data_20250901.csv` → 导入 MySQL
   2. 解压 `minio_export_20250901.tar.gz` → 上传到内网 MinIO
   3. 根据 MySQL 里的 `minio_id` 建立文件映射

2. **中转区**：公司有个FTP 服务器。

外网ftp中转服务器：        

"outside_server": {
            "server_name": "FTP",
            "ip": "192.168.250.51",
            "port": 55776,
            "username": "htgd1",
            "password": "htgd1",
            "remote_path": "/cl_transfer_data"
        },

内网ftp中转服务器：

"inside_server": {
            "server_name": "FTP",
            "ip": "114.22.14.224",
            "port": 21,
            "username": "htyf3",
            "password": "123456",
            "remote_path": "/cl_transfer_data"
        },

2.**内网机器**：每隔5分钟定时扫描对应的ftp文件夹有文件则拉取文件，导入数据库

您因该将外网导入模块（将数据推入ftp）和内网导出模块（将数据从ftp中导出）分别构建成celery定时任务。您可以模仿backend/app/rss文件夹中的代码来写。





export ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic
export ANTHROPIC_AUTH_TOKEN=0be7c385f8a447b7901477eac497cf5d.hVXd8bJrk2O8Pcyj
