# python离线下载安装

官方下载地址

~~~
https://pypi.org/
~~~

使用已有环境下载

~~~
pip download openpyxl==3.1.5 -d ./aa
~~~

会将所有依赖包都下载到文件夹aa中，在安装的时候直接输入
~~~
pip install ./aa
~~~

即可。



## ✅ 一、如果项目有 `requirements.txt`

### 1️⃣ 在可联网环境中下载所有依赖

```
pip download -r requirements.txt -d packages
```

说明：

- `-d packages`：把所有包（含依赖）下载到 `packages/` 目录
- 会同时下载 `.whl` 和 `.tar.gz`

------

### 2️⃣ 拷贝 `packages/` 到离线服务器

------

### 3️⃣ 在离线环境中安装

```
pip install --no-index --find-links=packages -r requirements.txt
```

------

## ✅ 二、如果没有 requirements.txt（只要当前环境依赖）

### 1️⃣ 导出依赖

```
pip freeze > requirements.txt
```

------

### 2️⃣ 下载

```
pip download -r requirements.txt -d packages
```

------

### 3️⃣ 离线安装

```
pip install --no-index --find-links=packages -r requirements.txt
```

------

## ✅ 三、使用 pip 本地缓存（无需显式 download）

联网机器先安装一遍：

```
pip install -r requirements.txt
```

找到缓存目录：

```
pip cache dir
```

把缓存目录（通常是 `~/.cache/pip` 或 `%LOCALAPPDATA%\pip\Cache`）拷贝走
在离线环境：

```
pip install --no-index --find-links=/path/to/cache -r requirements.txt
```

------

## ⚠️ 常见坑

1️⃣ 离线机器 Python 版本必须一致（最好也一致的 OS 架构）
2️⃣ 有些包需要编译（如 `cryptography`, `lxml`, `torch`），尽量下载 **whl 文件**
3️⃣ Windows ↔ Linux 的包不能通用
4️⃣ conda 环境建议用 `conda pack` 或 `conda env export`