# Docker容器与主机之间文件传递

## `docker cp`（最直接，适合临时拷贝）

### 1️⃣ 宿主机 → 容器

```
docker cp ./local_file.txt my_container:/app/local_file.txt
```

### 2️⃣ 容器 → 宿主机

```
docker cp my_container:/app/output.log ./output.log
```

📌 特点

- 不需要容器运行
- 不需要提前挂载目录
- **不适合长期同步**

✅ 适合：

- 拿日志
- 临时导出模型 / 数据文件
- 调试阶段

