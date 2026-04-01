# Windows 端口被系统占用解决方法

## 问题现象

运行 Docker 容器或其他程序时报错：

```
(HTTP code 500) server error - ports are not available: exposing port TCP 0.0.0.0:9091 -> 127.0.0.1:0: listen tcp 0.0.0.0:9091: bind: An attempt was made to access a socket in a way forbidden by its access permissions.
```

## 根本原因

Windows（开启了 Hyper-V 或 WSL2 的系统）在每次启动时会**随机**预留若干段端口范围（每段约 100 个端口）供系统内核独占使用。若目标端口恰好落入保留区间，任何普通程序试图绑定该端口都会被以"权限不足"为由直接拒绝。

这就是为什么**之前能用，重启后突然不行**——系统每次启动随机抽号，这次恰好抽中了你的端口。

## 诊断步骤

### 第一步：查看系统保留端口范围

以管理员身份打开 PowerShell，运行：

```powershell
netsh interface ipv4 show excludedportrange protocol=tcp
```

示例输出：

```
协议 tcp 端口排除范围

开始端口    结束端口
----------    --------
      1239        1338
      1339        1438
      8987        9086
      9087        9186   ← 9091 落在此区间内！
     13053       13152
     50000       50059     *

* - 管理的端口排除。
```

若目标端口落在任意区间内，即为被系统占用。

### 第二步：确认端口是否被进程占用

```cmd
netstat -ano | findstr :9091
```

- **有输出**：端口被某进程占用，找到 PID 后用 `taskkill /F /PID <PID>` 结束进程。
- **无输出**：端口未被进程占用，但被系统内核保留（即上述情况）。

## 解决方案

### 方案一：更换端口（最简单）

观察排除范围列表，选一个不在区间内的端口，例如 `9200`、`10000` 等。

Docker 示例：

```bash
docker run -p 9200:9091 ...
```

### 方案二：重启 WinNat 服务（临时恢复）

重启 WinNat 会重置随机保留的端口范围，有机会让目标端口重新可用。

```powershell
# 管理员 PowerShell
net stop winnat
# 立刻启动你的程序/容器，抢占端口
net start winnat
```

> 注意：下次重启系统后可能再次被随机占用。

### 方案三：永久锁定端口（推荐）

将目标端口加入"用户指定排除"，阻止系统以后随机抢占：

```powershell
# 管理员 PowerShell
net stop winnat
netsh int ipv4 add excludedportrange protocol=tcp startport=9091 numberofports=1
net start winnat
```

验证是否添加成功（带 `*` 号的即为用户指定）：

```powershell
netsh interface ipv4 show excludedportrange protocol=tcp
```

### 方案四：重置网络协议栈

若以上方法无效，尝试完全重置网络堆栈（需重启）：

```cmd
netsh winsock reset
netsh int ip reset
```

执行后**必须重启电脑**。

## 补充说明

- Windows 的**快速启动**（Fast Startup）本质是休眠，不会重置端口分配。若想彻底重置，请选择"重启"而非"关机"。
- 开启 **Hyper-V** 或 **WSL2** 的系统更容易触发此问题，因为这些功能依赖 WinNat 动态管理端口。
- 受影响的常见程序：Docker Desktop、Node.js 开发服务器、各类代理工具。
