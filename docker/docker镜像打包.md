# docker 镜像制作和镜像打包

#### 制作镜像

两种方式

1. docker commit命令
2. 使用docker build和Dockerfile文件

示例制作一个tomcat镜像，制作步骤：

```python
docker commit 提交一个正在运行的容器为一个新的镜像
1.拉取一个基础镜像
docker pull centos

2.创建一个交互式容器
docker run -it --name=mycentos centos：latest

3.上传软件到容器中
docker cp  xxx.tar  mycentos:/root/

4.在容器中安装软件


5. 将交互式的容器提交为一个新的镜像
docker commit mycentos myomcat
```

#### 镜像打包

**1.镜像打包**

```cobol
docker save -o /root/xxx.tar  <name>
```

**2.导入镜像**

```cobol
docker load -i /root/xxx.tar
```

#### 容器打包

**1.容器打包**

```cobol
docker export -o /root/xx.tar  <name>
```

**2.导入容器**

```haskell
docker import xx.tar <name>:latest
```