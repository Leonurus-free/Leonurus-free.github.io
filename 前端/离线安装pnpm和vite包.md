# 离线安装pnpm和vite包

离线安装全局的pnpm和vite包，需要提前下载这些包及其依赖的tarball文件，然后在没有网络连接的环境中进行安装。

下载：
npm pack pnpm
npm pack vite

安装：
npm install -g /path/to/pnpm-<version>.tgz
npm install -g /path/to/vite-<version>.tgz