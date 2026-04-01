# ubuntu安装libreoffice

### 安装

添加 官方PPA

```bash
sudo add-apt-repository ppa:libreoffice/ppa
```

安装

```bash
sudo apt update
sudo apt install libreoffice
```

### 卸载

```bash
sudo apt remove --purge libreoffice*
sudo rm -rf /home/<username>/.config/libreoffice
```

- 注意：不删除`config/libreoffice`可能在重新安装 LibreOffice 时出现问题

清除不再需要的依赖包

```bash
sudo apt-get autoremove
sudo apt-get autoclean
```

### 卸载PPA

~~~
sudo add-apt-repository --remove ppa:libreoffice/ppa
~~~

