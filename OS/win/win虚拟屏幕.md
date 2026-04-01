# win虚拟屏幕

### 未连接显示器时在 Windows 10 上激活辅助显示器

在没有物理显示器的情况下，通过远程软件向日葵或者todesk连接主机，默认显示640*640分辨率，而且无法修改，网上存在一些付费版虚拟显示器软件，今天再次推荐一种简单免费的方法。

### 下载

软件下载
[usbmmidd_v2.zip](https://www.amyuni.com/downloads/usbmmidd_v2.zip)

### 使用方法

下载软件包后解压，通过管理员身份打开命令提示符，然后依次输入以下命令:

```bash
cd c:\temp\usbmmid_v2 (解压的目录)
deviceinstaller64 install usbmmidd.inf usbmmidd
deviceinstaller64 enableidd 1
```

如果是在Windows 10中添加4个虚拟显示器，最多可以运行最后一条命令4次。

如果你使用的是32位系统，将"deviceinstaller64"替换为"deviceinstaller"

包含的批处理文件usbmmid.bat会自动运行这些命令，并在32位或64位版本的设备安装程序之间进行选择。

如果您不习惯打开命令提示符并输入这些命令，右键单击usbmmid.bat和“以管理员身份运行”。

要停用虚拟监视器，请运行以下命令：

```undefined
deviceinstaller64 enableidd 0
```

（如果添加了多个虚拟显示器，请多次运行此命令）

重新激活它：

```undefined
deviceinstaller64 enableidd 1
```

要从系统中完全删除驱动程序，您可以通过设备管理器并卸载“USB Mobile Monitor Virtual Display”，或运行以下命令：

```csharp
deviceinstaller64 stop usbmmidd
deviceinstaller64 remove usbmmid 
```

