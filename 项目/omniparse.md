# omniparse



## **Everything to Markdown**

## Supported Data Types

| Type         | Supported Extensions                    |
| ------------ | --------------------------------------- |
| Documents    | .doc, .docx, .pdf, .ppt, .pptx          |
| Images       | .png, .jpg, .jpeg, .tiff, .bmp, .heic   |
| Media(Video) | .mp4, .mkv, .avi, .mov                  |
| Media(Audio) | .mp3, .wav, .aac                        |
| Web          | dynamic webpages, http://<anything>.com |

## 构建基础开发镜像

~~~
# 基础镜像
FROM nvidia/cuda:12.5.0-base-ubuntu22.04

# 设置工作目录
WORKDIR /home

# 安装基础依赖，更新系统并安装必要的软件包
RUN apt-get update && apt-get install -y \
    python3.11 python3.10-venv python3.10-dev \
    python3-pip net-tools openssh-server vim \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 创建 SSH 目录并修改配置，允许 root 登录和开启公钥认证
RUN mkdir /var/run/sshd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config && \
    echo 'root:1qaz2wsx' | chpasswd

# 暴露端口
EXPOSE 22
EXPOSE 8001

# 启动 ssh 服务
CMD ["/usr/sbin/sshd", "-D"]

# 构建镜像
docker build -t omniparse_dev .
~~~





## 构建开发环境

注意：采用这种构建方式，在pycharm中不需要进行文件同步，需要把文件同步关闭！！！

~~~


docker run -itd -p 20022:22 -p 28001:8001 -v F:/pythonProject/omniparse:/home/pythonProject/omniparse --runtime=nvidia --gpus all --name omniparse_dev_v1 --privileged=true omniparse_dev:latest

启动之后就可以在pycharm采用ssh进行远程，然后安装所需要的包和环境
~~~



## docker镜像构建

~~~
dockerfile文件在项目的根目录下

# 构建镜像
docker build -t omniparse .

# 启动镜像
docker run -d --runtime nvidia --gpus all -p 8001:8001 -v F:/.omniparse:/tmp --name omniparse omniparse:latest
~~~

