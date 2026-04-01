针对单机 all 模式，以下是系统性的并发会话测试方案：

---
##   一、测试前准备

  确认当前资源基线

~~~
# 查看总内存和 CPU
free -h
nproc
~~~

~~~
# 查看当前容器资源占用（基础服务本身的开销）
docker stats --no-stream $(docker ps --format "{{.Names}}" | grep kasm)
~~~

~~~
# 查看磁盘剩余
df -h /var/lib/docker
~~~

~~~
# 确认 swap 已启用
swapon --show
~~~
### 如果没有输出说明没有 swap，建议创建

---
#  二、手动逐步并发测试（最直接）

##  步骤1：登录管理员界面

  访问 https://<your-ip>/ 使用 admin@kasm.local 登录

##   步骤2：开启多个浏览器标签页，逐步创建会话

  每创建一个新会话后，记录以下数据：

~~~
# 在服务器上持续监控（每2秒刷新）
watch -n 2 '
echo "=== 内存 ==="
free -h
echo ""
echo "=== 容器资源 ==="
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}" | grep kasm
echo ""
echo "=== 活跃会话数 ==="
docker ps | grep -v kasm_db | grep -v kasm_api | grep -v kasm_proxy | grep -v kasm_manager | grep -v kasm_guac |
wc -l
'
~~~



##   步骤3：记录每个并发数的指标

  ┌────────────┬──────┬──────────┬──────────┐
  │ 并发会话数 │ CPU% │ 内存使用 │ 延迟感受 │
  ├────────────┼──────┼──────────┼──────────┤
  │ 1                 │           │                │                            │
  ├────────────┼──────┼──────────┼──────────┤
  │ 5                 │          │                 │                            │
  ├────────────┼──────┼──────────┼──────────┤
  │ 10              │           │                 │                            │
  ├────────────┼──────┼──────────┼──────────┤
  │ ...               │           │                 │                            │
  └────────────┴──────┴──────────┴──────────┘

---
#   三、用脚本自动创建多个会话（API 方式）

  Kasm 提供 REST API，可以用脚本批量创建会话：

##   步骤1：获取 API 凭据

  ~~~
  # 先获取 API Token（替换密码）
  KASM_API_URL="https://localhost"
  ADMIN_PASS="HL6GxKWoixkS5"
  
  TOKEN=$(curl -sk -X POST "${KASM_API_URL}/api/public/request_extended_api_token" \
      -H "Content-Type: application/json" \
      -d '{
        "username": "admin@kasm.local",
        "password": "'"${ADMIN_PASS}"'",
        "token": ""
      }' | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('token',''))")
  
  echo "Token: $TOKEN"
  ~~~



##   步骤2：查询可用镜像 ID

~~~
curl -sk -X POST "${KASM_API_URL}/api/public/get_images" \
    -H "Content-Type: application/json" \
    -d "{\"token\": \"${TOKEN}\"}" | python3 -m json.tool | grep -E '"image_id"|"name"'
~~~



##   步骤3：批量创建会话的脚本

~~~
#!/bin/bash
KASM_API_URL="https://localhost"
TOKEN="替换为上面获取的token"
IMAGE_ID="替换为镜像ID"
TARGET_SESSIONS=10   # 目标并发数

for i in $(seq 1 $TARGET_SESSIONS); do
  echo "创建第 $i 个会话..."
  RESULT=$(curl -sk -X POST "${KASM_API_URL}/api/public/request_kasm" \
    -H "Content-Type: application/json" \
    -d "{
      \"token\": \"${TOKEN}\",
      \"image_id\": \"${IMAGE_ID}\"
    }")

  KASM_ID=$(echo $RESULT | python3 -c "import sys,json; d=json.load(sys.stdin);
print(d.get('kasm_id','ERROR'))")
  echo "  会话ID: $KASM_ID"

  # 记录当前资源情况
  echo "  内存: $(free -h | awk '/^Mem:/{print $3"/"$2}')"
  echo "  CPU负载: $(uptime | awk -F'load average:' '{print $2}')"
  echo ""

  sleep 5   # 间隔5秒，避免同时启动压力过大
done
~~~



---
#   四、监控脚本（另开一个终端运行）



~~~
#!/bin/bash

# 持续记录性能数据到文件
LOGFILE="kasm_perf_$(date +%Y%m%d_%H%M%S).csv"
echo "时间,会话容器数,内存已用MB,内存总MB,CPU负载1m,磁盘IO_read,磁盘IO_write" > $LOGFILE

while true; do
  TIME=$(date +%H:%M:%S)

  # 工作区容器数（排除基础服务）
  SESSION_COUNT=$(docker ps --format "{{.Names}}" | grep -v kasm_db | grep -v kasm_api | grep -v kasm_proxy |
grep -v kasm_manager | grep -v kasm_guac | grep -v kasm_rdp | wc -l)

  MEM_USED=$(free -m | awk '/^Mem:/{print $3}')
  MEM_TOTAL=$(free -m | awk '/^Mem:/{print $2}')
  LOAD=$(uptime | awk -F'load average:' '{print $2}' | awk -F',' '{print $1}' | xargs)

  echo "${TIME},${SESSION_COUNT},${MEM_USED},${MEM_TOTAL},${LOAD}" | tee -a $LOGFILE
  sleep 5
done
~~~



---
#   五、判断性能瓶颈的关键指标

~~~
# 内存压力（最关键）
# 当可用内存 < 500MB 时，系统开始用 swap，性能急剧下降
watch -n 1 'free -h'

# OOM Killer 是否触发（容器被强制杀死）
dmesg | grep -i "oom\|killed" | tail -20

# CPU 是否过载
# load average 超过 CPU 核心数说明过载
uptime

# 容器启动是否开始超时
docker events --filter type=container --filter event=die

~~~




---