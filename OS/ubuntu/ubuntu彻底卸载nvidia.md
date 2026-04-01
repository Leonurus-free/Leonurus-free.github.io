# ubuntu彻底卸载nvidia

卸载驱动

```bash
sudo apt-get --purge remove nvidia*
sudo apt autoremove
```

To remove CUDA Toolkit:

```bash
sudo apt-get --purge remove "*cublas*" "cuda*"
```

To remove NVIDIA Drivers:

```bash
sudo apt-get --purge remove "*nvidia*"
```



如果你之前通过 `.run` 文件安装的驱动，可以运行：

```
sudo nvidia-uninstall  # 如果存在该脚本
```

或者重新运行 NVIDIA 驱动的安装文件并选择卸载：

```
sudo ./NVIDIA-Linux-*.run --uninstall
```