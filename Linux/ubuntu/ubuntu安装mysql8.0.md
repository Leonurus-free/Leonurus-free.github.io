# ubuntu安装mysql8.0

## （无法设置 Root 密码）

> Ubuntu在20.04版本中，源仓库中MySQL的默认版本已经更新到8.0。可以直接使用apt安装。

### apt 安装MySQL

```sh
sudo apt-get update  #更新源
sudo apt-get install mysql-server #安装

sudo apt install net-tools

# 修改root密码
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '1qaz2wsx';

```

### MySQL服务管理

```sh
sudo service mysql status # 查看服务状态
sudo service mysql start # 启动服务
sudo service mysql stop # 停止服务
sudo service mysql restart # 重启服务
```

### 登录

查看密码使用这条查看

```sh
sudo cat /etc/mysql/debian.cnf
```

使用默认账户登录

```sh
mysql -u debian-sys-maint -p
```

或直接进入 Mysql

```sh
sudo mysql
```

> 找不到初始密码可以在my.ini中 [mysqld] 添加：`skip-grant-tables`

## 创建新用户

因为方法二尝试修改了root账户的密码似乎不起作用，于是创建一个新的账户来作为日常使用

### **新建账户**

新建一个free用户，密码为free

```sh
create user 'free'@'%' identified by 'free';
```

**授权**

```sh
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

修改MySQL数据库配置文件无密码登录后，修改密码报错为以下

```sh
ERROR 1290 (HY000): The MySQL server is running with the --skip-grant-tables option so it cannot execute this statement
```

则需先执行：`FLUSH PRIVILEGES;` 后再执行修改密码命令即可。

**重置密码**

重置root账户密码为 password

```sh
SET PASSWORD FOR root@'localhost' = PASSWORD('password');
```

或者执行

```sh
SET PASSWORD FOR root@'localhost' = 'password';
```

# 二、注释bind-address = 127.0.0.1

在Ubuntu系统中，MySQL默认只能本地访问，不能远程访问，因为访问地址被绑定死了为本地127.0.0.1，想要远程访问的话，需要去`/etc/mysql/mysql.conf.d/mysqld.cnf`中找到`bind-address = 127.0.0.1`，然后注释掉这一句，也就是在这句前面加上`#`号。

然后重启MySQL就可以了。
重启命令为：`service mysql restart`



## 卸载MySQL

```sh
sudo apt purge mysql-*
sudo rm -rf /etc/mysql/ /var/lib/mysql
sudo apt autoremove
sudo apt autoclean
```

注意如果要卸载需要卸载干净！避免影响以后的重新安装



### 错误

### MySQL报错：ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock'

出现问题原因：

有可能是 my.cnf 配置文件中设置了 [mysqld] 的参数 socket ，而没有设置[client]的参数socket

mysql.sock 文件有什么用：

**mysql 支持 socket 和 TCP/IP 连接。那么 mysql.sock 这个文件有什么用呢？连接localhost通常通过一个Unix域套接字文件进行，一般是/tmp/mysql.sock。如果套接字文件被删除了，本地客户就不能连接。/tmp 文件夹属于临时文件，随时可能被删除。**

1.TCP 连接**(如果报错 /tmp/mysql.sock，你可以尝试这种方式连接)**

> ```
> mysql -uroot -h 127.0.0.1 -p
> ```

2.socket 连接

> ```
> mysql -uroot -p
> ```

**解决方式：**

在/etc/my.cnf文件 添加 [client] 配置项，如下所示

**配置前：(配置 [client] 前，会报错'/tmp/mysql.sock' (2))**

> ```
> [mysqld]
> datadir=/usr/local/mysql/data
> basedir=/usr/local/mysql
> socket=/var/lib/mysql/mysql.sock
> user=mysql
> # Disabling symbolic-links is recommended to prevent assorted security risks
> symbolic-links=0
> [mysqld_safe]
> log-error=/var/log/mysqld.log
> pid-file=/var/run/mysqld/mysqld.pid
> ```

**配置后：(配置 [client] 后，重启 mysql服务)**

> ```
> [mysqld]
> datadir=/usr/local/mysql/data
> basedir=/usr/local/mysql
> socket=/var/lib/mysql/mysql.sock（跟这个socket路径一样）
> user=mysql
> # Disabling symbolic-links is recommended to prevent assorted security risks
> symbolic-links=0
> [mysqld_safe]
> log-error=/var/log/mysqld.log
> pid-file=/var/run/mysqld/mysqld.pid
> [client]
> port=3306
> socket=/var/lib/mysql/mysql.sock
> ```

end，本文结束，希望对大家有所帮助！