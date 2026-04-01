# centos 7安装Anaconda

1. 在官网下载 Anaconda 的最新版本，链接：https://www.anaconda.com/products/distribution

    https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh 地址也可以

1. 打开终端，进入下载目录，使用以下命令来安装 Anaconda：

~~~bash
 # 也可直接在线下载
wget https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh --no-check-certificate
wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh --no-check-certificate

bash Anaconda3-2024.02-1-Linux-x86_64.sh
~~~

3. 按照提示进行安装，注意修改安装路径、添加组件等。（默认安装目录 PREFIX=/root/[anaconda3](https://so.csdn.net/so/search?q=anaconda3&spm=1001.2101.3001.7020)）
4. 安装完毕后，可以输入以下命令使环境变量立即生效：

```bash
 source ~/.bashrc
```

5. 使用以下命令查看 Anaconda 是否已成功安装：

```bash
 conda --version
```

若安装成功，会出现版本号信息。