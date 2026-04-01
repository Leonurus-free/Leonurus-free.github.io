# ubuntu查找指定进程并关闭

## 查找

在 Ubuntu 中，可以通过以下几种方法查找所有含有特定字符串（例如 `marker`）的进程。

### 方法 1: 使用 `ps` 和 `grep`

```
ps aux | grep marker
```

- 解释：

  - `ps aux` 列出所有正在运行的进程。
  - `grep marker` 筛选出包含 `marker` 的行。

- 注意：该命令也可能显示 

  ```
  grep marker
  ```

   自身的进程。如果不希望显示，可以使用以下更精确的命令：

  ```
  ps aux | grep marker | grep -v grep
  ```

### 方法 2: 使用 `pgrep`

```
bash


复制代码
pgrep -a marker
```

- 解释：
  - `pgrep` 根据名称搜索匹配的进程。
  - `-a` 参数会显示匹配的进程以及它们的完整命令行。

### 方法 3: 使用 `htop` 或 `top`（实时监控）

1. 安装 

   ```
   htop
   ```

   （如果未安装）：

   ```
   bash复制代码sudo apt update
   sudo apt install htop
   ```

2. 启动 

   ```
   htop
   ```

   ：

   ```
   bash
   
   
   复制代码
   htop
   ```

3. 按 

   ```
   F3
   ```

    搜索输入 

   ```
   marker
   ```

   - `htop` 界面会高亮显示所有包含 `marker` 的进程。

### 方法 4: 使用 `lsof` 检查文件关联

如果你想查找与某些文件或资源相关的进程，可以使用 `lsof`：

```
bash


复制代码
lsof | grep marker
```

- **解释**：`lsof` 列出当前打开的文件（包括进程使用的文件、网络连接等），并筛选出包含 `marker` 的项。

### 方法 5: 使用 `pidof`（精确匹配进程名）

如果 `marker` 是某个特定进程的名字：

```
bash


复制代码
pidof marker
```

- 返回 `marker` 进程的 PID（如果存在）。

## 关闭

在 Ubuntu 中，关闭所有包含特定字符串（如 `marker`）的进程，可以通过以下步骤实现。请务必小心，确保这些进程是可以安全关闭的。

------

### **方法 1: 使用 `pkill`**

`pkill` 是专门用于终止进程的命令。

```
bash


复制代码
pkill -f marker
```

- 解释：
  - `-f`：表示根据完整命令行匹配。
  - `marker`：要匹配的字符串。

**注意**：`pkill` 会直接杀掉所有包含 `marker` 的进程，无需手动确认。

------

### **方法 2: 使用 `ps` + `grep` + `kill`**

1. 查找包含 `marker` 的进程：

   ```
   bash
   
   
   复制代码
   ps aux | grep marker
   ```

2. 获取进程的 PID 并手动终止：

   ```
   bash
   
   
   复制代码
   kill -9 PID
   ```

   例如：

   ```
   bash
   
   
   复制代码
   kill -9 12345
   ```

3. 如果需要批量终止所有匹配的进程，可以结合 `awk`：

   ```
   bash
   
   
   复制代码
   ps aux | grep marker | grep -v grep | awk '{print $2}' | xargs kill -9
   ```

   - `awk '{print $2}'` 提取第二列（即 PID）。
   - `xargs kill -9` 批量杀死这些进程。

------

### **方法 3: 使用 `pgrep` + `kill`**

1. 使用 

   ```
   pgrep
   ```

    查找匹配的进程：

   ```
   bash
   
   
   复制代码
   pgrep -f marker
   ```

2. 批量终止所有匹配的进程：

   ```
   bash
   
   
   复制代码
   pgrep -f marker | xargs kill -9
   ```

------

### **方法 4: 结合 `htop`（交互式）**

1. 打开 

   ```
   htop
   ```

   ：

   ```
   bash
   
   
   复制代码
   htop
   ```

2. 按 `F3` 搜索 `marker`。

3. 找到相关进程后，用方向键选中它们。

4. 按 `F9`，然后选择 `SIGKILL`（默认选项为 9）。

------

### **注意事项**

1. **确保安全**：确认这些进程是可以安全终止的，特别是生产环境中，以免引起系统或服务问题。

2. 权限问题：某些进程可能需要超级用户权限才能关闭。使用 

   ```
   sudo
   ```

    提升权限：

   ```
   bash复制代码sudo pkill -f marker
   sudo ps aux | grep marker | awk '{print $2}' | xargs sudo kill -9
   ```

3. **检查状态**：终止后，可以重新执行查找命令，确认进程已关闭。

以上方法可以灵活选择，推荐使用 `pkill` 或 `pgrep` + `kill` 的方式，简单快捷。