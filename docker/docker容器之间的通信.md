# docker容器之间的通信



## 创建自定义网络

~~~
docker network create my_network_1
~~~

### 1. **创建一个自定义网络**

首先，你需要创建一个新的自定义网络。你可以选择创建一个 `bridge` 类型的网络（这是默认的网络类型），或者创建其他类型的网络（例如 `host` 或 `overlay`，这取决于你的需求）。

```

docker network create my_custom_network
```

这个命令会创建一个名为 `my_custom_network` 的自定义网络。

### 2. **将已存在的容器连接到自定义网络**

你可以使用 `docker network connect` 命令将已存在的容器连接到这个新创建的自定义网络。

```
docker network connect my_custom_network <container_name_or_id>
```

替换 `<container_name_or_id>` 为你要连接的容器的名称或 ID。例如，如果你的容器名为 `mysql-container`，则命令是：

```
docker network connect my_custom_network mysql-container

docker network connect my_network_1 mysql_8.0
```

### 3. **确认容器已连接到网络**

你可以使用以下命令来检查容器是否已成功连接到自定义网络：

```
docker inspect <container_name_or_id>

docker inspect mysql_8.0
```

查看输出中的 `Networks` 部分，确认容器是否已连接到 `my_custom_network` 网络。例如：

```
json复制代码"Networks": {
    "bridge": {
        "NetworkID": "xyz123",
        "EndpointID": "abc456",
        "Gateway": "172.17.0.1",
        "IPAddress": "172.17.0.2",
        "IPPrefixLen": 16,
        "IPv6Gateway": "",
        "MacAddress": "02:42:ac:11:00:02",
        "DriverOpts": null
    },
    "my_custom_network": {
        "NetworkID": "my_custom_network_id",
        "EndpointID": "custom_endpoint_id",
        "Gateway": "172.18.0.1",
        "IPAddress": "172.18.0.2",
        "IPPrefixLen": 16,
        "IPv6Gateway": "",
        "MacAddress": "02:42:ac:12:00:02",
        "DriverOpts": null
    }
}
```

如果你在 `Networks` 部分看到 `my_custom_network`，说明容器已经成功连接到该网络。

### 4. **容器断开网络（如果需要）**

如果你想将容器从自定义网络断开，可以使用以下命令：

```
docker network disconnect my_custom_network <container_name_or_id>
```

### **注意事项**

- 如果容器已经在运行中，将它连接到新的网络不会导致容器重启。容器可以同时连接到多个网络。
- 如果容器通过 `docker run` 启动时没有指定 `--network` 参数，默认会连接到 `bridge` 网络。你可以使用 `docker network connect` 将容器从默认网络连接到其他网络。





#####  **从 `my-app-container` 连接到 `mysql-container`**

现在，你可以从 `my-app-container` 通过容器名 `mysql-container` 访问 MySQL 服务。例如，使用 Python 连接 MySQL：

```
python复制代码import mysql.connector

# 使用容器名称 'mysql-container' 作为主机
connection = mysql.connector.connect(
    host='mysql-container',  # 容器名
    port=3306,  # 默认 MySQL 端口
    user='root',
    password='my_password',
    database='your_database'
)

cursor = connection.cursor()
cursor.execute("SELECT DATABASE();")
print(cursor.fetchone())
connection.close()
```

在这个例子中，`host` 使用的是 MySQL 容器的名称 `mysql-container`，而不是 IP 地址，因为 Docker 会在同一网络内通过容器名解析 IP 地址。



## mysql更改用户身份验证插件

使用 `ALTER USER` 语句将用户的身份验证插件更改为 `mysql_native_password`，并为用户设置一个密码（如果你还没有设置密码）：

```
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'your_password';
```

- `root`：这是用户名，替换为你实际使用的用户名。
- `your_password`：这是你要设置的密码。

你可以将 `root` 替换为其他用户，例如 `'myuser'`，如果你使用的是其他用户进行连接。

**刷新权限** 在更改完用户的身份验证插件后，执行以下命令来刷新权限：

```
FLUSH PRIVILEGES;
```

**退出 MySQL** 完成后，退出 MySQL