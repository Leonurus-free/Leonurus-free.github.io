

~~~python
import argparse
import os
import sys

# Check if huggingface_hub is installed, if not, install it
try:
    import huggingface_hub
except ImportError:
    print("Install huggingface_hub.")
    os.system("pip install -U huggingface_hub")


parser = argparse.ArgumentParser(description="HuggingFace Download Accelerator Script.")
parser.add_argument(
    "--model",
    "-M",
    default=None,
    type=str,
    help="model name in huggingface, e.g., baichuan-inc/Baichuan2-7B-Chat",
)
parser.add_argument(
    "--token",
    "-T",
    default=None,
    type=str,
    help="hugging face access token for download meta-llama/Llama-2-7b-hf, e.g., hf_***** ",
)
parser.add_argument(
    "--include",
    default=None,
    type=str,
    help="Specify the file to be downloaded",
)
parser.add_argument(
    "--exclude",
    default=None,
    type=str,
    help="Files you don't want to download",
)
parser.add_argument(
    "--dataset",
    "-D",
    default=None,
    type=str,
    help="dataset name in huggingface, e.g., zh-plus/tiny-imagenet",
)
parser.add_argument(
    "--save_dir",
    "-S",
    default=None,
    type=str,
    help="path to be saved after downloading.",
)
parser.add_argument(
    "--use_hf_transfer", default=True, type=eval, help="Use hf-transfer, default: True"
)
parser.add_argument(
    "--use_mirror", default=True, type=eval, help="Download from mirror, default: True"
)

args = parser.parse_args()

if args.use_hf_transfer:
    # Check if hf_transfer is installed, if not, install it
    try:
        import hf_transfer
    except ImportError:
        print("Install hf_transfer.")
        os.system("pip install -U hf-transfer -i https://pypi.org/simple")
    # Enable hf-transfer if specified
    os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
    print("export HF_HUB_ENABLE_HF_TRANSFER=", os.getenv("HF_HUB_ENABLE_HF_TRANSFER"))


if args.model is None and args.dataset is None:
    print(
        "Specify the name of the model or dataset, e.g., --model baichuan-inc/Baichuan2-7B-Chat"
    )
    sys.exit()
elif args.model is not None and args.dataset is not None:
    print("Only one model or dataset can be downloaded at a time.")
    sys.exit()

if args.use_mirror:
    # Set default endpoint to mirror site if specified
    os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
    print("export HF_ENDPOINT=", os.getenv("HF_ENDPOINT"))  # https://hf-mirror.com


if args.token is not None:
    token_option = "--token %s" % args.token
else:
    token_option = ""

if args.include is not None:
    include_option = "--include %s" % args.include
else:
    include_option =  ""
    
if args.exclude is not None:
    exclude_option = "--exclude %s" % args.exclude
else:
    exclude_option = ""
    
    
if args.model is not None:
    model_name = args.model.split("/")
    save_dir_option = ""
    if args.save_dir is not None:
        if len(model_name) > 1:
            save_path = os.path.join(
                args.save_dir, "models--%s--%s" % (model_name[0], model_name[1])
            )
        else:
            save_path = os.path.join(
                args.save_dir, "models--%s" % (model_name[0])
            )
        save_dir_option = "--local-dir %s" % save_path

    download_shell = (
        "huggingface-cli download %s %s %s --local-dir-use-symlinks False --resume-download %s %s"
        % (token_option, include_option, exclude_option, args.model, save_dir_option)
    )
    os.system(download_shell)

elif args.dataset is not None:
    dataset_name = args.dataset.split("/")
    save_dir_option = ""
    if args.save_dir is not None:
        if len(dataset_name) > 1:
            save_path = os.path.join(
                args.save_dir, "datasets--%s--%s" % (dataset_name[0], dataset_name[1])
            )
        else:
            save_path = os.path.join(
                args.save_dir, "datasets--%s" % (dataset_name[0])
            )
        save_dir_option = "--local-dir %s" % save_path

    download_shell = (
        "huggingface-cli download %s %s %s --local-dir-use-symlinks False --resume-download  --repo-type dataset %s %s"
        % (token_option, include_option, exclude_option, args.dataset, save_dir_option)
    )
    os.system(download_shell)

~~~





## Usage

### 下载模型

从HuggingFace上获取到所需模型名，例如 `lmsys/vicuna-7b-v1.5`：

```
python hf_download.py --model lmsys/vicuna-7b-v1.5 --save_dir ./hf_hub
```

如果下载需要授权的模型，例如 meta-llama 系列，则需要指定 `--token` 参数为你的 Huggingface Access Token。

**注意事项：**

（1）若指定了 `--save_dir`，下载过程中会将文件先暂存在 transformers 的默认路径`~/.cache/huggingface/hub`中，下载完成后自动移动到`--save_dir`指定目录下，因此需要在下载前保证默认路径下有足够容量。

下载完成后使用 transformers 库加载时需要指定保存后的路径，例如：

```
from transformers import pipeline
pipe = pipeline("text-generation", model="./hf_hub/models--lmsys--vicuna-7b-v1.5")
```

**若不指定 `--save_dir` 则会下载到默认路径`~/.cache/huggingface/hub`中，这时调用模型可以直接使用模型名称 `lmsys/vicuna-7b-v1.5`。**

（2）若不想在调用时使用绝对路径，又不希望将所有模型保存在默认路径下，可以通过**软链接**的方式进行设置，步骤如下：

- 先在任意位置创建目录，作为下载文件的真实存储位置，例如：

  ```
  mkdir /data/huggingface_cache
  ```

- 若 transforms 已经在默认位置`~/.cache/huggingface/hub`创建了目录，需要先删除：

  ```
  rm -r ~/.cache/huggingface
  ```

- 创建软链接指向真实存储目录：

  ```
  ln -s /data/huggingface_cache ~/.cache/huggingface
  ```

- 之后运行下载脚本时**不要指定**`save_dir`，会自动下载至第一步创建的目录下：

  ```
  python hf_download.py --model lmsys/vicuna-7b-v1.5
  ```

- 通过这种方式，调用模型时可以直接使用模型名称，而不需要使用存储路径：

  ```
  from transformers import pipeline
  pipe = pipeline("text-generation", model="lmsys/vicuna-7b-v1.5")
  ```

（3）脚本内置通过 pip 自动安装 huggingface-cli 和 hf_transfer。如果 hf_transfer 版本低于 0.1.4 则不会显示下载进度条，可以手动更新：

```
pip install -U hf-transfer -i https://pypi.org/simple
```

如出现 `huggingface-cli: error` 问题，尝试重新安装：

```
pip install -U huggingface_hub
```

如出现关于 `hf_transfer`的报错，可以通过`--use_hf_transfer False`参数关闭hf_transfer。

### 下载数据集

和下载模型同理，以 `zh-plus/tiny-imagenet` 为例:

```
python hf_download.py --dataset zh-plus/tiny-imagenet --save_dir ./hf_hub
```

### 参数说明

- `--model`: huggingface上要下载的模型名称，例如 `--model lmsys/vicuna-7b-v1.5`
- `--dataset`: huggingface上要下载的数据集名称，例如 `--dataset zh-plus/tiny-imagenet`
- `--save_dir`: 文件下载后实际的存储路径
- `--token`: 下载需要登录的模型（Gated Model），例如`meta-llama/Llama-2-7b-hf`时，需要指定hugginface的token，格式为`hf_****`
- `--use_hf_transfer`: 使用 hf-transfer 进行加速下载，默认开启(True), 若版本低于开启将不显示进度条。
- `--use_mirror`: 从镜像站 https://hf-mirror.com/ 下载, 默认开启(True), 国内用户建议开启
- `--include`: 下载指定的文件，例如 `--include "tokenizer.model tokenizer_config.json"` 或 `--include "*.bin` 下载
- `--exclude`: 不下载指定的文件，与include用法一致，例如 `--exclude "*.md"`