	server{
	    listen       10010;
	    server_name  localhost;
	
	    location /{
	        proxy_pass  http://127.0.0.1:7000/;
	    }
	    location /OutputFile/{
	        root /home/luo/Project/OutputFile;
	    }
	}

**Centos nginx重启**

**重启Nginx**

**service nginx restart
/etc/init.d/nginx stop
/etc/init.d/nginx start**

**[Ubuntu](http://www.111cn.net/list-202/) Nginx**

$sudo service nginx start

$​sudo service nginx stop



