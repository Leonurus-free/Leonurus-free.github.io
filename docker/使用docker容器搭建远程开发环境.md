# 使用docker搭建远程开发环境



## 编写dockerfile

~~~
# 基础镜像
FROM nvidia/cuda:12.5.0-base-ubuntu22.04

# 设置工作目录
WORKDIR /home

# 安装基础依赖
# 更新系统并安装必要的软件包
RUN apt-get update \
    && apt-get install -y python3.11 python3.11-venv python3.11-dev \
	&& apt-get install -y net-tools \
	&& apt-get install -y openssh-server \
	&& apt-get install -y vim \
    && apt-get clean

# 设置 python3 和 pip3 指向 Python 3.11
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1

# 安装 pip
RUN apt-get install -y python3-pip

# 创建 SSH 目录
RUN mkdir /var/run/sshd

# 修改 sshd 配置文件，允许 root 登录和开启公钥认证
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config

# 设置root密码（可根据需要更改密码）
RUN echo 'root:1qaz2wsx' | chpasswd

# 暴露端口
EXPOSE 22
EXPOSE 7001

# 启动 ssh 服务
CMD ["/usr/sbin/sshd", "-D"]
~~~

### 简洁版本

~~~
# 基础镜像
FROM nvidia/cuda:12.5.0-base-ubuntu22.04

# 设置工作目录
WORKDIR /home

# 安装基础依赖，更新系统并安装必要的软件包
RUN apt-get update && apt-get install -y \
    python3.11 python3.11-venv python3.11-dev \
    python3-pip net-tools openssh-server vim \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 创建 SSH 目录并修改配置，允许 root 登录和开启公钥认证
RUN mkdir /var/run/sshd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config && \
    echo 'root:1qaz2wsx' | chpasswd

# 暴露端口
EXPOSE 22
EXPOSE 7001

# 启动 ssh 服务
CMD ["/usr/sbin/sshd", "-D"]
~~~


conda版本
~~~
# 基础镜像
FROM nvidia/cuda:12.5.0-base-ubuntu22.04

# 设置工作目录
WORKDIR /home

# 安装基础依赖，更新系统并安装必要的软件包
RUN apt-get update && apt-get install -y \
    wget bzip2 python3.11 python3.11-venv python3.11-dev \
    python3-pip net-tools openssh-server vim \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 下载并安装指定版本的 Anaconda3
RUN wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh -O /tmp/anaconda.sh && \
    bash /tmp/anaconda.sh -b -p /opt/anaconda && \
    rm /tmp/anaconda.sh && \
    /opt/anaconda/bin/conda init && \
    ln -s /opt/anaconda/bin/conda /usr/bin/conda

# 设置环境变量
ENV PATH="/opt/anaconda/bin:$PATH"

# 创建 SSH 目录并修改配置，允许 root 登录和开启公钥认证
RUN mkdir /var/run/sshd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config && \
    echo 'root:1qaz2wsx' | chpasswd

# 暴露端口
EXPOSE 22
EXPOSE 8002

# 启动 ssh 服务
CMD ["/usr/sbin/sshd", "-D"]

~~~

## 构建镜像

~~~
docker build -t dev_env_image .
~~~



## 启动镜像

~~~
docker run -d \
  -p 20022:22 \  # ssh端口
  -p 27001:7001 \  # 项目端口
  -v F:/pythonProject/Corrective_fintune_v1:/home/pythonProject \   # 项目代码
  --runtime=nvidia \
  --gpus all \
  --name base_dev_env_v2 \
  --privileged=true \
  base_dev_env:v2.0
  
docker run -itd -p 20022:22 -p 27001:7001 -v F:/pythonProject/Corrective_fintune_v1:/home/pythonProject --runtime=nvidia --gpus all --name base_dev_env_v2 --privileged=true base_dev_env:v2.0 

docker run -itd -p 20022:22 -p 27001:7001 -v F:/pythonProject/Corrective_fintune_v1:/home/pythonProject --runtime=nvidia --gpus all --name corrective_fintune_v1 --privileged=true corrective_fintune:v1.0

docker run -itd -p 20022:22 -p 27001:7001 -v /home/ubuntu/luo/Corrective_fintune_v1:/home/pythonProject --runtime=nvidia --gpus all --name corrective_fintune_v1 --privileged=true corrective_fintune_v1:latest

docker run -itd -p 20022:22 -p 28001:8001 -v F:/pythonProject/omniparse:/home/pythonProject/omniparse --runtime=nvidia --gpus all --name omniparse_dev_v2 --privileged=true omniparse_dev:latest
~~~



