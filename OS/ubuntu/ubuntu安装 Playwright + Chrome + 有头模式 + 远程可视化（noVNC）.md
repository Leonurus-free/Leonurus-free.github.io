# ubuntu**安装 Playwright + Chrome + 有头模式 + 远程可视化（noVNC）**

------

# ✅ 完整 Dockerfile（请直接使用）

```
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# -------------------------------
# 基础工具 + 桌面环境
# -------------------------------
RUN apt-get update && apt-get install -y \
    sudo \
    xvfb \
    x11vnc \
    xfce4 \
    xfce4-terminal \
    dbus-x11 \
    curl \
    git \
    wget \
    net-tools \
    supervisor \
    nano \
    && rm -rf /var/lib/apt/lists/*

# -------------------------------
# 安装 noVNC + Websockify
# -------------------------------
RUN mkdir -p /opt/novnc \
    && git clone https://github.com/novnc/noVNC.git /opt/novnc \
    && git clone https://github.com/novnc/websockify.git /opt/novnc/utils/websockify \
    && ln -s /opt/novnc/vnc.html /opt/novnc/index.html

# -------------------------------
# 安装 Node.js + Playwright Chromium（带 GUI）
# -------------------------------
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g playwright \
    && playwright install chromium \
    && playwright install-deps

# -------------------------------
# Supervisor 配置启动所有服务
# -------------------------------
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# -------------------------------
# 创建启动脚本
# -------------------------------
COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 5900 6080

CMD ["/start.sh"]
```

------

# ✅ supervisord.conf（请与 Dockerfile 同目录）

```
[supervisord]
nodaemon=true

[program:xvfb]
command=/usr/bin/Xvfb :1 -screen 0 1920x1080x24
autorestart=true

[program:dbus]
command=/usr/bin/dbus-daemon --system
autorestart=true

[program:xfce4]
environment=DISPLAY=":1"
command=/usr/bin/startxfce4
autorestart=true

[program:x11vnc]
command=/usr/bin/x11vnc -display :1 -nopw -forever
autorestart=true

[program:novnc]
command=/opt/novnc/utils/novnc_proxy --vnc localhost:5900 --listen 6080
autorestart=true
```

------

# ✅ start.sh（请与 Dockerfile 同目录）

```
#!/bin/bash
export DISPLAY=:1

# 设置 VNC 目录
mkdir -p ~/.vnc

# 启动 supervisor
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
```

------

# ✅ 构建并运行容器

```
docker build -t playwright-desktop .
docker run -it --rm -p 6080:6080 -p 5900:5900 playwright-desktop
```

------

# 💯 启动后你可以访问：

### 🌐 Web VNC（推荐）

```
http://localhost:6080
```

### 🖥 VNC 客户端连接

```
localhost:5900
```

------

# 🎉 你现在可以：

- 打开终端
- 运行 Playwright
- Chromium 有头运行
- 能看到窗口
- 能测试所有 GUI 自动化

例如：

```
playwright codegen https://www.baidu.com
```

将直接在 XFCE 桌面弹出浏览器。



# 在已经运行的容器中安装Playwright + Chrome + 有头模式 + 远程可视化（noVNC）

# ✅ **一、确认你当前容器环境**

进入你的现有容器：

```
docker exec -it <container_name> bash
```

确认容器里是 **Ubuntu**，并且你有 root 权限。

------

# ✅ 二、安装基础依赖（必须）

Playwright 的 GUI 模式需要大量依赖：

```
apt-get update
apt-get install -y \
    wget curl unzip git \
    xvfb x11vnc \
    supervisor \
    net-tools \
    xfce4 xfce4-terminal \
    dbus-x11 \
    libnss3 libatk1.0-0 libcups2 \
    libxss1 libxrandr2 libasound2 \
    libatk-bridge2.0-0 libgtk-3-0
```

------

# ✅ 三、安装 noVNC + websockify（远程查看 GUI）

```
mkdir -p /opt/novnc
cd /opt/novnc
git clone https://github.com/novnc/noVNC .
git clone https://github.com/novnc/websockify
ln -s vnc_lite.html index.html
```

------

# ✅ 四、安装 Playwright（含 Chrome）

如果是 Python：

```
pip install playwright
playwright install chromium
```

如果你要安装所有浏览器：

```
playwright install
```

------

# ⭐ **学习重点：Playwright 的浏览器和 system Chrome 不冲突，它自带 Chromium！**

所以你不需要自己安装 Google Chrome。

------

# ✅ 五、设置 VNC server（x11vnc）

我们要让 Playwright 的 headful 浏览器可视化展示：

```
mkdir -p /root/.vnc
x11vnc -storepasswd 123456 /root/.vnc/passwd
```

------

# ✅ 六、`/start-desktop.sh` 完整版本

```
#!/bin/bash
set -e

# =========================================================
# 用户可自定义参数
export DISPLAY=:1
SCREEN_RESOLUTION="1920x1080x24"
VNC_PORT=${VNC_PORT:-7005}
NOVNC_PORT=${NOVNC_PORT:-7004}
VNC_PASSWORD=${VNC_PASSWORD:-"7ujm8ik,9ol."}  # 默认密码

# =========================================================
echo "[INFO] Setting up VNC password ..."
mkdir -p /root/.vnc
x11vnc -storepasswd "$VNC_PASSWORD" /root/.vnc/passwd

# =========================================================
echo "[INFO] Starting Xvfb on display $DISPLAY ..."
Xvfb $DISPLAY -screen 0 $SCREEN_RESOLUTION &
XVFB_PID=$!
sleep 2

# =========================================================
echo "[INFO] Starting D-Bus (needed by XFCE) ..."
eval "$(dbus-launch --sh-syntax)"
export DBUS_SESSION_BUS_ADDRESS
export DBUS_SESSION_BUS_PID
sleep 1

# 创建 XFCE 配置目录，防止报错
mkdir -p ~/.config/xfce4

# =========================================================
echo "[INFO] Starting XFCE desktop ..."
xfsettingsd &
startxfce4 &
sleep 3

# =========================================================
echo "[INFO] Starting x11vnc ..."
x11vnc -display $DISPLAY -rfbport $VNC_PORT -rfbauth /root/.vnc/passwd -forever -shared -bg -o /tmp/x11vnc.log
sleep 2

# =========================================================
echo "[INFO] Starting noVNC web interface ..."
cd /opt/novnc
# clone websockify if not exist
if [ ! -d "./utils/websockify" ]; then
    echo "[INFO] Cloning websockify ..."
    git clone https://github.com/novnc/websockify utils/websockify
fi

# 启动 noVNC，不加 --passwdfile
./utils/novnc_proxy --vnc localhost:$VNC_PORT --listen $NOVNC_PORT &

# =========================================================
echo ""
echo "*************************************************************"
echo "✅ Desktop environment is ready!"
echo "VNC port      : $VNC_PORT"
echo "noVNC web URL : http://localhost:$NOVNC_PORT/vnc.html"
echo ""
echo "You can now run Playwright GUI with:"
echo "  DISPLAY=$DISPLAY playwright codegen <URL>"
echo "*************************************************************"

# =========================================================
wait

```

------

## 使用方法

1. 保存为 `/start-desktop.sh`

```
chmod +x /start-desktop.sh
```

1. 运行容器时映射端口：

```
docker run -it -p 6080:6080 -p 5900:5900 <your-container> bash
```

1. 启动桌面：

```
./start-desktop.sh
```

1. 浏览器访问 noVNC：

```
http://localhost:6080/vnc.html
```

1. 在容器终端运行 Playwright GUI：

```
export DISPLAY=:1
playwright codegen https://www.baidu.com
```

或用 Python 脚本打开 Chromium：

```
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.baidu.com")
    page.screenshot(path="test.png")
    browser.close()
```

------

