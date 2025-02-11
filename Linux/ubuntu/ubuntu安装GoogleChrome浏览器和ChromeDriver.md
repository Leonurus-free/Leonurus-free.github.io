# ubuntu安装Google Chrome 浏览器和ChromeDriver

要在Ubuntu上安装Google Chrome浏览器和ChromeDriver，可以按照以下步骤操作：

#### 1. 安装Google Chrome 浏览器

1. 下载Google Chrome 的最新版本。

   ```bash
   wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
   ```

2. 使用`dpkg`安装下载的deb包。

   ```bash
   sudo dpkg -i google-chrome-stable_current_amd64.deb
   ```

3. 如果在安装过程中遇到了依赖问题，您可以使用下面的命令来自动修复它。

   ```bash
   sudo apt-get install -f
   ```

此时，可以在Ubuntu中找到Google [Chrome浏览器](https://so.csdn.net/so/search?q=Chrome浏览器&spm=1001.2101.3001.7020)，并运行它。

#### 2. 安装ChromeDriver

1. 首先，需要查看您已经安装的Chrome浏览器的版本。

   ```bash
   google-chrome --version
   ```

2. 记下显示的版本号，然后去 https://googlechromelabs.github.io/chrome-for-testing/ 找到与您的Chrome浏览器版本匹配的ChromeDriver版本。

3. 下载对应的ChromeDriver版本。例如，如果您的Chrome版本是90.0.4430.24，则应该下载该版本的ChromeDriver。

   ```bash
   wget https://chromedriver.storage.googleapis.com/<version>/chromedriver_linux64.zip
   ```

   其中 `<version>` 需要替换为您查到的版本号。

4. 解压下载的文件。

   ```bash
   unzip chromedriver_linux64.zip
   ```

5. 移动解压后的 `chromedriver` 到`/usr/bin/`或其他在PATH[环境变量](https://so.csdn.net/so/search?q=环境变量&spm=1001.2101.3001.7020)中的目录，以便可以全局访问。

   ```bash
   sudo mv chromedriver /usr/bin/
   ```

6. 为`chromedriver`赋予可执行权限。

   ```bash
   sudo chmod +x /usr/bin/chromedriver
   ```

现在，已经成功地在Ubuntu上安装了Google Chrome和ChromeDriver。可以使用命令`google-chrome`来启动浏览器，并使用命令`chromedriver`来启动ChromeDriver。

chromedriver --version

