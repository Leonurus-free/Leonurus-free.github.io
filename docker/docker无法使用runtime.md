# docker无法使用runtime

这个错误表明你的 Docker 环境中没有正确配置 NVIDIA 容器运行时（`nvidia` runtime）。要解决这个问题，你需要确保正确安装了 NVIDIA 容器工具包（NVIDIA Container Toolkit），并配置 Docker 以支持 NVIDIA GPU。

### 解决方法：

#### 1. **安装 NVIDIA Container Toolkit**

运行以下命令安装 NVIDIA Container Toolkit：

```
# 添加 NVIDIA 的官方 GPG 密钥
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg

# 添加 NVIDIA 的仓库
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

# 更新软件包列表并安装 NVIDIA Container Toolkit
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
```

#### 2. **配置 Docker 使用 NVIDIA 运行时**

运行以下命令配置 Docker：

```
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

#### 3. **验证 NVIDIA 运行时是否可用**

运行以下命令检查 `nvidia` 运行时是否已正确配置：

```
docker info | grep -i runtime
```

输出应该包含 `nvidia`，例如：

```
Runtimes: nvidia runc
```

#### 4. **重新运行你的 Docker 命令**

现在你应该可以正常运行带有 `--runtime nvidia` 的 Docker 命令了：

```
docker run -d --runtime nvidia --gpus "device=0,1" --name vllm_GLM-4-32B-0414 -v /home/ubuntu/luo/model_files:/root/model -v /home/ubuntu/luo/.vllm/vllm:/root/.cache/vllm -v /home/ubuntu/luo/.vllm/huggingface:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN=<secret>" -p 8000:8000 --ipc=host vllm/vllm-openai:v0.8.4 --model /root/model/GLM-4-32B-0414 --gpu-memory-utilization 0.9 --tensor-parallel-size 3 --max-model-len 32768 --served-model-name GLM-4-32B-0414
```

### 替代方案（如果仍然有问题）

如果你使用的是较新版本的 Docker（>=19.03），可以直接使用 `--gpus` 参数而无需 `--runtime nvidia`：

```
docker run -d --gpus "device=0,1" --name vllm_GLM-4-32B-0414 ...
```

这样 Docker 会自动使用 NVIDIA 支持。

### 其他可能的问题

- 确保你的 NVIDIA 驱动已正确安装（运行 `nvidia-smi` 检查）。
- 确保 Docker 已正确安装并运行（`sudo systemctl status docker`）。

如果问题仍然存在，请提供 `nvidia-smi` 和 `docker info` 的输出以便进一步排查。