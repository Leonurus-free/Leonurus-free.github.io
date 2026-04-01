# centos安装google-chrome

## 一、最新版RPM安装

### 1、安装依赖

```cobol
yum install liberation-fonts -y

yum install vulkan -y

yum -y install redhat-lsb*

yum -y install libXss*

yum -y install libappindicator*

yum -y install libgbm
```

 

### 2、下载google-chrome RPM

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
```

### 3、安装google-chrome

```cobol
rpm -ivh google-chrome-stable_current_x86_64.rpm
```

### 4、查看google-chrome版本

```bash
google-chrome --version
```

## 三、下载chromedriver

### 1、根据google-chrome版本号下载对应的驱动

下载链接：[https://googlechromelabs.github.io/chrome-for-testing/#stable](https://registry.npmmirror.com/binary.html?path=chromedriver/)

https://googlechromelabs.github.io/chrome-for-testing/

### 2、使用unzip解压

```python
unzip chromedriver-linux64.zip
```

### 3、设置可执行权限

```perl
chmod +x chromedriver
```

4、移动位置

~~~bash
cp chromedriver /usr/local/bin/
~~~

5、查看驱动版本

~~~bash
chromedriver --version
~~~

