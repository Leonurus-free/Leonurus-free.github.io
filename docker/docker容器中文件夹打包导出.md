# docker容器中文件夹打包导出

## ✅ 方式一：直接从容器拷贝出来（最简单）

不需要进入容器、无需 tar：

```
docker cp <容器名或ID>:<容器内路径> <宿主机目标目录>
```

示例：

```
docker cp myapp:/data /home/user/
```

------

## ✅方式二：在容器中打包，再拷贝出来（适合大文件 / 保留权限）

进入容器打包：

```
docker exec myapp tar czf /tmp/data.tar.gz /data
```

再从容器拷贝到宿主机：

```
docker cp myapp:/tmp/data.tar.gz /home/user/
```

------

## ✅方式三：一次命令完成（不写入容器磁盘）

直接流式导出：

```
docker exec myapp tar czf - /data > data.tar.gz
```

或者：

```
docker exec myapp tar cf - /data | gzip > data.tar.gz
```

------

样例

~~~
/home/ubuntu/luo/projectDockerCompose/test# docker exec comfyui tar czf - /root/ComfyUI/custom_nodes/comfyui_custom_nodes_alekpet > /comfyui_custom_nodes_alekpet.tar.gz
~~~



