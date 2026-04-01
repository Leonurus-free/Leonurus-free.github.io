## Docker rm

`docker rm` 根据容器的名称或者 ID 来删除容器。

如果 Docker 容器正在运行，你在删除它们之前需要先停止运行。

- 停止所有容器运行：`docker stop $(docker ps -a -q)`
- 删除所有停止运行的容器：`docker rm $(docker ps -a -q)`

### 删除多个容器

你可以通过向命令传递要删除的容器列表来停止和删除多个容器。shell 语法 `$()` 返回括号中执行的任何结果。因此，你可以在其中创建容器列表，以传递给 `stop` 和 `rm` 命令。

### **docker ps -a -q 分解**

- `docker ps` 列出容器。
- `-a` 这个选项用于列出所有容器，包括停止运行的。如果没有这个选项，则默认只列出在运行的容器。
- `-q` 这个选项列出容器的数字 ID，而不是容器的所有信息。



## 1. 查看镜像的详细信息

查看 Docker 镜像的详细信息对于了解镜像的大小、创建时间等非常有用：

```
#!/bin/bash
# 查看镜像的详细信息
docker inspect $1
```

 解释：

-  `docker inspect`：查看镜像的详细信息。

------

## 2. 限制容器的资源

为了避免单个容器占用过多系统资源，可以在启动容器时限制其资源使用：

```
#!/bin/bash
# 限制容器的资源
docker run -d --memory="512m" --cpus="1" --name my_container my_image
```

解释：

-  `--memory="512m"`：限制容器的内存使用为 512MB。
-  `--cpus="1"`：限制容器使用一个 CPU 核心。

------

## 3. 备份容器的数据

```
#!/bin/bash
# 备份容器的数据
CONTAINER_ID=$1
BACKUP_FILE="${CONTAINER_ID}_backup_$(date +%F).tar"
docker export $CONTAINER_ID > $BACKUP_FILE
echo "备份保存到 $BACKUP_FILE"
```

解释：

-  `docker export`：导出容器的文件系统。
-  将容器 ID 作为脚本参数传递。
-  备份文件命名格式为容器 ID + 当前日期。

------

## 4. 删除停止的容器

```
#!/bin/bash
# 删除所有停止的容器
docker rm $(docker ps -aq -f "status=exited")
```

解释：

- `docker ps -aq -f "status=exited"`：列出所有停止的容器。
- `docker rm`：删除这些容器。

------

## 5. 自动重启容器

```
#!/bin/bash
# 使用重启策略重启容器
CONTAINER_NAME=$1
docker update --restart always $CONTAINER_NAME
echo "$CONTAINER_NAME 现在将在失败后自动重启。"
```

 解释：

-  `docker update --restart always`：设置容器在失败后自动重启。

------

## 6. 运行容器并在退出后清理

```
#!/bin/bash
# 运行容器并清理
IMAGE_NAME=$1
docker run --rm $IMAGE_NAME
```

  解释：

-  `--rm`：容器停止后自动删除。

------

## 7. 列出所有容器的镜像层

在调试或排查容器相关问题时，查看容器的镜像层有时非常有帮助。以下脚本列出每个容器的镜像层：

```
#!/bin/bash
# 列出所有容器的镜像层
docker inspect --format '{{.Id}}: {{.Image}}' $(docker ps -q)
```

  解释：

-  `docker inspect --format`：通过格式化输出，获取容器的镜像层。
-  `docker ps -q`：列出所有运行中的容器。

------

## 8. 自动清理未使用的资源

```
#!/bin/bash
# 清理未使用的资源
docker system prune -f --volumes
```

  解释：

-  `docker system prune`：删除未使用的容器、网络、镜像。
-  `--volumes`：删除未使用的卷。

------

## 9. 删除dangling的镜像

```
#!/bin/bash
# 删除dangling 镜像
docker rmi $(docker images -q -f "dangling=true")
```

  解释：

-  `docker images -q -f "dangling=true"`：列出所有未被引用的镜像 ID。
-  `docker rmi`：删除这些镜像。

------

## 10. 查看容器的详细信息

如果需要查看容器的详细信息（例如环境变量、配置等），可以使用以下脚本：

```
#!/bin/bash
# 查看容器的详细信息
CONTAINER_ID=$1
docker inspect $CONTAINER_ID
```

  解释：

-  `docker inspect`：提供容器的详细信息，包括网络配置、挂载卷等。

------

## 11. 监控容器的资源使用情况

```
#!/bin/bash
# 监控所有运行中容器的资源使用情况
docker stats --all
```

  解释：

-  `docker stats`：显示容器的实时 CPU、内存、网络等统计信息。
-  `--all`：包括所有容器，已停止的容器也会显示。

------

## 12. 重启所有容器

```
#!/bin/bash
# 重启所有容器
docker restart $(docker ps -q)
```

  解释：

-  `docker restart`：重启所有正在运行的容器。

------

## 13. 自动启动所有容器

```
#!/bin/bash
# 启动所有停止的容器
docker start $(docker ps -aq)
```

  解释：

-  `docker ps -aq`：列出所有容器 ID（包括停止的容器）。
-  `docker start`：启动容器。

------

## 14. 从容器复制文件

```
#!/bin/bash
# 从容器复制文件
CONTAINER_ID=$1
SOURCE_PATH=$2
DEST_PATH=$3
docker cp $CONTAINER_ID:$SOURCE_PATH $DEST_PATH
echo "从 $CONTAINER_ID 复制 $SOURCE_PATH 到 $DEST_PATH"
```

  解释：

-  `docker cp`：在容器和主机之间复制文件或目录。

------

## 15. 列出所有暴露的端口

```
#!/bin/bash
# 列出所有暴露的端口
docker ps --format '{{.ID}}: {{.Ports}}'
```

  解释：

-  `docker ps --format`：自定义输出格式，显示容器 ID 和暴露的端口。

------

## 16. 从备份恢复容器

```
#!/bin/bash
# 从 tar 备份恢复容器
BACKUP_FILE=$1
docker import $BACKUP_FILE restored_container:latest
echo "容器恢复为 'restored_container:latest'"
```

  解释：

-  `docker import`：从 tar 文件创建新的 Docker 镜像。
-  使用恢复后的镜像启动一个新的容器。

------

## 17. 检查所有容器的日志

```
#!/bin/bash
# 显示所有容器的日志
docker ps -q | xargs -I {} docker logs {}
```

  解释：

-  `docker ps -q`：列出所有运行中的容器 ID。
-  `xargs`：将容器 ID 传递给 `docker logs`，以查看日志。

------

## 18. 删除挂起的容器

有时容器会被暂停或进入挂起状态，您可以使用以下脚本来自动清理这些状态异常的容器：

```
#!/bin/bash
# 删除挂起的容器
docker rm $(docker ps -aq -f "status=paused")
```

  解释：

-  `docker ps -aq -f "status=paused"`：列出所有被暂停的容器。
-  `docker rm`：删除这些暂停的容器。

------

## 19. 更新运行中的容器

```
#!/bin/bash
# 更新运行中的容器
CONTAINER_NAME=$1
IMAGE_NAME=$(docker inspect --format='{{.Config.Image}}' $CONTAINER_NAME)
docker pull $IMAGE_NAME
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
docker run -d --name $CONTAINER_NAME $IMAGE_NAME
```

  解释：

-  `docker inspect --format='{{.Config.Image}}'`：获取容器的镜像名称。
-  拉取镜像的最新版本并重建容器。

------

## 20. 停止所有运行中的容器

```
#!/bin/bash
# 停止所有运行中的容器
docker stop $(docker ps -q)
```

  解释：

-  `docker ps -q`：列出所有正在运行的容器的 ID。
-  `docker stop`：停止容器。