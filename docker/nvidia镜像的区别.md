# nvidia镜像的区别



**12.6.3-cudnn-runtime-ubuntu22.04 (12.6.3/ubuntu2204/runtime/cudnn/Dockerfile)**：

- 这个镜像包含了 **CUDA 12.6.3** 和 **cuDNN** 的运行时环境。
- **cuDNN** 是针对深度学习优化的 GPU 加速库，这意味着它包含了深度学习相关的运行时支持库。
- 适用于需要在容器中运行已经训练好的深度学习模型的场景。

**12.6.3-runtime-ubuntu22.04 (12.6.3/ubuntu2204/runtime/Dockerfile)**：

- 这个镜像只包含 **CUDA 12.6.3** 的运行时环境，而没有 cuDNN。
- 它适用于那些只需要使用 CUDA 的基本功能，但不依赖于 cuDNN 库的应用。

**12.6.3-cudnn-devel-ubuntu22.04 (12.6.3/ubuntu2204/devel/cudnn/Dockerfile)**：

- 这个镜像包含了 **CUDA 12.6.3** 和 **cuDNN** 的开发环境。
- 包含了 **开发工具**，如编译器和头文件，适用于开发和编译需要 CUDA 和 cuDNN 支持的程序或库。

**12.6.3-devel-ubuntu22.04 (12.6.3/ubuntu2204/devel/Dockerfile)**：

- 这个镜像只包含了 **CUDA 12.6.3** 的开发环境，但不包括 cuDNN。
- 它适用于开发不需要 cuDNN 支持的 CUDA 应用。

**12.6.3-base-ubuntu22.04 (12.6.3/ubuntu2204/base/Dockerfile)**：

- 这个镜像包含了基础的 **CUDA 12.6.3** 环境，不包括任何额外的库，如 cuDNN、开发工具等。
- 适用于你只需要基础 CUDA 环境的情况，可以在此基础上自定义安装其他工具和库。



在这些镜像中，只有 **`devel`** 版本的镜像包含了 **`nvcc`**，即 CUDA 编译器。`nvcc` 是用来编译 CUDA C++ 代码的工具，通常只出现在开发环境中。