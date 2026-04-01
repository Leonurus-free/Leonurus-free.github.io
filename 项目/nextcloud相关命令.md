# nextcloud相关命令

# 一、基础信息 & 状态

### 1️⃣ 查看 Nextcloud 状态

```
docker exec -u www-data app-server php occ status
```

### 2️⃣ 查看 Nextcloud 版本

```
docker exec -u www-data app-server php occ status --output=json
```

------

# 二、应用管理（非常常用）

### 3️⃣ 查看所有已安装应用

```
docker exec -u www-data app-server php occ app:list
```

### 4️⃣ 仅查看已启用应用

```
docker exec -u www-data app-server php occ app:list --enabled
```

### 5️⃣ 启用应用

```
docker exec -u www-data app-server php occ app:enable context_chat
```

### 6️⃣ 禁用应用

```
docker exec -u www-data app-server php occ app:disable context_chat
```

------

# 三、后台任务 / Cron

### 7️⃣ 查看后台任务模式

```
docker exec -u www-data app-server php occ config:system:get backgroundjobs_mode
```

> 正确值应为：`cron`

------

### 8️⃣ 手动执行一次后台任务（关键）

```
docker exec -u www-data app-server php occ cron

docker exec -u www-data app-server php -f /var/www/html/cron.php
```

------

### 9️⃣ 查看后台任务队列状态

```
docker exec -u www-data app-server php occ background:queue:status
```

### 1. 查看后台作业队列

```
docker exec -u www-data app-server php occ background-job:list
```

- 列出所有挂起的和正在执行的后台作业。

------

### 2. 手动执行 Cron 任务

```
docker exec -u www-data app-server php occ background:cron
```

- 强制触发 Cron 后台作业，可以立即处理队列。

------

### 3. 查看后台作业状态（执行历史）

```
docker exec -u www-data app-server php occ background-job:worker
```

- 启动一个后台作业 worker，处理队列中的任务。

------

# 四、Context Chat / AI 索引相关

### 🔟 查看 Context Chat 状态

```
docker exec -u www-data app-server php occ context_chat:stats
```

### 1️⃣1️⃣ 手动扫描并索引用户文件

```
docker exec -u www-data app-server php occ context_chat:scan admin
```

### 1️⃣2️⃣ 查看 Context Chat 后台任务

```
docker exec -u www-data app-server php occ background:queue:status | grep ContextChat
```

------

# 五、文件索引 / 修复

### 1️⃣3️⃣ 扫描所有用户文件

```
docker exec -u www-data app-server php occ files:scan --all
```

### 1️⃣4️⃣ 扫描指定用户

```
docker exec -u www-data app-server php occ files:scan admin
```

### 1️⃣5️⃣ 清理文件缓存

```
docker exec -u www-data app-server php occ files:cleanup
```

------

# 六、配置查看 / 修改

### 1️⃣6️⃣ 查看所有系统配置

```
docker exec -u www-data app-server php occ config:system:list
```

### 1️⃣7️⃣ 查看单个系统配置

```
docker exec -u www-data app-server php occ config:system:get trusted_domains
```

### 1️⃣8️⃣ 设置系统配置

```
docker exec -u www-data app-server php occ config:system:set trusted_domains 1 --value=example.com
```

------

# 七、用户管理

### 1️⃣9️⃣ 查看所有用户

```
docker exec -u www-data app-server php occ user:list
```

### 2️⃣0️⃣ 查看用户信息

```
docker exec -u www-data app-server php occ user:info admin
```

### 2️⃣1️⃣ 重置用户密码

```
docker exec -u www-data app-server php occ user:resetpassword admin
```

------

# 八、数据库 & 维护（排障常用）

### 2️⃣2️⃣ 数据库修复

```
docker exec -u www-data app-server php occ db:add-missing-indices
docker exec -u www-data app-server php occ db:add-missing-columns
```

------

### 2️⃣3️⃣ 维护模式

```
docker exec -u www-data app-server php occ maintenance:mode --on
docker exec -u www-data app-server php occ maintenance:mode --off
```

------

# 九、日志



**手动跑一次 cron**

~~~
docker exec -u www-data app-server php -f /var/www/html/cron.php
~~~



日志文件所在位置

~~~
/home/ubuntu/luo/.collaborative_editing/nextcloud/data
context_chat.log  nextcloud.log
~~~

context_chat_backend容器的日志。



分词模型下载：
~~~
HF_HOME=/home/ubuntu/luo/.collaborative_editing/context_chat_backend/model_files huggingface-cli download gpt2 config.json merges.txt tokenizer.json tokenizer_config.json vocab.json
~~~



使用linux系统自带的crontab执行任务

#### 宿主机是 Linux：

直接编辑 `crontab -e`，添加这两行：

```
# 每 5 分钟跑一次常规任务
*/5 * * * * docker exec -u www-data app-server php -f /var/www/html/cron.php
# 每 1 分钟跑一次 AI Worker (实现近乎即时的 AI 响应)
* * * * * docker exec -u www-data app-server php /var/www/html/occ background-job:worker --no-interaction
```

~~~
界面特点：屏幕底部有两行明显的菜单，显示类似 ^O WriteOut 和 ^X Exit。

按下 Ctrl + O（保存文件）。

屏幕会提示文件名，直接按 Enter 确认。

按下 Ctrl + X（退出编辑器）。

保存后的检查
当你成功退出编辑器后，终端应该会显示一行提示：

crontab: installing new crontab

你可以输入以下命令来确认你的任务是否真的保存成功了：

crontab -l
该命令会列出当前用户下所有生效的定时任务。
~~~



查看crontab 日志：

~~~
# Ubuntu/Debian 系统
grep CRON /var/log/syslog | tail -n 20
~~~



### 常见错误：数据库连接爆炸

查看指定任务数
~~~
ps aux | grep "background-job:worker" | grep -v grep | wc -l
~~~

杀死任务

~~~
ps aux | grep "background-job:worker" | grep -v grep | awk '{print $2}' | xargs kill -9
~~~



## 应用注册和取消注册

~~~
docker exec -u www-data ${NC_CONTAINER} php occ app_api:daemon:register --net nextcloud_network --set-default manual_external "Context Chat Backend External" manual-install http context_chat_backend http://nginx-server

docker exec -u www-data app-server php occ ai:exapp:unregister context_chat_backend
~~~

