# docker镜像删除

通过如下两个都可以删除镜像：

```bash
docker rmi [image]
```

或者：

```bash
docker image rm [image]
```

支持的子命令如下：

- `-f, -force`: 强制删除镜像，即便有容器引用该镜像；
- `-no-prune`: 不要删除未带标签的父镜像；