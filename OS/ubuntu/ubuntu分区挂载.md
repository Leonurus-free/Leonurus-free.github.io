![image-20250530164123845](./ubuntu分区挂载/image-20250530164123845.png)

# 挂载2T以上的磁盘

因为 [fdisk](https://zhida.zhihu.com/search?content_id=238237563&content_type=Article&match_order=1&q=fdisk&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NDg3NzAzNDcsInEiOiJmZGlzayIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjIzODIzNzU2MywiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.r13BG8z96RIb21CZKWwoi5KYjla4BQxo__ym49iY7XA&zhida_source=entity) 主要是针对[MBR](https://zhida.zhihu.com/search?content_id=238237563&content_type=Article&match_order=1&q=MBR&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NDg3NzAzNDcsInEiOiJNQlIiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMzgyMzc1NjMsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.HQxIliaBg4aRonxJhlO_R-Pti_-eT3AqnyqcEnkHqyA&zhida_source=entity)分区磁盘设计的，MBR支持的最大磁盘容量为2T（2^32 * 512 B）；下面主要用 [parted](https://zhida.zhihu.com/search?content_id=238237563&content_type=Article&match_order=1&q=parted&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NDg3NzAzNDcsInEiOiJwYXJ0ZWQiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMzgyMzc1NjMsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.00bSGZfSJW8EMMNRFm_bFXIZLDwijPPOaZzG9JtW0ok&zhida_source=entity) 给2T以上的磁盘进行分区。

## 初始条件

Ubuntu 22.04

未分区磁盘 3T

![img](./ubuntu分区挂载/v2-0cc38a20f5794ca5f17aafd75a181fcd_1440w.jpg)

### 操作目标

将新磁盘 /dev/sdb 全量挂载到 /data 目录下

## 具体操作步骤

1、查看磁盘 fdisk -l ，如上图所示。

2、当前对设备/dev/sdb ，进行全量分区。

```text
parted /dev/sdb
#显示当前磁盘的基本信息和已存在的分区情况
print
#将磁盘的分区表类型转换为GUID Partition Table (GPT)
mklabel gpt
#文件系统类型为ext4，从磁盘的开始位置（0%）到结束位置（100%）占用全部空间
mkpart primary ext4 0% 100%
print
#退出
quit
```

![img](./ubuntu分区挂载/v2-eeafd30ad44aed5210dc113c0ff4f7ea_1440w.jpg)

### 磁盘挂载

关键命令

```text
#格式化磁盘 时间比较长
mkfs.ext4 /dev/sdb1
sudo 

ls -l /dev/disk/by-uuid/
sudo vim /etc/fstab
#添加一行记录 挂载磁盘推荐用uuid的形式，这样在磁盘增加或减少时的盘的挂载是稳定的，以免/dev/sdb名称变动
UUID=74954814-8b48-4763-902f-d025b4cfbed0 /data ext4 defaults 0 0
# 新建挂载目录
sudo mkdir /data
sudo chmod -R 777 /data
#执行挂载
mount -a
#查看挂载信息
mount
```

![img](./ubuntu分区挂载/v2-7342fad27b3e9ea46e6f653519ffdb5c_1440w.jpg)

重启查看挂载信息 mount