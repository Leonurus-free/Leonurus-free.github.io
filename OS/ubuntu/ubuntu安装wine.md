# ubuntu安装wine

Wine（Wine Is Not an Emulator）是一个广受欢迎的兼容层，允许 Linux 用户在其系统上原生运行 Windows 应用程序。无论是为了游戏、生产力软件还是单纯为了方便，Wine 提供了一种无需完整虚拟机或双系统设置就能运行 Windows 程序的解决方案。本指南将引导您完成在 Ubuntu 22.04 上安装 Wine 的步骤，确保您能够无缝运行所需的 Windows 应用程序。我们还将在常见问题解答部分涵盖常见问题。

## 前提条件

在开始之前，请确保您具备以下条件：

- 运行 Ubuntu 22.04（Jammy Jellyfish）的机器
- 管理员（root）权限
- 用于下载软件包的互联网连接

## 教程步骤

### 步骤 1：更新系统的软件包列表

首先，更新软件包列表以确保您的软件源是最新的：

```
sudo apt update
```

这确保将安装所有最新可用的软件包和依赖项。

### 步骤 2：启用 32 位架构支持

Wine 在 64 位系统上需要 32 位架构支持，这在现代计算机上很常见。您可以使用以下命令启用它：

```
sudo dpkg --add-architecture i386
```

此命令告诉您的系统准备安装 32 位软件包。

### 步骤 3：添加 WineHQ 软件源

要安装最新版本的 Wine，您需要将官方 WineHQ 软件源添加到您的系统中。

#### 3.1. 添加 WineHQ 密钥：

下载并添加 WineHQ 密钥，以便您的系统信任该软件源：

```
sudo mkdir -pm755 /etc/apt/keyrings
sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key
```

#### 3.2. 添加 WineHQ 软件源：

现在，添加对应于 Ubuntu 22.04（Jammy）的软件源：

```
sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/jammy/winehq-jammy.sources
```

### 步骤 4：安装 Wine

添加软件源后，再次更新系统的软件包列表并安装 Wine。使用以下命令：

```
sudo apt update
sudo apt install --install-recommends winehq-stable
```

--install-recommends 标志确保安装所有推荐的 Wine 软件包，提供更流畅的体验。

### 步骤 5：验证安装

安装完成后，您可以通过输入以下命令来验证 Wine 是否成功安装以及运行的是哪个版本：

```
wine --version
```

此命令将输出已安装的 Wine 版本。

### 步骤 6：配置 Wine

在运行任何 Windows 应用程序之前，最好首次配置 Wine。这个设置过程会安装必要的组件，如 Mono（用于 .NET 应用程序）和 Gecko（用于 HTML 渲染）。要执行此操作，请运行：

```
winecfg
```

这将打开 Wine 配置窗口，您可以在其中设置 Wine 应模拟的 Windows 版本（对于大多数应用程序，建议使用 Windows 10）。

## 可选步骤：安装 Winetricks

Winetricks 是一个辅助脚本，可简化各种 Windows 库和运行时组件（如 DirectX、.NET）的安装。它对需要额外依赖项的特定软件特别有用。

要安装 Winetricks，请运行：

```
sudo apt install winetricks
```

安装后，您可以使用 Winetricks 安装某些 Windows 应用程序可能需要的额外软件。

## 常见问题解答

1. Wine 是什么，为什么我应该使用它？ Wine 是一个兼容层，使用户能够在 Linux 上运行 Windows 应用程序。对于那些需要运行特定 Windows 软件但不想设置双系统或虚拟机的人来说，它是理想的选择。
2. 我需要 32 位系统才能使用 Wine 吗？ 不需要，但 64 位系统仍需支持 32 位架构，因为许多 Windows 应用程序是为 32 位系统设计的。Wine 可以处理 32 位和 64 位应用程序，但您需要在 64 位系统上启用 32 位架构以实现完全兼容。
3. WineHQ 稳定版、开发版和暂存版之间有什么区别？ 稳定版：经过最多测试的版本，推荐给大多数用户。它优先考虑稳定性而非新功能。 开发版：更前沿的版本，包含最新更新，但可能不太稳定。 暂存版：包含稳定版或开发版中没有的实验性功能。它对测试特定程序有用，但可能不太可靠。
4. Wine 能运行所有 Windows 程序吗？ 并非所有程序都保证能与 Wine 一起工作，特别是非常新或图形密集型的软件。然而，许多流行的应用程序，包括 Microsoft Office 和一些游戏，都能很好地运行。您可以查看 Wine 的应用程序数据库（WineHQ AppDB）来了解特定软件的兼容性。
5. 如果我不再需要 Wine，如何卸载它？ 如果您决定移除 Wine，可以使用以下命令卸载它：

```
sudo apt remove --purge winehq-stable wine-stable wine-stable-i386 wine-stable-amd64
sudo apt autoremove
```

1. 如果在使用 Wine 运行 Windows 应用程序时遇到问题，我该怎么办？

如果应用程序运行不如预期，请查看 WineHQ AppDB 以获取特定的调整或解决方法。您还可以使用 winetricks 安装程序可能需要的额外库，如 .NET 或 DirectX。

## 结论

Wine 是一个强大的工具，允许 Linux 用户通过在其 Ubuntu 系统上运行 Windows 应用程序来享受两个世界的好处。通过遵循本指南，您将能够在 Ubuntu 22.04 上安装 Wine 并运行您喜爱的 Windows 软件。对于更高级的配置和故障排除，请探索 Wine 的文档或查阅 WineHQ AppDB 以获取特定应用程序指南。享受您的新软件自由！