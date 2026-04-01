# ubuntu安装win字体

1. 找到C:/Windows目录，将其中的Fonts文件夹拷贝至ubuntu中。
2. 将该文件夹放至ubuntu的/usr/share/fonts目录下面，可用下列命令。

```bash
sudo cp -r Fonts /usr/share/fonts/winfonts
```

3.进行安装。

```bash
sudo mkfontscale
sudo mkfontdir
sudo fc-cache
```