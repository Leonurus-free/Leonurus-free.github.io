# 使用 ClamAV 进行 Ubuntu 系统病毒扫描

ClamAV 是一款开源的反病毒引擎，用于检测和清除恶意软件和病毒。在本文中，我们将介绍如何在 Ubuntu 系统上安装、配置和使用 ClamAV 进行病毒扫描。

## 1.ClamAV 简介

ClamAV 是一个流行的反病毒引擎，它可以用于扫描文件和目录，以查找潜在的恶意软件和病毒。它是一个开源工具，可用于保护你的系统免受恶意软件的威胁。

## 2.具体使用教程

### 2.1安装 ClamAV

在 Ubuntu 系统上，你可以使用以下命令来安装 ClamAV：

```bash
sudo apt-get install clamav
```

安装后可以使用以下命令来确认是否成功启动：

```bash
systemctl list-unit-files | grep clamav
```

如果显示

```bash
clamav-daemon.service                                                     
clamav-freshclam.service                                              
```

表示正常跑起来了。

### 2.2更新病毒库

安装完成后，为了保持病毒库的最新状态，我们需要定期更新它。首先，停止 ClamAV 的病毒库更新服务：

```bash
sudo systemctl stop clamav-freshclam
```

然后运行以下命令来手动更新病毒库：

```bash
sudo freshclam
```

完成更新后，重新启动 ClamAV 的病毒库更新服务：

```bash
sudo systemctl start clamav-freshclam
```

设置后台自动升级病毒库：

```bash
systemctl start clamav-freshclam
systemctl enable clamav-freshclam
```

如果报错可以使用以下方法

```bash
sudo rm /var/log/clamav/freshclam.log
sudo touch /var/log/clamav/freshclam.log
sudo chown clamav:clamav /var/log/clamav/freshclam.log
```

### 2.3修改/etc/logrotate.d/clamav-freshclam

```bash
sudo vim /etc/logrotate.d/clamav-freshclam
/var/log/clamav/freshclam.log {
     rotate 12
     weekly
     compress
     delaycompress
     missingok
     create 640  clamav clamav
     postrotate
     if [ -d /run/systemd/system ]; then
         systemctl -q is-active clamav-freshclam && systemctl kill --signal=SIGHUP clamav-freshclam || true
     else
         invoke-rc.d clamav-freshclam reload-log > /dev/null || true
     fi
     endscript
     }
~        
```

把create 640 clamav **adm**改成**create 640 clamav clamav**

再次运行

```bash
sudo freshclam
Mon Dec 25 19:36:41 2023 -> ^Your ClamAV installation is OUTDATED!
Mon Dec 25 19:36:41 2023 -> ^Local version: 0.103.9 Recommended version: 0.103.11
Mon Dec 25 19:36:41 2023 -> DON'T PANIC! Read https://docs.clamav.net/manual/Installing.html
Mon Dec 25 19:36:41 2023 -> daily database available for update (local version: 27133, remote version: 27134)
Current database is 1 version behind.
Downloading database patch # 27134...
Time:    0.1s, ETA:    0.0s [========================>]    4.76KiB/4.76KiB
Mon Dec 25 19:36:42 2023 -> Testing database: '/var/lib/clamav/tmp.491bf71/clamav-4cc5abccea9b682713a5.tmp-daily.cld' ...
Mon Dec 25 19:36:45 2023 -> Database test passed.
Mon Dec 25 19:36:45 2023 -> daily.cld updated (version: 27134, sigs: 2049428, f-level: 90, builder: raynman)
Mon Dec 25 19:36:45 2023 -> main.cvd database is up-to-date (version: 62, sigs: 6647427, f-level: 90, builder: sigmgr)
Mon Dec 25 19:36:45 2023 -> bytecode.cvd database is up-to-date (version: 334, sigs: 91, f-level: 90, builder: anvilleg)
Mon Dec 25 19:36:45 2023 -> Clamd successfully notified about the update.
```

## 升级ClamAV

可以发现上面的日志显示Mon Dec 25 19:36:41 2023 -> ^Local version: 0.103.9 Recommended version: 0.103.11这告诉我们本地的版本为0.103.9 可以升级到0.103.11

我们可以在下面的地址找到最新版本。
[ClamAV](https://www.clamav.net/download.html#otherversions)
以下载最新的**1.2.1** **Latest**为例
下载
[clamav-1.2.1.linux.i686.deb](https://www.clamav.net/downloads/production/clamav-1.2.1.linux.i686.deb)
输入命令安装

```
sudo dpkg -i clamav-1.2.1.linux.i686.deb
```

### 配置freshclam.conf

```
sudo cp /usr/local/etc/freshclam.conf.sample /usr/local/etc/freshclam.conf

sudo vim /usr/local/etc/freshclam.conf
把Example加上注释

#Example
```

保存退出输入

```
clamscan --version
```

查看版本。

再次运行

```bash
sudo freshclam

reating missing database directory: /usr/local/share/clamav
Assigned ownership of database directory to user "clamav".
ClamAV update process started at Mon Dec 25 19:42:54 2023
daily database available for download (remote version: 27134)
Time:    0.7s, ETA:    0.0s [========================>]   59.57MiB/59.57MiB
Testing database: '/usr/local/share/clamav/tmp.20274d2f53/clamav-79a3679fe8a796d1c9e69f6ae331aee6.tmp-daily.cvd' ...
Database test passed.
daily.cvd updated (version: 27133, sigs: 2049397, f-level: 90, builder: raynman)
Received an older daily CVD than was advertised. We'll retry so the incremental update will ensure we're up-to-date.
daily database available for update (local version: 27133, remote version: 27134)
Current database is 1 version behind.
Downloading database patch # 27134...
Time:    0.0s, ETA:    0.0s [========================>]    4.76KiB/4.76KiB
Testing database: '/usr/local/share/clamav/tmp.20274d2f53/clamav-c430c67fb0a4c84683f741d6b47a74da.tmp-daily.cld' ...
Database test passed.
daily.cld updated (version: 27134, sigs: 2049428, f-level: 90, builder: raynman)
main database available for download (remote version: 62)
Time:    2.6s, ETA:    0.0s [========================>]  162.58MiB/162.58MiB
Testing database: '/usr/local/share/clamav/tmp.20274d2f53/clamav-b1d4862a68bf3fea3f24eecbf4de78ba.tmp-main.cvd' ...
Database test passed.
main.cvd updated (version: 62, sigs: 6647427, f-level: 90, builder: sigmgr)
bytecode database available for download (remote version: 334)
Time:    0.0s, ETA:    0.0s [========================>]  285.12KiB/285.12KiB
Testing database: '/usr/local/share/clamav/tmp.20274d2f53/clamav-1c4548c1e22afef68266862585abf44d.tmp-bytecode.cvd' ...
Database test passed.
bytecode.cvd updated (version: 334, sigs: 91, f-level: 90, builder: anvilleg)
```

## 3.扫描示例

### 3.1扫描并只显示感染文件路径

你可以使用 `-i` 参数来执行扫描并只显示感染了病毒的文件的路径。例如：

```bash
clamscan -r -i /home
```

这将递归扫描 `/home` 目录及其子目录中的文件，并只显示感染了病毒的文件路径列表。

### 3.2扫描并显示全部结果

如果不使用 `-i` 参数，`clamscan` 将显示所有扫描结果，包括感染和非感染的文件。

```bash
clamscan -r /home
```

## 出日志和定时扫描

你可以使用 `-l` 参数来指定扫描结果的日志文件，例如：

```bash
clamscan -r -i /home -l /var/log/clamav/scan.log
```

这将把扫描结果输出到 `/var/log/clamav/scan.log` 文件中。

要定时每天扫描一次，你可以使用 cron 任务。编辑你的 cron 配置文件：

```bash
crontab -e
```

然后添加以下行来在每天的固定时间运行扫描任务：

```bash
0 2 * * * clamscan -r -i /home -l /var/log/clamav/scan.log
```

这将在每天凌晨 2 点运行 ClamAV 扫描并将结果输出到 `/var/log/clamav/scan.log` 文件中。

## 总结

ClamAV 是一个强大的工具，可以帮助你保护 Ubuntu 系统免受恶意软件和病毒的威胁。通过定期更新病毒库、使用不同的扫描参数以及设置定时任务，你可以确保你的系统保持安全。希望这篇文章能帮助你更好地了解如何使用 ClamAV 来增强系统的安全性。