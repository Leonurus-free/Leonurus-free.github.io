# docker容器中restart启动区别

在 Docker 中，`--restart=always` 和 `--restart=unless-stopped` 都是用来控制容器在退出时是否自动重启的策略，但它们的触发条件有细微差别：

------

### **1. `--restart=always`**

- **行为**：无论容器以 **何种状态退出**（包括正常退出 `exit 0` 或手动停止 `docker stop`），Docker 都会无条件重启容器。
- **例外**：仅当 Docker 守护进程（`dockerd`）本身停止时，容器不会重启（需等待守护进程恢复后才会重启）。
- **典型场景**：需要确保容器 **永远运行**，即使人为手动停止后也希望自动恢复（例如关键服务）。

------

### **2. `--restart=unless-stopped`**

- **行为**：
  - 如果容器是 **手动停止**（通过 `docker stop` 或 `docker rm -f`），则 **不会自动重启**。
  - 其他情况（如进程崩溃、系统重启、`exit 非0` 等），Docker 会自动重启容器。
- **典型场景**：允许用户临时停止容器（如调试期间），但其他意外退出时自动恢复。

------

### **对比示例**

| 场景                        | `--restart=always` | `--restart=unless-stopped` |
| :-------------------------- | :----------------- | :------------------------- |
| 容器进程正常退出 (`exit 0`) | ✅ 重启             | ✅ 重启                     |
| 容器进程崩溃 (`exit 非0`)   | ✅ 重启             | ✅ 重启                     |
| 手动执行 `docker stop`      | ✅ 重启             | ❌ **不重启**               |
| Docker 守护进程重启         | ✅ 重启             | ✅ 重启                     |

------

### **如何设置？**

```
# always 策略
docker run -d --restart=always nginx

# unless-stopped 策略
docker run -d --restart=unless-stopped nginx
```

------

### **总结**

- 选择 `always`：适用于 **必须保持运行** 的服务，即使人为停止也不允许中断。
- 选择 `unless-stopped`：更灵活，允许人工干预停止后不再重启。