# ubuntu添加源和删除源

### **一、添加软件源**

#### **方法 1：通过 `add-apt-repository` 命令（推荐）**

```
sudo add-apt-repository ppa:user/ppa-name  # 添加 PPA 源
sudo add-apt-repository 'deb [arch=amd64] https://example.com/ubuntu focal main'  # 添加第三方源
```

- **示例**（添加 Node.js 官方源）：

  ```
  curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
  ```

#### **方法 2：手动编辑 `/etc/apt/sources.list`**

```
sudo nano /etc/apt/sources.list
```

- 在文件末尾添加一行（格式如下）：

  ```
  deb [arch=amd64] https://example.com/ubuntu focal main
  ```

- 保存后更新软件列表：

  ```
  sudo apt update
  ```

#### **方法 3：在 `/etc/apt/sources.list.d/` 中添加单独文件**

```
sudo nano /etc/apt/sources.list.d/custom.list
```

- 写入源地址（格式同 `sources.list`），保存后运行 `sudo apt update`。

------

### **二、删除软件源**

#### **方法 1：删除 PPA 源**

```
sudo add-apt-repository --remove ppa:user/ppa-name  # 删除 PPA
sudo rm /etc/apt/sources.list.d/user-ppa-name-*.list  # 手动删除 PPA 文件
```

#### **方法 2：手动编辑或删除源文件**

- 删除 `/etc/apt/sources.list` 中的对应行，或直接删除 `/etc/apt/sources.list.d/` 下的相关文件：

  ```
  sudo rm /etc/apt/sources.list.d/custom.list
  ```

#### **方法 3：禁用源（不删除）**

在源文件的行首添加 `#` 注释，或使用以下命令：

```
sudo sed -i 's/^deb/#deb/' /etc/apt/sources.list.d/custom.list
```

------

### **三、后续操作**

- 更新软件列表（修改源后必须执行）：

  ```
  sudo apt update
  ```

- 如果遇到 GPG 密钥错误，需添加密钥：

  ```
  sudo apt-key add keyfile.asc  # 或通过 wget/curl 导入
  ```

------

### **注意事项**

1. **谨慎操作**：错误的源可能导致系统不稳定。
2. **版本匹配**：确保源中的发行版代号（如 `focal`、`jammy`）与你的 Ubuntu 版本一致。
3. **优先使用官方源**：第三方源可能存在兼容性问题。