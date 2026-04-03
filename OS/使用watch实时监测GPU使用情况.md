# 使用 watch 实时监测 GPU 使用情况

遇到一个场景：在大模型推理时，需实时观测GPU使用情况，nvidia-smi提供-l选项用于周期性的输出GPU使用情况。每2s输出一次GPU使用情况，命令如下：

```
nvidia-smi -l 2
```

该命令不会清空上次输出，而是持续输出到终端中。类似每2s调用一次nvidia-smi。

通过for循环，调用clear、nvidia-smi、sleep可实现清空上次输出，使nvidia-smi输出在固定位置。命令如下：

```
for i in {1..100}; do clear; nvidia-smi; sleep 2; done
```

调用clear会使屏幕闪烁。

watch命令会按照指定的间隔时间执行命令并显示其输出。watch在固定的位置显示命令的输出，输出变化时，只更新变化的部分，屏幕不再闪烁。每2s输出一次GPU使用情况，命令如下：

```
watch -n 2 nvidia-smi
```

watch提供-d选项，高亮显示变化的部分。每2s输出一次GPU使用情况，并高亮显示变化部分，命令如下：

```
watch -n 2 -d nvidia-smi
```

我写了一个称作docker.sh的小项目，该项目旨在通过一系列的实验使用户对docker的底层技术，如Namespace、CGroups、rootfs、联合加载、Docker 网络、iptables等有一个感性的认识。在此过程中，我们还将通过Shell脚本一步一步地实现一个简易的docker，以期使读者在使用docker的过程中知其然知其所以然。该项目的仓库地址如下：

```
https://github.com/pandengyang/docker.sh.git
```

可用于学习 Docker 原理，里面有Namespace、CGroups、Docker 网络的原理及示例的介绍。

我写了一个小项目桃花源（英文名为 peach），该项目是一个迷你虚拟机，用于学习 Intel 硬件虚拟化技术。学习该项目可使读者对 CPU 虚拟化、内存虚拟化技术有个感性、直观的认识，为学习 KVM 打下坚实的基础。peach 实现了如下功能：

- 使用Intel VT-x技术实现CPU虚拟化
- 使用EPT技术实现内存虚拟化
- 支持虚拟x86实模式运行环境
- 支持虚拟CPUID指令
- 支持虚拟HLT指令，Guest利用HLT指令关机

代码仓库如下：

```
https://github.com/pandengyang/peach.git
```