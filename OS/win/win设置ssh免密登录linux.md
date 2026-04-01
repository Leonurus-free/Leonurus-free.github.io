# win设置ssh免密登录linux

## **使用 `ssh` 手动复制公钥（推荐✅）**

### **步骤 1. 生成 SSH 密钥**

在 **PowerShell** 里运行：

```powershell
ssh-keygen -t rsa -b 4096 -C "100.100" -f "$env:USERPROFILE\.ssh\id_rsa_100"
```

解释：

- `-t rsa` → 指定加密算法（RSA）

- `-b 4096` → 指定密钥长度 4096 位

- `-C "your_email@example.com"` → 注释信息（可随便写）

- `-f` → 指定生成的密钥文件路径和名字
  例如：

  ```
  C:\Users\你的用户名\.ssh\id_rsa_100
  C:\Users\你的用户名\.ssh\id_rsa_100.pub
  ```

- 会提示保存路径，直接回车，默认保存到：

  ```powershell
  C:\Users\你的用户名\.ssh\id_rsa
  ```

- 会提示设置密码，直接回车即可（无密码）。

- 生成后会有两个文件：

  - `id_rsa` → 私钥
  - `id_rsa.pub` → 公钥

------

### **步骤 2. 将公钥复制到远程服务器**

在 PowerShell 中运行：

```powershell
type $env:USERPROFILE\.ssh\id_rsa_100.pub | ssh ubuntu@192.168.100.100 "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```

解释：

- `type` → 读取公钥内容
- `ssh ubuntu@192.168.100.100` → 登录远程服务器
- `mkdir -p ~/.ssh` → 如果没有 `.ssh` 文件夹则创建
- `cat >> ~/.ssh/authorized_keys` → 将公钥追加到 `authorized_keys`
- `chmod 600 ~/.ssh/authorized_keys` → 设置权限

------

### **步骤 3. 测试免密登录**

```powershell
ssh ubuntu@192.168.100.100
```

如果不需要输入密码，说明免密成功 ✅



注意：

SSH 公钥认证非常严格，不仅要求：

- `~/.ssh` 目录权限为 **700**
- `~/.ssh/authorized_keys` 文件权限为 **600**

同时还要求：

- **用户主目录 `/home/ubuntu` 的权限不能过宽**

如果 `/home/ubuntu` 权限太宽（比如 777 或 755 有问题），SSH 会拒绝公钥认证。

------

## **解决方法**

### **1. 修复用户主目录权限**

在服务器上执行：

```bash

chmod 700 /home/ubuntu
```

或者更安全：

```bash

chmod 755 /home/ubuntu
```

然后确认权限：

```bash

ls -ld /home/ubuntu
```

输出应该类似：

```bash

drwxr-xr-x  3 ubuntu ubuntu 4096 Sep 1 08:00 /home/ubuntu
```

> 注意：**不要是 777**，否则 SSH 公钥会被拒绝。

------

### **2. 修复 `.ssh` 和 `authorized_keys` 权限**

```bash
chmod 700 /home/ubuntu/.ssh
chmod 600 /home/ubuntu/.ssh/authorized_keys
chown -R ubuntu:ubuntu /home/ubuntu/.ssh
```

------

### **3. 重启 SSH 服务**

```bash

sudo systemctl restart ssh
```

