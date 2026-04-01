# 最实用的Nginx配置笔记

Nginx是一款轻量级的Web 服务器/反向代理服务器及电子邮件（IMAP/POP3）代理服务器，在BSD-like 协议下发行。其特点是占有内存少，并发能力强，事实上nginx的并发能力在同类型的网页服务器中表现较好。

网上关于Nginx文章介绍非常多，但是老感觉说的要不是太多太广泛，要不就是瞄准一个点说的太细，并没有针对一个web项目，列出其最基本，最常用的配置。所以我想总结一篇，不敢说100%，就是大部分的项目其实有下面介绍的配置就完全能跑起来，够用。如果需要个性化的或者特殊的配置，再去搜索。

**Nginx应用场景**

- http服务器：

  Nginx是一个http服务可以独立提供http服务。可以做网页静态服务器。

- 反向代理：

   反向代理是针对服务器来说的，一般来说是 客户端直接访问服务器，反向代理是客户端->Nginx->后端接口

- 负载均衡：

  当网站并发量大时，一台服务器已经无法承受，此时需要部署多个服务器来分担压力，这时候可以通过Nginx配置来将请求，通过一定分发规则，分发到不同的服务器来达到负载的作用。

  Nginx可以通过反向代理来实现负载均衡。

- 虚拟主机：

  有的网站访问量大，需要负载均衡。然而并不是所有网站都如此出色，有的网站，由于访问量太小，需要节省成本，将多个网站部署在同一台服务器上。

  例如将www.abc.com和www.bca.com两个网站部署在同一台服务器上，两个域名解析到同一个IP地址，但是用户通过两个域名却可以打开两个完全不同的网站，互相不影响，就像访问两个服务器一样，所以叫两个虚拟主机。

- 解决跨域问题

  项目开发过程中，有时候前端需要同时访问两个服务的后端接口，两个服务的端口肯定不一样，这时候通过Nginx配置转发就可以实现跨域访问。

**静态界面配置**

```
server {  
	listen       10117;  
	access_log  logs/host.10117.log  ;  
	charset utf-8;  
	location / {      
		charset utf-8;      root D:\hbidding\hst-meet\web\meet; #静态界面路径      
		index index.html; #默认首页地址    
	}
}
```



**后端服务器转发配置**

```
server {    
	listen       9006;  #监听端口   
    access_log  logs/host.9006.log ; #日志    
    server_name www.baidu.com; #可以不写，不写默认当前服务器   
    # 表示以 purchaser 开头的地址    
    location /purchaser {            
    		proxy_pass http://127.0.0.1:7132;           
        	proxy_set_header   Host    $http_host ;            
        	proxy_set_header   X-Real-IP   $remote_addr;            
        	proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;       
        }   
     # /表示所有地址    
     location / {                    
     		proxy_pass http://127.0.0.1:8006;           
     		proxy_set_header   Host    $http_host ;            
    		proxy_set_header   X-Real-IP   $remote_addr;           
    		proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;        
     	}        
     error_page   500 502 503 504  /50x.html;
}
```

设置

| 指令 | 说明                      |
| ---- | ------------------------- |
| =    | 精准匹配，优先级最高      |
| ^~   | 表示uri以某常规字符串开头 |
| ~    | 区分大小写的正则匹配      |
| ~*   | 不区分大小写的正则匹配    |
| ! ~  | 区分大小写不匹配正则      |
| ! ~* | 不区分大小写不匹配的正则  |
| /    | 通用匹配，匹配任何请求    |



**优先级：**

**表格依次向下，也就是“=”最高 “/” 最低**



**websocket配置**

```
location / {       
	...       
    #其他配置不变，下面添加这两列配置。       
    proxy_set_header Upgrade $http_upgrade;       
    proxy_set_header Connection "upgrade";
}
```



**负载均衡**

```
upstream mkj_pools {  
	server 192.168.1.72:8880   
	weight=1;  
	server 192.168.1.73:9990  
    weight=2;  
    server 192.168.1.74:8989  
    weight=3;  #weigth参数表示权值，权值越高被分配到的几率越大
}
server {   
	listen 80;  
	server_name www.mkj.com;  
	location / {      
    	proxy_pass http://mkj_pools;   
    }
}
```

**其他配置**

```
proxy_connect_timeout 60s; #nginx和后端服务器连接超时时间
proxy_read_timeout 300s; # 连接成功后，后端服务器响应时间
```

**Host X-Real-IP X-Forwarded-For**具体含义请看 [如何正确获取http客户端IP地址](http://mp.weixin.qq.com/s?__biz=MzkwMDY4Mzc5OA==&mid=2247483760&idx=1&sn=66653f6fe9a6e0362fa98228c8cdfb99&chksm=c0410009f736891f9d12b5357a1185ec7e2c75a75a68e30a9b76a06e69504c614024f067cc68&scene=21#wechat_redirect)

**Nginx常用命令**

```
//常用命令，使用命令需要先到nginx安装目录下
重启启动Nginx：nginx.exe -s reload
预编译：nginx.exe -t
停止所有服务：taskkill /f /im nginx.exe  //有模块新增时，需要先停止后启动才能生效
```

