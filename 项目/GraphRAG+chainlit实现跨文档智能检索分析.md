# GraphRAG+chainlit实现跨文档智能检索分析

### 安装

```python
pip3 install graphrag

mkdir -p ./ragtest/input

curl https://raw.githubusercontent.com/win4r/mytest/main/book.txt > ./ragtest/input/book.txt

python3 -m graphrag.index --init --root ./ragtest

python3 -m graphrag.index --root ./ragtest


python3 -m graphrag.query \
--root ./ragtest \
--method global \
"show me some Prompts about Interpretable Soft Prompts."


python3 -m graphrag.query \
--root ./ragtest \
--method local \
"show me some Prompts about Knowledge Generation."
```

### chainlit

```python
#pip3 install chainlit

import chainlit as cl
import subprocess
import shlex


@cl.on_chat_start
def start():
    cl.user_session.set("history", [])


@cl.on_message
async def main(message: cl.Message):
    history = cl.user_session.get("history")

    # 从 Message 对象中提取文本内容
    query = message.content

    # 构建命令
    cmd = [
        "python3", "-m", "graphrag.query",
        "--root", "./ragtest",
        "--method", "local",
    ]

    # 安全地添加查询到命令中
    cmd.append(shlex.quote(query))

    # 运行命令并捕获输出
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        output = result.stdout

        # 提取 "SUCCESS: Local Search Response:" 之后的内容
        response = output.split("SUCCESS: Local Search Response:", 1)[-1].strip()

        history.append((query, response))
        cl.user_session.set("history", history)

        await cl.Message(content=response).send()
    except subprocess.CalledProcessError as e:
        error_message = f"An error occurred: {e.stderr}"
        await cl.Message(content=error_message).send()


if __name__ == "__main__":
    cl.run()
```

