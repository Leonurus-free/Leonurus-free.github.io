# Dockerflie的编写



Docker 是一个开源平台，旨在自动化应用程序的构建、交付和运行。通过 Dockerfile，您可以定义镜像的构建过程。Dockerfile 是由一系列指令组成的文件，Docker 根据这些指令构建镜像。本文将介绍常用的 Dockerfile 指令、格式、解析器指令以及环境变量替换的用法，帮助开发者编写高效、规范的 Dockerfile。

## **Dockerfile 常用指令**

| 指令        | 描述                             |
| :---------- | :------------------------------- |
| ADD         | 添加本地或远程文件和目录。       |
| ARG         | 使用构建时变量。                 |
| CMD         | 指定默认命令。                   |
| COPY        | 复制文件和目录。                 |
| ENTRYPOINT  | 指定默认可执行文件。             |
| ENV         | 设置环境变量。                   |
| EXPOSE      | 描述您的应用程序正在监听的端口。 |
| FROM        | 从基础镜像创建新的构建阶段。     |
| HEALTHCHECK | 启动时检查容器的健康状况。       |
| LABEL       | 向镜像添加元数据。               |
| MAINTAINER  | 指定镜像的作者。                 |
| ONBUILD     | 指定在构建中使用镜像时的说明。   |
| RUN         | 执行构建命令。                   |
| SHELL       | 设置镜像的默认 shell。           |
| STOPSIGNAL  | 指定退出容器的系统调用信号。     |
| USER        | 设置用户和组 ID。                |
| VOLUME      | 创建卷挂载。                     |
| WORKDIR     | 更改工作目录。                   |

## **Dockerfile 格式**

Dockerfile 的基本格式如下：

```
INSTRUCTION arguments
```

- **指令区分大小写**，通常使用大写字母表示。

- **指令按顺序执行**。

- **Dockerfile 必须以`FROM` 指令开头**。

- **注释**：以`#` 开头的行是注释，BuildKit 会忽略这些行，除非它们是有效的解析器指令。

  - 行中的任何其他位置的`#` 标记都被视为参数。这允许使用诸如以下语句

    ```
    RUN echo 'we are running some # of cool things'
    ```

  - 注释行在执行 Dockerfile 指令之前被删除。以下示例中的注释在 shell 执行`echo` 命令之前被删除。

    ```
    RUN echo hello \
    # comment
    world
    ```

    以下示例是等效的。

    ```
    RUN echo hello \
    world
    ```

  - 注释不支持行延续字符。

- **空白符**：指令参数中的空格不会被忽略。

  指令参数中的空格不会被忽略。以下示例按指定的空格打印`hello world`

  ```
  RUN echo "\
       hello\
       world"
  ```

## **解析器指令**

解析器指令是影响 Dockerfile 处理方式的可选指令，它们以特殊注释格式`# directive=value` 编写，并不会添加构建层，也不会显示为构建步骤。

### **规则**

- 解析器指令必须位于 Dockerfile 的顶部。
- 解析器指令不支持行延续字符。
- 解析器指令不区分大小写，且通常采用小写。

### **支持的指令**

- `# syntax=docker/dockerfile:1`：指定 Dockerfile 的语法版本。

  - 如果未指定，BuildKit 使用捆绑的 Dockerfile 前端版本。

  - 设置将使 BuildKit 在构建之前拉取最新的稳定版本的 Dockerfile 语法。

    ```
    # syntax=docker/dockerfile:1
    ```

- `# escape=`：设置转义字符，允许跨行书写指令。

  - 如果未指定，则默认转义字符为`\`。

  - 将转义字符设置为`\` 在`Windows` 上特别有用，因为`\` 是目录路径分隔符。`\` 与 Windows PowerShell一致。

    ```
    # escape=`
    
    FROM microsoft/nanoserver
    COPY testfile.txt c:\
    RUN dir c:\
    ```

### **无效示例**

由于这些规则，以下示例都是无效的：

- 由于行延续而无效

  ```
  # direc \
  tive=value
  ```

- 由于出现两次而无效

  ```
  # directive=value1
  # directive=value2
  
  FROM ImageName
  ```

- 被视为注释，因为它出现在构建器指令之后

  ```
  FROM ImageName
  # directive=value
  ```

- 被视为注释，因为它出现在不是解析器指令的注释之后

  ```
  # About my dockerfile
  # directive=value
  FROM ImageName
  ```

- 以下`unknowndirective` 被视为注释，因为它不被识别。已知的`syntax` 指令被视为注释，因为它出现在不是解析器指令的注释之后。

  ```
  # unknowndirective=value
  # syntax=value
  ```

解析器指令允许使用非换行符空格。因此，以下行都被视为相同

```
#directive=value
# directive =value
# directive= value
# directive = value
#   dIrEcTiVe=value
```

## **环境变量替换**

Dockerfile 中的环境变量通过`ENV` 指令进行定义，可以在多个指令中作为变量进行替换。环境变量在 Dockerfile 中通常使用`$variable_name` 或`${variable_name}` 的形式进行引用，它们是等效的。大括号语法（`${}`）一般用于处理没有空格的变量名问题，例如`${foo}_bar`。

### **变量替换语法**

- `$variable_name` 和`${variable_name}` 都可以表示环境变量。
- `${variable_name}` 语法支持一些标准的`bash` 修饰符，例如：
  - `${variable:-word}`：如果设置了`variable`，则结果为该值；如果未设置`variable`，则结果为`word`。
  - `${variable:+word}`：如果设置了`variable`，则结果为`word`；否则结果为空字符串。

### **转义环境变量**

如果需要在 Dockerfile 中转义整个变量名，可以在变量名前添加`\`。例如：

- `\$foo` 或`\${foo}` 分别表示`$foo` 和`${foo}` 文字。

示例（解析后的表示形式显示在`#` 之后）

```
FROM busybox
ENV FOO=/bar
WORKDIR ${FOO}   # WORKDIR /bar
ADD . $FOO       # ADD . /bar
COPY \$FOO /quux # COPY $FOO /quux
```

### **支持环境变量的指令**

以下是支持环境变量替换的 Dockerfile 指令列表：

- `ADD`
- `COPY`
- `ENV`
- `EXPOSE`
- `FROM`
- `LABEL`
- `STOPSIGNAL`
- `USER`
- `VOLUME`
- `WORKDIR`
- `ONBUILD`（与上述支持的指令之一组合时）

### **`RUN`、`CMD` 和`ENTRYPOINT` 中的环境变量**

您还可以将环境变量与`RUN`、`CMD` 和`ENTRYPOINT` 指令一起使用。但在这些指令中，变量替换是由命令 shell 处理的，而不是由构建器处理的。

### **环境变量的作用范围**

在 Dockerfile 中，环境变量的替换在整个指令中使用相同的值。修改环境变量的值仅对后续的指令生效。

```
ENV abc=hello
ENV abc=bye def=$abc
ENV ghi=$abc
```

在这个例子中：

- `def` 的值变为`hello`。
- `ghi` 的值变为`bye`。

## **总结**

Dockerfile 是构建 Docker 镜像的核心工具，理解和掌握常用指令及解析器指令的使用，能够帮助您高效地构建镜像并简化 DevOps 流程。通过合理设置环境变量和优化构建过程，您可以提升应用程序的可移植性和可维护性。



~~~
# 基础镜像
FROM nvidia/cuda:12.2.0-base-ubuntu22.04

# 设置工作目录
WORKDIR /CODE

# 安装基础依赖
# 更新系统并安装必要的软件包
RUN apt-get update \
    && apt-get install -y python3.11 python3.11-venv python3.11-dev \
	&& apt-get install -y nginx \
	&& apt-get install -y redis \
	&& apt-get install -y vim \
    && apt-get clean

# 设置 python3 和 pip3 指向 Python 3.11
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1

# 安装 pip
RUN apt-get install -y python3-pip

# 复制项目文件到容器
COPY . /CODE

# 安装项目依赖
RUN pip install --no-cache-dir -r /CODE/requirements.txt

# 暴露端口
EXPOSE 80
EXPOSE 7001

# 设置默认命令
CMD ["/bin/bash"]

~~~

## 构建Docker镜像

~~~
docker build -t corrective_image .
~~~

