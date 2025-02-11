# Ubuntu安装卸载tex

## LaTeX安装

### 1.1 镜像文件下载

进入 Texlive [清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/)，下载 texlive2023.iso；

~~~
sudo mount -o loop texlive2023.iso /mnt/iso
~~~



### 1.2 安装步骤

下载完成后双击 .iso 镜像文件进行挂载，挂载后终端进入 .iso 目录执行如下命令进行安装

```
sudo perl ./install-tl --no-interaction
```

等待安装完成，相关安装路径为

```
/usr/local/texlive/YYYY/bin/PLATFORM
e.g., /usr/local/texlive/2023/bin/x86_64-linux
```

在安装命令的终端输出结尾会输出如下路径

```
Add /usr/local/texlive/2024/texmf-dist/doc/man to MANPATH.
Add /usr/local/texlive/2024/texmf-dist/doc/info to INFOPATH.
Most importantly, add /usr/local/texlive/2024/bin/x86_64-linux
to your PATH for current and future sessions.
```

进一步将 texlive 添加到环境变量中

```
sudo vim ~/.bashrc
```

在 .bashrc 文件的末尾添加如下代码

```
export PATH=/usr/local/texlive/2024/bin/x86_64-linux:$PATH
export MANPATH=/usr/local/texlive/2024/texmf-dist/doc/man:$PATH
export INFOPATH=/usr/local/texlive/2024/texmf-dist/doc/info:$PATH
```

完成环境变量的添加后重新加载 .bashrc 文件

```
source ~/.bashrc
```

完成上述步骤后，进行设备重启

```
sudo reboot
```

### 1.3 查看是否安装成功

打开终端命令行键入如下命令

```
tex --version
```

终端返回输出：

```
TeX 3.141592653 (TeX Live 2024)
kpathsea version 6.4.0
Copyright 2024 D.E. Knuth.
There is NO warranty.  Redistribution of this software is
covered by the terms of both the TeX copyright and
the Lesser GNU General Public License.
For more information about these matters, see the file
named COPYING and the TeX source.
Primary author of TeX: D.E. Knuth.
```

至此， texlive 的安装完成。

### 1.4 相关依赖安装

打开新的终端，键入如下命令下载相关依赖支持

```
sudo apt-get install texlive-latex-extra -y
sudo apt-get install texlive-latex-recommended -y
sudo apt-get install texlive-science -y
```

## 2 安装 windows 字体

首先在 windows 下进入 C 盘下的 C:/windows/Fonts 下将需要的字体拷贝出来，放到新建的文件夹中

下一步将拷贝出来的字体文件通过 U 盘拷贝至 Ubuntu 下

在 Ubuntu 的计算机存储下新建目录用于存储字体

```
sudo mkdir /usr/share/fonts/winfonts
```

将 windows 系统下的字体拷贝到刚刚创建的 winfonts 目录下

```
sudo chmod 644 /usr/share/fonts/winfonts/*
```

刷新缓存字体

```
sudo mkfontscale
sudo mkfontdir
sudo fc-cache -fsv
```

查看系统中安装的中文字体

```
fc-list :lang=zh | sort
```

## LaTeX卸载

```bash
sudo apt-get purge texlive*
rm -rf /usr/local/texlive and rm -rf ~/.texlive*
rm -rf /usr/local/share/texmf
rm -rf /var/lib/texmf
rm -rf /etc/texmf
sudo apt-get remove tex-common --purge
rm -rf ~/.texlive*
```

## 背景介绍

[Pandoc](https://pandoc.org/) 可以很方便地对不同 Markup 语言的文件进行格式转换，因此被誉为格式转换的「瑞士军刀」。使用 Pandoc 把 Markdown 文件转为 PDF 文件，实际上包含两个步骤：

- 第一步， Markdown 文件被转为 LaTeX 源文件。
- 第二步，调用系统的 `pdflatex`, `xelatex` 或者其他 TeX 命令，将 `.tex` 文件转换为最终的 PDF 文件 。

Pandoc 默认使用的 `pdflatex` 命令无法处理 Unicode 字符，如果要把包含中文的Markdown 文件转为 PDF，在生成 PDF 的过程中会报错。我们需要使用 `xelatex` 来处理中文，并且需要使用 `mainfont` 选项指定支持中文的字体。

```
pandoc --pdf-engine=xelatex -V mainfont="XXX" test.md -o test.pdf
```

## 安装和查看本机上的中文字体

安装字体

```
apt-get install fontconfig xfonts-utils # 安装fc-cache
apt-get install ttf-mscorefonts-installer # 微软的TrueType 核心字库
apt-get install ttf-wqy-microhei  #文泉驿-微米黑
apt-get install ttf-wqy-zenhei  #文泉驿-正黑
apt-get install xfonts-wqy #文泉驿-点阵宋体
```

我是debian环境，字体位置，`/usr/share/fonts`

```
fc-list :lang=zh
```

## 转换pdf常用参数

- –latex-engine=pdflatex/lualatex/xelatex

–latex-engine用来指定转换PDF格式时LaTeX引擎，默认情况下是pdflatex，但是由于pdflatex不支持中文，因此需要将引擎设置为xelatex

- –template=FILE

使用FILE指定的文件作为输出文档的自定义模板。可将模板文件放置任意处，只是指定FILE时需要该FILE的路径。

- –toc, –table-of-contents

使用该参数后，会在输出文档开头自动产生文件目录，对于输出格式是man, docbook, slidy, slideous, s5, docx 或者odt的文档，该参数不起任何作用。

- –toc-depth=NUMBER

指定文件目录中包含的章节级别，默认NUMBER=3，表示一级标题、二级标题、三级标题都会被在目录中展示。

- -V KEY[=VAL], –variable=KEY[:VAL]

当渲染standalone模式下文档时，设置模板变量KEY的值为VAL。pandoc会自动设置默认模板中的这些变量，因此该选项这通常在使用–template选项指定自定义模板时有用，如果没有指定VAL值，那么该KEY会被赋予值true。

- -s, –standalone

转换输出文档时会自动加上合适的header和footer(例如standalone HTML, LaTeX, RTF).该选择在转换输出pdf，epub，epub3，fb2，docx，odt格式文件时会被自动设置，因此如果转换输出上述格式文件，则不用显示指定该选项。

- -N, –number-sections

对于转换输出LaTeX, ConTeXt, HTML, EPUB格式文档时，对文中章节进行编号。默认情况下，文章的章节是不会被编号的。对于使用了class unnumbered 的章节肯定不会被标号，即使使用了–number-sections选项。

## 命令备忘

```
pandoc --pdf-engine=xelatex -V mainfont='WenQuanYi Zen Hei Mono' 1.md --template pm -o 2.pdf
```

我用了[这个模版](https://github.com/tzengyuxio/pages/tree/gh-pages/pandoc)，对中文比较友好，将 [pm-template.latex](https://github.com/tzengyuxio/pages/blob/gh-pages/pandoc/pm-template.latex) 文件拷贝到 `/usr/share/pandoc/data/templates`后直接使用。

> 这个模版需要做些调整，将字体设置的地方`LiHei Pro`，改为我本机存在的字体`WenQuanYi Zen Hei Mono`。
>
> 遇到个问题，中文无法换行。最后直接用这个模版解决了。

还有另一个模版[Eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template.git)也比较常用的。



~~~
pandoc --pdf-engine=xelatex -V mainfont='新宋体' 1.md --template my_template -o 2.pdf
pandoc --pdf-engine=xelatex --template my_template --toc 1.md -o 2.pdf 
~~~



~~~
cd /home/luo/Project/
cd  /usr/share/pandoc/data/templates
~~~

