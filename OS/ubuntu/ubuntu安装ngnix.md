# ubuntu安装ngnix

# Ubuntu20.04安装配置Nginx

#### 1. 安装nginx

##### 1.1 安装及常用命令

```shell
# 更新apt-get源
sudo apt-get update
# 安装
sudo apt-get install nginx
# 安装后将自动开启nginx服务，打开浏览器输入ip即可查看初始页面

# 查看安装版本
nginx -v
# 输出:nginx version: nginx/1.18.0 (Ubuntu)

# systemctl命令
# 查看状态
sudo systemctl status nginx
# 启动
sudo systemctl start nginx
# 停止
sudo systemctl stop nginx
# 重启
sudo systemctl restart nginx
```

**注意：\**对nginx配置文件修改之后，都要\**重启nginx服务**，加载修改后的配置文件

##### 1.2 文件结构

```shell
# 查看文件结构
tree /etc/nginx

/etc/nginx
├── conf.d
├── fastcgi.conf
├── fastcgi_params
├── koi-utf
├── koi-win
├── mime.types
├── modules-available
├── modules-enabled
│   ├── 50-mod-http-image-filter.conf -> /usr/share/nginx/modules-available/mod-http-image-filter.conf
│   ├── 50-mod-http-xslt-filter.conf -> /usr/share/nginx/modules-available/mod-http-xslt-filter.conf
│   ├── 50-mod-mail.conf -> /usr/share/nginx/modules-available/mod-mail.conf
│   └── 50-mod-stream.conf -> /usr/share/nginx/modules-available/mod-stream.conf
├── nginx.conf
├── proxy_params
├── scgi_params
├── sites-available
│   └── default
├── sites-enabled
│   └── default -> /etc/nginx/sites-available/default
├── snippets
│   ├── fastcgi-php.conf
│   └── snakeoil.conf
├── uwsgi_params
└── win-utf
```

##### 1.3 配置文件内容

**nginx.conf** （为了方便看，我删掉了初始内容中所有带注释的代码）

```nginx
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 768;
}

http {

	sendfile on;
	tcp_nopush on;
	tcp_nodelay on;
	keepalive_timeout 65;
	types_hash_max_size 2048;

	include /etc/nginx/mime.types;
	default_type application/octet-stream;

	ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE
	ssl_prefer_server_ciphers on;

	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;

	gzip on;

	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
}
```

最关键的是下面两行引入，上面的代码含义目前我还没研究，用到再说

```nginx
include /etc/nginx/conf.d/*.conf;
include /etc/nginx/sites-enabled/*;
```

这两行的意思是：从conf.d中加载所有后缀为conf的文件，从sites-enabled中加载所有文件，均作为配置文件

sites-enabled文件我用不习惯，因此我注释掉了这行，使用conf.d做配置文件

**在conf.d中添加`static.conf`**

```nginx
server {
    listen       80;
    server_name  localhost;

    charset utf-8; # 防止中文显示出现乱码

    #access_log  logs/host.access.log  main;

    location / {
        root   /var/www/html; # 你的静态资源路径
        index  index.html index.htm;# 访问的文件为html, htm
    }
}
```

要注意的是，在`/var/www/html`目录中，文件的名字不是`index.html`，原名为`index.nginx.debian.html`，改成前者即可。

通过三处修改，完成从`sites-enable`到`conf.d`的迁移

- 在`nginx.conf`中注释掉`include /etc/nginx/sites-enabled/*;`
- 在`conf.d`目录下新建`static.conf`，添加如上文件内容
- 修改`/var/www/html`目录中的文件名为`index.html`

```shell
# 检查配置文件是否有误
nginx -t
# nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
# nginx: configuration file /etc/nginx/nginx.conf test is successful

# 重启服务
sudo systemctl restart nginx
```

#### 2. 配置静态服务器

自行寻找一个网页做测试，上传到`/var/www/html`

我上传了之前写过的一个markdown在线编辑器，是一个文件夹，文件夹名为`markdown`

**开始修改`static.conf`文件**

```nginx
server {
    listen       80;
    server_name  localhost;

    charset utf-8; # 防止中文显示出现乱码

    # 根据自己需要配置日志文件，可以单独配置，也可以全部放在/var/log/nginx的日志中
    #access_log  logs/host.access.log  main;

    location / {
        root   /var/www/html; # 你的静态资源路径
        index  index.html index.htm;# 访问的文件为html, htm
    }
    
    location /markdown {
        alias   /var/www/html/markdown; # 你的静态资源路径
        index  index.html index.htm;# 访问的文件为html, htm
    }
    
    # 后续如果有其他配置，模仿markdown的配置添加即可
    # location /example {
    #     alias   /var/www/html/example; # 你的静态资源路径
    #     index  index.html index.htm;# 访问的文件为html, htm
    # }
}
```

**对于多个路径的配置：** [1]

- 使用**root**会将location后的markdown追加在路径的尾部，在访问时就会访问到/var/www/html/markdown/markdown
- 使用**alias**则不会将location后的markdown追加在路径尾部，访问时就为正确路径/var/www/html/markdown

**如果添加`charset utf-8;`后还存在乱码，强制刷新一下试试**

输入`IP/markdown`查看配置结果

#### 3. 配置端口转发

自行寻找一个服务做测试，开在非80端口即可，我开在了8822端口

**注：要在服务器的安全组配置，打开对应端口**

首先测试一下 IP:8822 能不能正常使用，可以使用说明服务成功启动在8822端口，进行后续配置。

```nginx
server {
    listen       80;
    server_name  localhost;
 
    charset utf-8; # 防止中文显示出现乱码

	# 添加头部信息
    proxy_set_header  Cookie $http_cookie;
    proxy_set_header  X-Forwarded-Host $Host;
    proxy_set_header  proxy_set_Server  $Host;
    proxy_set_header  X-Forwarded-For $proxy_add_x_forwarded_for;
	
    # 访问IP/eat，则会自动访问对应地址IP:8822
    location /eat/ {
        proxy_pass http://localhost:8822/;
    }
    
    # 后续如果有其他配置，模仿eat的配置添加即可
    # 访问IP/example，则会自动访问对应地址IP:port
    # location /example/ {
    #     proxy_pass http://localhost:port/;
    # }
}
```

输入`IP/eat`查看配置结果

#### 4. 配置域名

我从阿里云购买了域名southyang.cn，将子域名demo.southyang.cn解析到服务器上

**以端口转发为例：**

```nginx
server {
    listen       80;
    server_name  demo.southyang.cn;
 
    charset utf-8; # 防止中文显示出现乱码

	# 添加头部信息
    proxy_set_header  Cookie $http_cookie;
    proxy_set_header  X-Forwarded-Host $Host;
    proxy_set_header  proxy_set_Server  $Host;
    proxy_set_header  X-Forwarded-For $proxy_add_x_forwarded_for;
	
    # 访问demo.southyang.cn/eat，则会自动访问对应地址IP:8822
    location /eat/ {
        proxy_pass http://localhost:8822/;
    }
    
    # 后续如果有其他配置，模仿eat的配置添加即可
    # 访问IP/example，则会自动访问对应地址IP:port
    # location /example/ {
    #     proxy_pass http://localhost:port/;
    # }
}
```

输入`demo.southyang.cn/eat`查看配置结果

#### 5. 配置https

**以端口转发为例：** [2]

```nginx
server {
    listen 80;
    server_name demo.southyang.cn;
    # 跳转https
    return 301 https://$host$request_uri;
}

server {
    listen 443   ssl http2;
    server_name  demo.southyang.cn;
 
    charset utf-8; # 防止中文显示出现乱码

	# 添加头部信息
    proxy_set_header  Cookie $http_cookie;
    proxy_set_header  X-Forwarded-Host $Host;
    proxy_set_header  proxy_set_Server  $Host;
    proxy_set_header  X-Forwarded-For $proxy_add_x_forwarded_for;
    
    # 配置证书
    ssl_certificate 证书密钥地址
    ssl_certificate_key 证书公钥地址
    ssl_verify_client off;
    proxy_ssl_verify off;
	
    # 访问demo.southyang.cn/eat，则会自动访问对应地址IP:8822
    location /eat/ {
        proxy_pass http://localhost:8822/;
        proxy_redirect off;
    }
    
    # 后续如果有其他配置，模仿eat的配置添加即可
    # 访问IP/example，则会自动访问对应地址IP:port
    # location /example/ {
    #     proxy_pass http://localhost:port/;
    # }
}
```

输入`demo.southyang.cn/eat`查看配置结果

**注：** 目前我只用到了上述所列的内容，其他内容用到了再学