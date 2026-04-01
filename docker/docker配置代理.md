# docker配置代理

设置docker 代理
Docker 使用代理拉取镜像

~~~
vim  /etc/systemd/system/docker.service.d/proxy.conf
~~~

填入如下内容
~~~
[Service]
Environment="HTTP_PROXY=socks5://192.168.20.21:1080"
Environment="HTTPS_PROXY=socks5://192.168.20.21:1080"

~~~

重启Docker

~~~
sudo systemctl daemon-reload && 
sudo systemctl restart docker
~~~



检查Docker有没有使用VPN

~~~
systemctl show --property=Environment docker

~~~

出现
Environment=HTTP_PROXY=http://127.0.0.1:7890 HTTPS_PROXY=http://127.0.0.1:7890
此时Docker就已经自动实现代理喽。后续拉取镜像不需要追加参数，直接使用即可哦！



