# 安装步骤

## 安装并启用 SSH 服务

如果host上还没有ssh服务, 安装一下, 方便后面的安装步骤, 远程通过ssh进行. 如果不安装, 本机关闭桌面在命令行下也可以, 就是调试起来不方便

```bash
sudo apt install openssh-server
sudo systemctl status ssh.service 
# 确认是否开机自启动
sudo systemctl is-enabled ssh.service 
```

## 初始安装

(可选)安装XFCE桌面. 如果想使用自带的 Ubuntu桌面, 也可以不安装

```bash
sudo apt install xfce4 xfce4-goodies
```

安装vncserver

```bash
sudo apt install tigervnc-standalone-server
```

上面的安装完之后, 用普通用户在ssh连接(或者命令行终端)中启动一次

```bash
vncserver
```

过程中会让你设置密码和只读密码, 会自动分配端口号. 查看启动后的实例

```bash
$ vncserver -list
 
TigerVNC server sessions:
 
X DISPLAY #	RFB PORT #	RFB UNIX PATH	PROCESS ID #	SERVER
2         	5902      	             	11368       	Xtigervnc
```

如果-list看不到实例, 说明启动失败, 需要`journalctl -fe`看一下具体原因

如果事后想再修改密码, 可以用`vncpasswd`命令

上面启动的服务, 默认是只监听本地127.0.0.1, 所以从其它机器是无法连接的, 如果需要连接, 可以用这个命令启动

```bash
vncserver -localhost no
```

## 配置和添加到系统服务

关闭刚才的实例, `:1`根据自己的实例修改

```bash
vncserver -kill :1
```

将 tigervncservice 服务添加到启动, `:1`根据自己的实例修改

```bash
sudo systemctl start tigervncserver@:1.service
sudo systemctl enable tigervncserver@:1.service
```

服务配置文件在 /lib/systemd/system/tigervncserver@.service , 因为服务使用的是 /usr/libexec/tigervncsession-start 这个脚本, 脚本里面调用的是 /usr/sbin/tigervncsession , 参考 https://manpages.ubuntu.com/manpages/impish/man8/tigervncsession.8.html, 需要在 ~/.vnc/ 下创建文件 config, 输入内容

```ini
session=ubuntu
geometry=2560x1440
securitytypes=vncauth,tlsvnc
```

- `session=xfce`如果前面安装了`xfce`, 这里可以用`xfce`, 否则需要改成`ubuntu`(Desktop版自带桌面)
  - 能用哪些值, 取决于 `/usr/share/xsessions` 目录下包含哪些 desktop. 例如使用自带的 Ubuntu桌面, 可以改成 `session=ubuntu`
  
- geometry=1366x768 是开启时的默认分辨率

- 如果要只允许本地连接, 可以加一行 `localhost`

修改完重启服务生效

```kotlin
sudo systemctl restart tigervncserver@:1.service
```



记住：先关闭系统自带的桌面



~~~
sudo systemctl set-default multi-user.target
~~~

然后重启



恢复方法

~~~
sudo systemctl set-default graphical.target
~~~





## ubuntu桌面

~~~
sudo apt install ubuntu-desktop
~~~



如果不配置xstartup刚开始可以远程桌面，但是过一段时间就不能显示了，报错：
~~~
Xsession: unable to launch "env GNOME_SHELL_SESSION_MODE=ubuntu /usr/bin/gnome-session --session=ubuntu" X session --- "env GNOME_SHELL_SESSION_MODE=ubuntu /usr/bin/gnome-session --session=ubuntu" not executable; falling back to default session.
~~~

我没有找到原因

解决办法就是：



### 配置xstatup

### **方法 1：直接运行 `gnome-session`（推荐）**

修改 `~/.vnc/xstartup`，去掉 `/etc/X11/Xsession`，直接运行 `gnome-session`：

```
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
export XDG_CURRENT_DESKTOP=ubuntu:GNOME
export GNOME_SHELL_SESSION_MODE=ubuntu
exec /usr/bin/gnome-session --session=ubuntu
```

注意：**以上方法可能依赖bash运行!**

**关键点**：

- `exec` 确保进程替换当前 shell，避免残留进程。

- 确保文件可执行：

  ```
  sudo chmod +x ~/.vnc/xstartup
  ```

------

### **方法 2：使用 `dbus-launch` 包装 GNOME 会话**

如果 GNOME 依赖 DBus，可以尝试：

```
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
export XDG_CURRENT_DESKTOP=ubuntu:GNOME
export GNOME_SHELL_SESSION_MODE=ubuntu
exec dbus-launch /usr/bin/gnome-session --session=ubuntu
```

------

### **方法 3：改用 `Xsession` 但简化参数**

如果必须使用 `/etc/X11/Xsession`，可以改为：

```
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
export XDG_CURRENT_DESKTOP=ubuntu:GNOME
export GNOME_SHELL_SESSION_MODE=ubuntu
exec /etc/X11/Xsession "gnome-session --session=ubuntu"
```

**注意**：将整个命令作为 **单个参数** 传递，避免 `Xsession` 解析错误。：q
