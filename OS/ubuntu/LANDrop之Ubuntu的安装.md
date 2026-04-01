# LANDrop之Ubuntu的安装

## 下载地址

目前，这个软件[linux](https://so.csdn.net/so/search?q=linux&spm=1001.2101.3001.7020)应该只支持x86_x64架构，我自己在Ubuntu系统的arrch64架构上无法安装，望周知。
下载地址：https://landrop.app/#downloads，在下载页里选择Linux,将会下载一个.AppImage结尾 名为LANDrop-latest-linux.AppImage的文件。

## 安装流程

默认打开终端
在/home目录下创建一个LANDrop文件夹

```bash
mkdir LANDrop
```

将下载的LANDrop-latest-linux.AppImage拷贝进LANDrop文件夹内

```bash
mv LANDrop-latest-linux.AppImage /home/自己系统的地址/LANDrop
```

进入该目录

```bash
cd /home/自己系统的地址/LANDrop
```

允许文件作为程序执行

```bash
sudo chmod 777 LANDrop-latest-linux.AppImage
```

对AppImage文件进行解压

```bash
./LANDrop-latest-linux.AppImage --appimage-extract
```

解压完成后，将生成一个squashfs-root文件夹，进入它

```bash
 cd squashfs-root
```

运行软件

```bash
./AppRun
```

至此，就可以在[ubuntu系统](https://so.csdn.net/so/search?q=ubuntu系统&spm=1001.2101.3001.7020)上使用该软件了

## 创建桌面图标

美中不足的是，用上文的操作，每次运行软件都必须进文件夹内启动`./AppRun`，而且启动后的终端不能退出，否则软件也将退出，因此，给这个软件创建一个桌面图标能避免该现象发生。
默认打开终端

```bash
cd ~/.local/share/applications
```

编辑桌面程序代码

```bash
gedit LANDrop.desktop
```

弹出来的文件中输入（注意大小写、不包含中文与空格）

```bash
[Desktop Entry]
Name=LANDrop
Icon=/home/自己的地址/LANDrop/squashfs-root/LANDrop.svg
Exec=/home/自己的地址/LANDrop/squashfs-root/AppRun
Type=Application
```

增加权限

```bash
chmod +x LANDrop.desktop
```

好了，现在你就可以在你的桌面程序中搜索软件名，然后添加收藏，就可以在桌面栏中现显示出来了。