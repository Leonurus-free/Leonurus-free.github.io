# 使用docker搭建开发环境



## 需要安装的基础软件

~~~
wget
vim
net-tools

# 以下软件需要手动启动
ssh
redis
mysql
anaconda
nginx
~~~

### ssh

~~~
apt install openssh-server

vi /etc/ssh/sshd_config                  # 编辑ssh配置文件   
	PermitRootLogin yes                  # 把PermitRootLogin prohibit-password 改为 PermitRootLogin yes
	PubkeyAuthentication yes             # 开启公钥登录

# 启动ssh
service ssh start

# 查看ssh状态
service ssh status
# 设置ssh服务开机自启：
systemctl is-enabled ssh  # 虽然好像没什么用，每次重启后都需要手动启动ssh
~~~

### redis

~~~
apt install redis-server

redis-server /etc/redis/redis.conf

systemctl status redis


~~~



### anaconda

~~~
wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh --no-check-certificate

bash Anaconda3-2024.02-1-Linux-x86_64.sh

source ~/.bashrc
 
conda --version
~~~

## mysql

~~~

~~~









---

## 拉取镜像

~~~
docker pull nvidia/cuda:12.5.0-base-ubuntu22.04
docker run --rm --runtime=nvidia --gpus all nvidia/cuda:12.5.0-base-ubuntu22.04 nvidia-smi
~~~

## 启动容器

~~~
docker run -d \
  -p 20022:22 \  # ssh端口
  -p 23306:3306 \  # mysql数据库端口
  -p 26379:6379 \  # redis端口
  -p 27001:7001 \  # 项目端口
  -v F:/pythonProject/Corrective_fintune_v1:/home/pythonProject \   # 项目代码
  -v F:/pythonProject/Corrective_fintune_v1/envs:/root/anaconda \
  -v /home/free/python_project/Stirling-PDF/logs:/logs \
  -v /home/free/python_project/Stirling-PDF/customFiles:/customFiles \
  -e DOCKER_ENABLE_SECURITY=true \
  -e INSTALL_BOOK_AND_ADVANCED_HTML_OPS=true \
  -e LANGS=zh_CN \
  -e http_proxy=socks5://192.168.20.21:1080 \
  -e https_proxy=socks5://192.168.20.21:1080 \
  --name base_dev_env \
  --privileged=true \
  nvidia/cuda:12.5.0-base-ubuntu22.04
  
docker run -itd -p 20022:22 -p 27001:7001 -p 23306:3306 -p 26379:6379 --name base_dev_env --privileged=true nvidia/cuda:12.5.0-base-ubuntu22.04 
~~~

## 进入容器

~~~
docker exec -it base_dev_env /bin/bash
~~~



## 安装软件包



### 通过Dockerfile的方式

~~~
# 基础镜像
FROM nvidia/cuda:12.5.0-base-ubuntu22.04

# 设置工作目录
WORKDIR /CODE

# 安装基础依赖
# 更新系统并安装必要的软件包
RUN apt-get update \
    && apt-get install -y python3.11 python3.11-venv python3.11-dev \
	&& apt-get install -y nginx \
	&& apt-get install -y redis \
	&& apt-get install -y vim \
    && apt-get clean

# 设置 python3 和 pip3 指向 Python 3.11
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1

# 安装 pip
RUN apt-get install -y python3-pip

# 复制项目文件到容器
COPY . /CODE

# 安装项目依赖
RUN pip install --no-cache-dir -r /CODE/requirements.txt

# 暴露端口
EXPOSE 80
EXPOSE 7001

# 设置默认命令
CMD ["/bin/bash"]
~~~



## 将容器保存为镜像

~~~
# 将交互式的容器提交为一个新的镜像
docker commit base_dev_env base_dev_env:v1
~~~



## 编写Dockerfile文件，构建新的镜像

~~~
# 基础镜像
FROM base_dev_env:v1

# 设置工作目录
WORKDIR /home

# 创建启动脚本
RUN echo -e "#!/bin/bash \n\
service ssh start \n\
redis-server /etc/redis/redis.conf \n\
service mysql start \n\
tail -f /dev/null" > start.sh

# 赋予脚本执行权限
RUN chmod +x start.sh

# 暴露端口
EXPOSE 22
EXPOSE 7001
EXPOSE 3306
EXPOSE 6379

# 设置默认命令
CMD ["/home/start.sh"]
~~~



### 构建镜像

~~~
docker build -t base_dev_env:v2.0 .
~~~



## 从新的镜像中启动容器

~~~
docker run -d \
  -p 20022:22 \  # ssh端口
  -p 23306:3306 \  # mysql数据库端口
  -p 26379:6379 \  # redis端口
  -p 27001:7001 \  # 项目端口
  -v F:/pythonProject/Corrective_fintune_v1:/home/pythonProject \   # 项目代码
  -v F:/pythonProject/Corrective_fintune_v1/envs:/root/anaconda3/envs \  # 环境
  -v F:/pythonProject/Corrective_fintune_v1/mysql_data:/var/lib/mysql \  # mysql数据库文件
  --name base_dev_env_v2 \
  --privileged=true \
  base_dev_env:v2.0
  
docker run -itd -p 20022:22 -p 27001:7001 -p 23306:3306 -p 26379:6379 -v F:/pythonProject/Corrective_fintune_v1:/home/pythonProject -v F:/pythonProject/Corrective_fintune_v1/envs:/root/anaconda3/envs --name base_dev_env_v2 --privileged=true base_dev_env:v2.0 
~~~

