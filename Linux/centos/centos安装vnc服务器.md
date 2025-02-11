# centos安装vnc服务器

1、关闭防火墙和selinux

```
systemctl stop firewalld.service
setenforce 0
```

2、安装图形支持

```
yum groups install "GNOME Desktop" -y
```

3、安装vncserver

```
yum -y install tigervnc-server
```

4、修改配置文件

```
cp /lib/systemd/system/vncserver@.service /etc/systemd/system/vncserver@:1.service

vim /etc/systemd/system/vncserver@\:1.service 
```

找到如下行

```
ExecStart=/usr/bin/vncserver_wrapper <USER> %i
```

我以root登陆，所以修改为

```
ExecStart=/usr/sbin/runuser -l root -c "/usr/bin/vncserver %i"
PIDFile=/root/.vnc/%H%i.pid
```

5、重新加载systemd

```
systemctl daemon-reload
```

6、设置vnc登陆密码

```
vncpasswd 
```

7、启动vncserver

```
systemctl enable vncserver@:1.service
systemctl start vncserver@:1.service
```

8、查看是否正常启动

```
ps -ef | grep vnc

systemctl status vncserver@:1.service
```

至此vncserver搭建完毕。

在windows上面安装VNC Viewer软件，连接远程主机.

IP:1即可远程



当vnc连接出错的时候，我们通常可以查看log文件看具体什么错误。

通过命令：


```perl
vncserver -kill :1
```

把端口1的vnc服务杀掉，然后再启用vnc:

```undefined
vncserver
```

然后就会打印vnc的log文件位置：



然后vim编辑器查看错误：

```cobol
vim /root/.vnc/firefly:1.log
```





问题：**Could not make bus activated clients aware of XDG_CURRENT_DESKTOP=GNOME environment variable:**
**Could not connect: Connection refused**

**解决方案一：**

```
[root@kevin ~]# cat /root/.vnc/kevin:1.log

...........

...........

(imsettings-check:31898): GLib-GIO-CRITICAL **: 21:56:03.842: g_dbus_proxy_call_sync_internal: assertion 'G_IS_DBUS_PROXY (proxy)' failed

GLib-GIO-Message: 21:56:03.854: Using the 'memory' GSettings backend.  Your settings will not be saved or shared with other applications.

 

** (process:31798): WARNING **: 21:56:03.861: Could not make bus activated clients aware of XDG_CURRENT_DESKTOP=GNOME environment variable:

Could not connect: Connection refused

 

原因：dbus-daemon存在冲突。

因为root系统环境中装有anaconda，它的bin目录中的dbus-daemon会与系统自带的dbus-daemon冲突。
[root@kevin ~]# find / -name "dbus-daemon"

/usr/bin/dbus-daemon

/data/anaconda3/bin/dbus-daemon

/data/anaconda3/pkgs/dbus-1.13.6-h746ee38_0/bin/dbus-daemon

 

[root@kevin ~]# which dbus-daemon

/data/anaconda3/bin/dbus-daemon

 

解决办法：使用非root用户启动vncserver

[root@kevin ~]# useradd vncuser

[root@kevin ~]# echo "vncuser@123"|passwd --stdin vncuser

[root@kevin ~]# vim /etc/sudoers

vncuser ALL=(ALL)       NOPASSWD: ALL

 

修改vncserver使用vncuser这个非root用户启动

[root@kevin ~]# cat /etc/systemd/system/vncserver@:1.service

..........

..........

ExecStart=/usr/sbin/runuser -l vncuser -c "/usr/bin/vncserver %i"

PIDFile=/root/.vnc/%H%i.pid

 

接着切入到非root用户vncuser下启动vncserver

[root@kevin ~]# su - vncuser

Last login: Tue Jul  2 22:05:38 CST 2019 on pts/2

 

设置vnc登录密码

[vncuser@kevin ~]$ vncpasswd

 

启动vnc

[vncuser@kevin ~]$ vncserver

 

查看vnc日志

[vncuser@kevin ~]$ cd .vnc/

[vncuser@kevin .vnc]$ ll

total 20

-rw-r--r-- 1 vncuser vncuser  332 Jul  2 22:06 config

-rw-rw-r-- 1 vncuser vncuser 1046 Jul  2 22:10 kevin:1.log

-rw-rw-r-- 1 vncuser vncuser    5 Jul  2 22:06 kevin:1.pid

-rw------- 1 vncuser vncuser    8 Jul  2 22:06 passwd

-rwxr-xr-x 1 vncuser vncuser  112 Jul  2 22:06 xstartup

 

[vncuser@kevin .vnc]$ cat kevin\:1.log

 

Xvnc TigerVNC 1.8.0 - built Nov  2 2018 19:05:14

Copyright (C) 1999-2017 TigerVNC Team and many others (see README.txt)

See http://www.tigervnc.org for information on TigerVNC.

Underlying X server release 12001000, The X.Org Foundation

 

 

Tue Jul  2 22:06:26 2019

 vncext:      VNC extension running!

 vncext:      Listening for VNC connections on all interface(s), port 5901

 vncext:      created VNC server for screen 0

touch: cannot touch ‘/home/vncuser/.cache/imsettings/log’: No such file or directory

 

Tue Jul  2 22:06:30 2019

 ComparingUpdateTracker: 0 pixels in / 0 pixels out

 ComparingUpdateTracker: (1:-nan ratio)

 

Tue Jul  2 22:10:22 2019

 Connections: accepted: 192.168.1.200::56162

 

Tue Jul  2 22:10:23 2019

 Connections: closed: 192.168.1.200::56162 (reading version failed: not an RFB

              client?)

 EncodeManager: Framebuffer updates: 0

 EncodeManager:   Total: 0 rects, 0 pixels

 EncodeManager:          0 B (1:-nan ratio)

 ComparingUpdateTracker: 0 pixels in / 0 pixels out

 ComparingUpdateTracker: (1:-nan ratio)
```

**解决方案二：**

~~~
vim ~/.bashrc

注释anconda内容

source ~/.bashrc

reboot

当vnc启动后，再修改~/.bashrc添加已注释anconda内容
再source ~/.bashrc即可
~~~

