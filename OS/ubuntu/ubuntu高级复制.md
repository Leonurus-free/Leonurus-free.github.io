# ubuntu中高级复制

在 Ubuntu（Linux）中，你可以用多种方式实现“复制文件夹但排除部分文件/子文件夹”。常见且推荐的方式有两种：

------

### ✅ **方法 1：使用 `rsync`（推荐）**

`rsync` 是最灵活、最常用的工具，支持排除规则、断点续传等。

#### 基本语法：

```
rsync -av --exclude='排除规则' 源目录/ 目标目录/
```

#### 示例 1：排除单个文件夹

```
rsync -av --exclude='node_modules' /path/to/A/ /path/to/B/
```

#### 示例 2：排除多个文件或目录

```
rsync -av \
  --exclude='node_modules' \
  --exclude='.git' \
  --exclude='*.log' \
  /path/to/A/ /path/to/B/
```

#### 示例 3：使用排除列表文件

如果排除项很多，可以写进一个文件：

```
# exclude.txt
node_modules
.git
*.log
tmp/
```

然后执行：

```
rsync -av --exclude-from='exclude.txt' /path/to/A/ /path/to/B/
```

#### 参数说明：

- `-a` ：归档模式（保留权限、时间、符号链接等）
- `-v` ：显示详细过程
- `--exclude`：指定要排除的匹配模式
- 目录后面的 `/` 表示复制目录内容而不是目录本身（这一点很关键）

------

### ✅ **方法 2：使用 `cp` + `--exclude`（GNU cp 特性）**

部分 Linux 发行版（如 Ubuntu 22.04+）支持 `--exclude` 参数，但**兼容性不如 rsync**。

```
cp -r --verbose --exclude='node_modules' /path/to/A /path/to/B
```

👉 注意：不是所有版本的 `cp` 都支持 `--exclude`。可以先执行：

```
cp --help | grep exclude
```

如果有说明行，才可以用。

------

### ✅ **方法 3：使用 `tar` 管道复制（较高级）**

如果你希望在不借助 `rsync` 的前提下复制并排除文件，也可以用 `tar`：

```
tar --exclude='node_modules' -cf - -C /path/to/A . | tar -xf - -C /path/to/B
```

这条命令的意思是：

- 从 `/path/to/A` 打包（排除 node_modules），但不写入文件；
- 用管道传输到另一个 `tar` 命令，在 `/path/to/B` 解包。

------

### 🚀 推荐总结：

| 方法    | 命令                      | 优点                       |
| ------- | ------------------------- | -------------------------- |
| ✅ rsync | `rsync -av --exclude=...` | 最方便、最安全、最推荐     |
| cp      | `cp -r --exclude=...`     | 简单，但不一定可用         |
| tar     | `tar --exclude=...`       | 无需额外安装，但语法稍复杂 |



------

~~~
rm -rf /home/frontend_project/cl_luo_front && rsync -av --exclude-from='./cl_luo_front/exclude.txt' ./cl_luo_front /home/frontend_project
~~~

~~~
rm -rf /home/pythonProject/cl_luo_backend && rsync -av --exclude-from='./cl_luo_backend/exclude.txt' ./cl_luo_backend /home/pythonProject
~~~

