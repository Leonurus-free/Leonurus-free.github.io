# conda基本操作

### 环境相关

```
# 配置指定python版本的环境
conda create -n env_name python=2.7
conda create --name env_name python=3.5 numpy scipy

# 列出所有的环境
conda env list
conda info -e
conda info --envs

# 激活环境
conda activate env_name

# 退出环境
conda decativate env_name

# 删除环境
conda remove -n env_name --all

# 环境中的包的管理
conda install pkg_name -n env_name
conda uninstall pkg_name -n env_name
conda remove pkg_name -n env_name

# 复制环境
conda create --name new_env_name --clone old_env_name

# 分享环境
# 把已有的环境分享给其他人，A电脑到B电脑
# A电脑上的操作
conda activate target_env
conda env export > target_env.yml

# 从A copy yml文件，B电脑上的操作
conda env create -f target_env.yml
```

### 软件包相关

```
# 在当前环境中安装
conda install pkg_name 

# 在指定虚拟环境中安装
conda install -n env_name pkg_name

# 升级包
conda update pkg_name
conda update -n env_name pkg_name

# 搜索包
conda search pkg_name


# 指定升级渠道（源）
conda install -c conda-forge pkg_name

# 更改镜像源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes # 搜索时显示通道地址

# 卸载包
conda remove pkg_name
conda remove -n env_name pkg_name

# 列出所有安装的包
conda list --name env_name
conda list -n env_name
conda activate env_name && conda list

# 更新所有包
conda upgrade --all
```

### conda瘦身

```
# 删除没用的包
conda clean -p

# Remove cached package tarballs
conda clean -t

# 删除所有的安装包及cache
conda clean -y -all
```

### condarc添加国内源

```
$ vi ~/.condarc
channels:
  - defaults
show_channel_urls: true default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
  - r
  - bioconda
  - conda-forge

custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud

envs_dirs:
  - /home/luna/miniconda3/build/envs
  - /home/luna/anaconda3/envs

pkgs_dirs:
  - /home/luna/miniconda3/build/pkgs
  - /home/luna/anaconda3/pkgs

auto_activate_base: false
```

## 参考

[conda常用命令](https://www.jianshu.com/p/7ebe1df808ba)

[Conda Command reference](https://docs.conda.io/projects/conda/en/latest/commands.html#conda-general-commands)

[conda清理没用的安装包](https://blog.csdn.net/weixin_41481113/article/details/88411241)