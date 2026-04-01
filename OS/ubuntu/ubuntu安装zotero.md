# ubuntu安装Zotero,任何版本ubuntu适用



两个方法

#### 1.方法一(简单但是不好使)

这个方法没有科学的络网很慢，**适用于所有的版本**

```bash
# 添加ppa
$ sudo apt-add-repository ppa:smathot/cogscinl 
# 更新源
$ sudo apt-get update
# 下载--
$ sudo apt-get install zotero-standalone
```

#### 2. 方法二（**※五星推荐※**）

适用任何版本该方法

- 从`zotero`官网下载安装包

目前官网下载的最新的版本是`Zotero-5.0.89_linux-x86_64.tar.bz2`。

- 解压文件

解压在当前，生成了`Zotero_linux-x86_64`这个文件夹，这个文件夹包含了`zotero`这个软件的所有的文件。

- 创建zotero目录

这里选择的是`/opt/`这个目录下创建的，因为这个目录通常放下`Google Chrome`和火狐浏览器和`pycharm`。

```bash
sudo mkdir /opt/zotero
```

- 复制解压文件到`/opt/zotero`目录下

```bash
# Zotero_linux-x86_64是解压的zotero所有
sudo mv Zotero_linux-x86_64/* /opt/zotero/
```

- 更新`zotero`的桌面位置

```bash
cd /opt/zotero
sudo ./set_launcher_icon
```

- 创造软连接到应用程序桌面

```bash
ln -s /opt/zotero/zotero.desktop ~/.local/share/applications/zotero.desktop
```

这时候搜索`zotero`会存在了