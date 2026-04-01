# Ubuntu安装搜狗输入法

#### 01. 更新应用源

```powershell
sudo apt update
```

#### 02. 安装输入法系统

```powershell
sudo apt-get install fcitx

# 使用最新的命令
sudo apt install fcitx5-frontend-gtk4
```

#### 03. 打开系统设置

![在这里插入图片描述](./ubuntu安装搜狗输入法/8a393ba21da355ea2e41b8f3484e5cd4.png)

#### 04. 打开语言支持窗口

① 设置 `键盘输入法` 系统为: fcitx
② 添加或删除语言: 中文简体、英文
③ 应用到整个系统
④ 重启系统
![在这里插入图片描述](./ubuntu安装搜狗输入法/1d7b08cf2a7a206826ce0c59a748478a.png)

#### 05. 设置fcitx开机自启动

```powershell
# 将fcitx.desktop文件复制到开机自启动目录中
# 命令格式: sudo cp "fcitx.desktop文件所在的位置"  "开机自启动目录"
sudo cp /usr/share/applications/fcitx.desktop /etc/xdg/autostart/
```

![在这里插入图片描述](./ubuntu安装搜狗输入法/81c982085eaacd0f8ab5223bf61102bb.png)

#### 06. 卸载ibus输入法系统（可以不要卸载）

```powershell
sudo apt purge ibus
```

![在这里插入图片描述](./ubuntu安装搜狗输入法/d9d94a50ca601335527f8130c26dd31b.png)

#### 07. 下载[搜狗输入法](https://so.csdn.net/so/search?q=搜狗输入法&spm=1001.2101.3001.7020)

[搜狗输入法官网下载地址](https://shurufa.sogou.com/)

需要选择适合你 `个人电脑` 的CPU架构进行下载
最好是直接使用UBuntu系统里的Firefox浏览器下载, 下载后的文件名称大致如此: `sogoupinyin_4.2.1.145_amd64.deb`
![在这里插入图片描述](./ubuntu安装搜狗输入法/3fa9d3c99f2277346f925de7d47e8510.png)

#### 08. 安装搜狗输入法

两种安装方式, 选择其一

> 方式一: 命令方式安装

```powershell
# sudo dpkg -i "安装包所在路径"
sudo dpkg -i "/home/getter/Downloads/sogoupinyin_4.2.1.145_amd64.deb"
```

> 方式二: 可视化安装

![在这里插入图片描述](./ubuntu安装搜狗输入法/35fb020ea8bfc44d5b636cf2b7108729.png)
![在这里插入图片描述](./ubuntu安装搜狗输入法/b1e13644efe1e18f75b5ad1885521a9f.png)![在这里插入图片描述](./ubuntu安装搜狗输入法/afad36ce0b49b52d9c686c349a73f087.png)

#### 09. 安装搜狗输入法所需要的其它依赖工具

安装完成后重启

```powershell
sudo apt install libqt5qml5 libqt5quick5 libqt5quickwidgets5 qml-module-qtquick2 libgsettings-qt1
```

![在这里插入图片描述](./ubuntu安装搜狗输入法/9febdf6820de3f5d238192a34050a7ce.png)

#### 10. 添加搜狗输入法到语言栏

![在这里插入图片描述](./ubuntu安装搜狗输入法/04a18e5a3375f89e42f247f6d2e033c6.png)
![在这里插入图片描述](./ubuntu安装搜狗输入法/431dcf719c6f028e6657d1e509ef70b5.png)
![在这里插入图片描述](./ubuntu安装搜狗输入法/2994dbfc3c8d50537f4e44b9c1178e73.png)

#### 11. 使用输入法

打开一个文档或者记事本, 使用快捷键[Ctrl + 空格] 或 [Shift] 切换到搜狗输入法, 就可以使用啦!

**补充:** 如果按了快捷键似乎没有反应, 依旧是英文输入法, 那么r可以尝试**重启**或者在右上角的输入法中**手动切换**一下看看
![在这里插入图片描述](./ubuntu安装搜狗输入法/c4f4ccff341c0710db6f0e9cb4f77349.png)