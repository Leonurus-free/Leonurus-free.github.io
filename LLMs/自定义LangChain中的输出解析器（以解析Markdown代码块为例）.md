# 自定义LangChain中的输出解析器（以解析Markdown代码块为例）

## 01 LangChain输出解析器简介

官方文档关于输出解析器的传送门：

https://python.langchain.com/docs/modules/model_io/output_parsers

LangChain中的输出解析器属于`提示词模板`的范畴，简单说，就是在提示词模板中加入对输出格式的说明，然后预期大模型以符合该格式的内容进行输出，我们再对结果进行解析。

类似下面这种效果：

```python
prompt = """
请给我3个有关天空的形容词。

你的输出需要以逗号分隔，例如：
good, nice, wonderful

你的输出：
"""
```

有了输出解析器，我们在创建多个chain进行流水线处理的时候，可以保证每个chain的输入和输出是符合格式预期的，从而保证整个chain的稳定性。

在官方文档中，给出了5种主要的输出解析器，分别是：

- **List parser** 列表解析器，指定输出为列表格式
- **Datetime parser** 日期时间解析器，指定输出满足时间日期格式
- **Enum parser** 枚举解析器，指定输出的值只能为枚举值
- **Pydantic (JSON) parser** JSON解析器，指定输出的内容满足JSON格式
- **Structured output parser** 结构化输出解析器，该解析器接收一个自定义类，根据类的字段及描述，返回的内容满足该类的JSON范式

不过官方文档中没有提到如何自定义一个输出解析器

本文以Markdown文档的代码块为例举例说明如何自定义一个输出解析器。

## 02 自定义Markdown代码块解析器

### 2.1 需求描述

我希望模型的输出是一个Markdown代码块（或是需要包含Markdown代码块），以便我解析到代码块中的内容。

例如一个经典的使用场景：自然语言转sql，我希望大模型生成的sql语句总是包裹在Markdown代码块中，方便我识别提取。

### 2.2 编码实现

新建一个`custom_parser.py`文件来实现。

下面是代码：

~~~python
import re
from typing import Any, Literal

from langchain.schema import BaseOutputParser, OutputParserException

# 自定义代码块输出解析器结构化指令的提示词
CUSTOM_CODE_BLOCK_INSTRUCTIONS = """
The output should be format as a Markdown-formatted Code Block.
Here is the output example:
```
(code content, such as sql,python,java,etc.)
```
"""


class CodeBlockOutputParser(BaseOutputParser[str]):
    """
    自定义一个代码块输出解析器，继承BaseOutputParser类，其中的泛型表示解析后要返回的数据类型。
    继承基类后，需要实现3个方法，分别是：
    parse -> 该方法用于解析大模型的输出，将其解析为既定格式，返回值即为泛型类型，例如在列表解析中返回类型为List
    get_format_instructions -> 该方法返回一段提示词，该提示词需要嵌入到原本的提示词模板中，作为对大模型返回格式的提示
    _type -> 这是一个只读的私有方法，调用该方法可获取解析器的类型，类型支持自命名
	"""
	# 自定义的一个字段，用于指定返回代码块的类型
    code_type: str = None

	# 在这段初始化方法中，指定了code_type只能为限定类型的代码
    def __init__(self, code_type: Literal["sql", "python", "java", "bash"] = "sql", **kwargs: Any):
        super().__init__(**kwargs)
        self.code_type = code_type

    def parse(self, text: str) -> str:
        """该方法用于解析模型的输出"""
        # 使用非贪婪匹配 .*? 来捕获三个反引号之间的任何内容
        pattern = r'```(.*?)```'

        # 执行搜索
        match = re.search(pattern, text, re.DOTALL)

        # 判断并输出结果
        if match:
            code = match.group(1)
            code = code.strip(self.code_type).strip()
            return code
        else:
            raise OutputParserException("The response has no code block.", llm_output=text)

    def get_format_instructions(self) -> str:
        """给出格式化指令"""
        return CUSTOM_CODE_BLOCK_INSTRUCTIONS

    @property
    def _type(self) -> str:
        """返回该解析器的类型 这里返回的是自定义代码块解析器"""
        return "CustomCodeBlock"
~~~

## 03 使用自定义的输出解析器

自定义输出解析器的用法与LangChain自带的输出解析器的用法是一样的，下面是示例代码：

~~~python
from langchain import PromptTemplate, OpenAI
from custom_parser import CodeBlockOutputParser

# 创建大语言模型 API-KEY写在环境变量中了
llm = OpenAI(temperature=0)

# 写一个示例提示词模板，其中需要为格式化输出提示词预留空位
sql_prompt = "请为我写一个sql查询语句，查询user表中年龄在20到30岁之间用户的用户名。\n{format_instructions}"

# 创建代码块输出解析器对象
output_parser = CodeBlockOutputParser(code_type="sql")
format_instructions = output_parser.get_format_instructions()  # 获取格式化提示词

----------------------------------------------------------------------------------------------------

# 组装提示词
prompt = PromptTemplate(template=sql_prompt, input_variables=[], partial_variables={"format_instructions": format_instructions})
prompt = prompt.format()
print(f"提示词为：\n{prompt}")
"""
提示词为：
请为我写一个sql查询语句，查询user表中年龄在20到30岁之间用户的用户名。
The output should be format as a Markdown-formatted Code Block.
Here is the output example:
```
(code content, such as sql,python,java,etc.)
```
"""

----------------------------------------------------------------------------------------------------

# 调用大模型获取结果
output_raw = llm(prompt=prompt)
print(f"原始输出为：\n{output_raw}")
"""
原始输出为：
```
SELECT username FROM user WHERE age BETWEEN 20 AND 30;
```
"""

----------------------------------------------------------------------------------------------------
# 解析输出的结果
output = output_parser.parse(output_raw)
print(f"解析后的输出为：\n{output}")
"""
解析后的输出为：
SELECT username FROM user WHERE age BETWEEN 20 AND 30;
"""
~~~

