

curl -x 10d3354ed35ee951.qzc.na.ipidea.online:2333 -U "njnuzq_1985-zone-custom-region-us:zq19851119" ipinfo.ipidea.io





https://www.congress.gov/search?q=%7B%22source%22%3A%22nominations%22%2C%22congress%22%3A%22117%22%7D



https://www.congress.gov/search?q=%7B%22source%22%3A%22nominations%22%2C%22congress%22%3A%22116%22%7D



错误：

raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: unknown error: failed to wait for extension background page to load: chrome-extension://afnpidonopfokmkenglmhfalgegpafcl/_generated_background_page.html
from tab crashed



解决方案：

1、options.add_experimental_option('useAutomationExtension', False)打开自动化扩展   ==解决不了==

通义千问

2、更换插件代码（后来发现网上插件代码都一样）

3、在发生未找到页面元素的时候，彻底关闭浏览器，包括浏览器缓存、cookie。

https://blog.csdn.net/zwq912318834/article/details/79215400?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-79215400-blog-123972316.235%5Ev43%5Epc_blog_bottom_relevance_base1&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-79215400-blog-123972316.235%5Ev43%5Epc_blog_bottom_relevance_base1&utm_relevant_index=1

https://blog.csdn.net/dubo_csdn/article/details/123972316

https://www.volcengine.com/theme/8015403-S-7-1



df -h 查看linux硬盘使用情况



本身id,用户ID，翻译状态，时长，文件地址，





# `qwen`请求的介绍

- `messages`：用户与模型的对话历史。array中的每个元素形式为{"role":角色, "content": 内容}，角色当前可选值：`system`、`user`、`assistant`和`tool`。

  - `system`：表示系统级消息，用于指导模型按照预设的规范、角色或情境进行回应。是否使用`system`角色是可选的，如果使用则必须位于messages的最开始部分。

  - `user`和`assistant`：表示用户和模型的消息。它们应交替出现在对话中，模拟实际对话流程。

  - `tool`：表示工具的消息。在使用function call功能时，如果要传入工具的结果，需将元素的形式设为{"content":"工具返回的结果", "name":"工具的函数名", "role":"tool"}。其中name是工具函数的名称，需要和上轮response中的tool_callsi['name']参数保持一致；content是工具函数的输出。

    

tool参数用于指定可供模型调用的工具库，一次function call流程模型会从中选择其中一个工具。tools中每一个tool的结构如下：

- type，类型为string，表示tools的类型，当前仅支持function。
- function，类型为object，键值包括name，description和parameters：
  - name：类型为string，表示工具函数的名称，必须是字母、数字，可以包含下划线和短划线，最大长度为64。
  - description：类型为string，表示工具函数的描述，供模型选择何时以及如何调用工具函数。
  - parameters：类型为object，表示工具的参数描述，需要是一个合法的JSON Schema。如果parameters参数为空，表示function没有入参。

使用tools时需要同时指定result_format为message。在function call流程中，无论是发起function call的轮次，还是向模型提交工具函数的执行结果，均需设置tools参数。当前支持的模型包括qwen-turbo、qwen-plus、qwen-max和qwen-max-longcontext。

**说明**

tools暂时无法和incremental_output参数同时使用。





硬盘序列号：00748d35173140fc2df033ef0ab00506





    user_id, user_name, user_department, task_name, transcription_statuses, upload_start_time, file_name, file_type, file_duration, file_size, file_location, file_source, file_language, file_frequency, file_detection_time, file_importance, transcription_results, content_preview, keyword

~~~
transcription_statuses, transcription_results
~~~



```
docker run -e XINFERENCE_MODEL_SRC=modelscope -v F:/pythonProject/data/.xinference:/root/.xinference -v F:/pythonProject/data/.cache/huggingface:/root/.cache/huggingface -v F:/pythonProject/data/.cache/modelscope:/root/.cache/modelscope -p 9997:9997 --gpus all xprobe/xinference:latest xinference-local -H 0.0.0.0
```



~~~
python run_server.py --llm Qwen2-72B-Instruct --model_server http://192.168.100.143:8090/v1 --workstation_port 7864 --api_key 123
~~~



zb_user

!Aa123456
