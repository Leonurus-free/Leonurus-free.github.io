# ubuntu中安装redis

### 1. 更新包列表

首先，确保你的系统包列表是最新的，这样你可以获取到最新的软件包信息。打开终端并运行下面的命令：

```bash
sudo apt update
```

### 2. 安装Redis

接下来，使用`apt`命令来安装Redis。在终端中输入以下命令：

```bash
sudo apt install redis-server
```

这个命令会安装`redis-server`以及相关的依赖包。安装过程可能需要一些时间，根据你的网络速度和系统状态而定。

### 3. 验证安装

安装完成后，你可以检查Redis服务是否正在运行。运行以下命令：

```bash
sudo systemctl status redis
```

如果一切顺利，你将看到Redis服务正在运行的消息。

### 4. 测试Redis

你可以使用Redis的命令行工具`redis-cli`来测试Redis是否工作正常。运行以下命令：

```bash
redis-cli
```

这将启动Redis命令行界面。你可以尝试输入`ping`命令来测试Redis是否响应：

```bash
ping
```

如果一切正常，你应该会看到`PONG`的响应。

### 5. 配置防火墙（可选）

如果Ubuntu系统启用了UFW防火墙，你需要打开Redis的默认端口（6379）以允许外部连接。运行以下命令：

```bash
sudo ufw allow 6379/tcp
```

这将允许通过TCP协议的6379端口的连接。

### 6. 配置Redis（可选）

你可能需要根据你的需求来配置Redis。默认配置文件位于`/etc/redis/redis.conf`。你可以使用文本编辑器（如`nano`或`vi`）来编辑这个文件。

例如，如果你想更改Redis监听的IP地址或端口，你可以在配置文件中找到`bind`和`port`行进行修改。

### 7. 重启Redis服务

如果修改了配置文件，需要重启Redis服务以应用新的设置。运行以下命令：

```bash
sudo systemctl restart redis
```

以上步骤将指导你完成在Ubuntu中安装和配置Redis的过程。



- 如果没有使用systemd，或者你不确定容器的初始化系统，你可以停止并重新启动Redis服务器：

  ```bash
  redis-cli -p 6379 shutdown
  redis-server /etc/redis/redis.conf
  ```