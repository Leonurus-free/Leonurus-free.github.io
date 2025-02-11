# 解决Docker中Error response from daemon: unknown or invalid runtime name: nvidia的问题



在使用Docker运行基于NVIDIA容器的应用程序时，可能会遇到一个常见的错误：”Error response from daemon: unknown or invalid runtime name: nvidia”。这个错误通常表示Docker守护进程没有正确配置以识别NVIDIA容器运行时。以下是一种解决方案，可以帮助您解决这个问题。
首先，您需要确保已正确安装了NVIDIA容器运行时。可以使用以下命令在您的系统上安装它：

- 对于基于Debian的系统（如Ubuntu）：

  ```
  sudo apt-get install nvidia-container-runtime
  ```

- 对于基于RPM的系统（如CentOS）：

  ```
  sudo yum install nvidia-container-runtime
  ```

  安装完成后，您需要配置Docker守护进程以识别NVIDIA容器运行时。可以通过编辑Docker守护进程的配置文件来实现这一点。请按照以下步骤操作：

1. 打开终端并以root用户身份登录。

2. 导航到Docker守护进程的配置文件所在的目录。在大多数系统上，默认配置文件位于`/etc/docker/daemon.json`。如果没有该文件，请创建一个新文件。

3. 使用文本编辑器打开 daemon.json 文件。例如，您可以使用 vi 或 nano 编辑器：

   ```
   touch /etc/docker/daemon.json 
   sudo vi /etc/docker/daemon.json
   ```

4. 在打开的文件中，添加以下内容（如果文件已经是空的，可以直接将以下内容粘贴到文件中）：

   ```
   {
   	"runtimes": {
   		"nvidia": {
   			"path": "/usr/bin/nvidia-container-runtime",
   			"runtimeArgs": []
   		}
   	}
   }
   ```

5. 保存并关闭文件。在`vi`编辑器中，按下Esc键，然后输入`:wq`并按Enter键保存并退出。

6. 最后，重启Docker守护进程以使更改生效。在终端中运行以下命令：

   ```
   sudo systemctl restart docker
   ```

   完成这些步骤后，Docker应该能够识别NVIDIA容器运行时，并允许您运行基于NVIDIA容器的应用程序。请注意，如果您之前尝试运行过基于NVIDIA容器的应用程序而遇到该错误，您可能需要重新创建并重新拉取包含NVIDIA容器的Docker镜像。这样，您可以确保Docker使用已正确配置的NVIDIA容器运行时来运行这些容器。