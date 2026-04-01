

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







LLMs and Human-AI Interaction. LLMs (Brown et al.,2020; OpenAI, 2023) a class of neural networks that execute in auto-regressive for text generation. Given a sequence of text tokens with length t as x1:t = (x1, . . . , xt),the generation of a next token xt+1 could be formulated as sampling from a probabilistic model P (·|x1:t).



LLM 和人类-人工智能交互。LLM（Brown 等，2020；OpenAI，2023）是一类用于文本生成的自回归神经网络。给定长度为 t 的文本序列 x1:t = (x1, ..., xt)，生成下一个 token xt+1 可以表示为从概率模型 P (·|x1:t) 中采样。





我是一名个人开发者，我非常热爱计算机领域，喜欢做一个有趣的小应用，擅长python、c++、ts、人工智能开发。偶然间看到贵站的论坛水平非常高，我想和各位大佬交流技术，因此特申请注册！望能同意我的请求。





请参考文件apps\web-antd\src\views\rss\in-content-drawer.vue，我想将录音详情页apps\web-antd\src\views\multi-media\components\recording-detail-modal.vue使用抽屉    
  实现。其中抽屉中的布局你可以参考图片中[Image #3]的布局.1、请特别注意抽屉文件的实现方式，要求代码规范，逻辑清晰。2、请注意图片布局中的内容，就比如左侧是转写内容 ，左边上面上说话人，右边是摘要和笔记，右边下面是RAG问答等等。技术栈：Vben5、vue3、antd、tailwind css等来实现。请先给出你的思考过程，不要修改代码



我已经按照 文件结构：
  recording-detail-drawer.vue  # 主抽屉组件
  ├── TranscriptionPanel.vue   # 左侧转录面板
  ├── SummaryPanel.vue         # 右侧摘要面板
  ├── ChatPanel.vue            # RAG对话面板
  └── AudioPlayer.vue          # 音频播放器组件

实现了抽屉的功能，但是还有一些问题。请参考文件apps\web-antd\src\views\rss\in-content-drawer.vue文件的抽屉实现，参考图片中[Image #3]的布局。帮我检查一下录音详情抽屉界面功能的实现情况。接口可以参考apps\web-antd\src\api\multimedia文件夹中的接口实现。重点：1、请特别注意抽屉文件的实现方式，要求代码规范，逻辑清晰。2、请注意图片布局中的内容，就比如左侧是转写内容 ，左边上面上说话人，右边是摘要和笔记，右边下面是RAG问答等等。技术栈：Vben5、vue3、antd、tailwind css等来实现。



你可以参考apps\web-antd\src\api\multimedia文件夹中的接口实现。



建议将新的抽屉组件拆分为以下模块：

  文件结构：
  recording-detail-drawer.vue  # 主抽屉组件
  ├── TranscriptionPanel.vue   # 左侧转录面板
  ├── SummaryPanel.vue         # 右侧摘要面板
  ├── ChatPanel.vue            # RAG对话面板
  └── AudioPlayer.vue          # 音频播放器组件

  功能模块：
  1. 转录模块

    - 说话人管理（调用speaker API）
    - 转录文本编辑
    - 时间戳同步
    - 音频播放控制
  2. 摘要模块

    - AI摘要生成和编辑
    - 笔记管理
    - 标签管理
  3. RAG对话模块

    - 使用 chatWithRecordingApi 单录音对话
    - 对话历史管理
    - 消息输入和发送



| 配置项  | 写法模式           | 条件判断 | 管理器             | 优先级支持 | 健康追踪 | 日志详细度            | 默认值处理   |
| ------- | ------------------ | -------- | ------------------ | ---------- | -------- | --------------------- | ------------ |
| 代理    | 管理器 + 动态注册  | ✅ if     | ✅ ProxyManager     | ✅ HIGH/LOW | ✅        | ⭐⭐⭐ (priority+source) | 在管理器中   |
| UA      | 管理器 + 动态注册  | ✅ if     | ✅ UserAgentManager | ✅ HIGH/LOW | ✅        | ⭐⭐⭐ (priority+source) | 在管理器中   |
| 延迟    | 管理器 + 动态注册  | ✅ if     | ✅ RequestScheduler | ✅ HIGH/LOW | ❌        | ⭐⭐ (只显示值)         | 在管理器中   |
| 请求头  | 直接赋值           | ✅ if     | ❌                  | ❌          | ❌        | ⭐ (只显示域名)        | 在 Helper 中 |
| Cookies | 直接赋值           | ✅ if     | ❌                  | ❌          | ❌        | ⭐⭐ (显示 keys)        | 在 Helper 中 |
| 重试    | 直接赋值（无判断） | ❌        | ❌                  | ❌          | ❌        | ⭐ (只显示值)          | 在 Helper 中 |
| 超时    | 条件判断 + 回退    | ✅ if     | ❌                  | ❌          | ❌        | ⭐⭐ (显示转换)         | 在代码中     |



  httpx 的实际使用情况

| 模块                           | 使用场景                | httpx 使用            |
| ------------------------------ | ----------------------- | --------------------- |
| web_smart_download.py          | Playwright 渲染完整网页 | ❌ 不使用 httpx        |
| feed_fetcher.py - RSSFetcher   | 获取 RSS XML            | ✅ 使用 httpx（104行） |
| feed_fetcher.py - JSONFetcher  | 获取 JSON API           | ✅ 使用 httpx（296行） |
| feed_fetcher.py - XPathFetcher | 获取 HTML 页面          | ❌ 使用 Playwright     |
| feed_fetcher.py - HTMLFetcher  | 获取 HTML 页面          | ❌ 使用 Playwright     |



  统一字段规范表

| 配置类型   | 必需字段   | 可选字段           | 支持多值 | 示例                                      |
| ---------- | ---------- | ------------------ | -------- | ----------------------------------------- |
| proxy      | url        | username, password | ✅        | [{"url": "socks5://192.168.20.23:50022"}] |
| user_agent | value      | -                  | ✅        | [{"value": "Mozilla/5.0..."}]             |
| headers    | key, value | -                  | ✅        | [{"key": "Referer", "value": "..."}]      |
| cookies    | value      | -                  | ❌        | [{"value": "session_id=abc; token=xyz"}]  |
| delay      | value      | -                  | ❌        | [{"value": 5.0}]                          |
| retry      | value      | -                  | ❌        | [{"value": 3}]                            |
| timeout    | value      | -                  | ❌        | [{"value": 30}]                           |





方案一:轻量级 - 即席爬取服务(推荐)

  在现有架构基础上添加一个独立的 即席爬取(Ad-hoc Crawl) 模块:

  backend/app/dynamic_monitor/
  ├── service/
  │   ├── adhoc_crawler.py           # 新增:即席爬取服务
  │   ├── feed_fetcher.py             # 现有:订阅源获取器
  │   └── ...
  ├── api/v1/
  │   └── adhoc/                      # 新增:即席爬取API
  │       └── adhoc.py
  └── model/
      └── adhoc_crawl_task.py         # 新增:即席任务模型(可选)

  核心设计:
  - 复用现有的下载器(PlaywrightDownloader, HttpxDownloader)
  - 复用现有的内容提取器(ArticleContentExtractor)
  - 提供 REST API,接受临时爬取请求
  - 可选:记录爬取历史到数据库

  优点:
  - 复用现有基础设施,工作量小
  - 与订阅源系统解耦,互不影响
  - 灵活性高,适合临时需求



  推荐方案：JSONB 字段 + 元数据

  表结构设计

  CREATE TABLE adhoc_crawl_result (
      id BIGINT PRIMARY KEY AUTO_INCREMENT,
      uuid VARCHAR(64) UNIQUE NOT NULL COMMENT '结果唯一标识',
      task_name VARCHAR(255) COMMENT '任务名称(如"京东iPhone价格监控")',
      url VARCHAR(768) NOT NULL COMMENT '爬取的URL',

      -- 核心：用JSONB存储提取的数据
      extracted_data JSONB NOT NULL COMMENT '提取的结构化数据',
    
      -- 元数据
      data_hash VARCHAR(64) COMMENT '数据指纹(用于去重)',
      created_by VARCHAR(64) COMMENT '创建人',
    
      -- 可选：原始数据引用
    html_minio_id: Mapped[str | None] = mapped_column(UniversalText, default=None, comment='HTML内容存储在MinIO的ID')
    snapshot_full_minio_id: Mapped[str | None] = mapped_column(UniversalText, default=None, comment='HTML内容存储在MinIO的完整截图ID')
    snapshot_viewport_minio_id: Mapped[str | None] = mapped_column(UniversalText, default=None, comment='HTML内容存储在MinIO的视口截图ID')
    pdf_minio_id: Mapped[str | None] = mapped_column(UniversalText, default=None, comment='HTML内容存储在MinIO的PDF ID')
    
      -- 索引
      INDEX idx_task_time (task_name, crawl_time),
      INDEX idx_url_time (url, crawl_time),
      INDEX idx_created_by (created_by)
  );



  方案B：两步走（更灵活）

  # 步骤1：预览URL
  POST /api/v1/adhoc/preview-urls
  {...}
  # 返回：将要爬取的URL列表

  # 步骤2：确认爬取
  POST /api/v1/adhoc/crawl
  {
      "urls": [...],
      "extraction_rules": [...]
  }
  优点：用户可以确认URL，避免误爬
  缺点：需要两次请求


  1. URL发现策略（核心）

  class UrlDiscoveryStrategy(Enum):
      """URL发现策略"""
      SINGLE = "single"                # 单个URL，直接爬取
      LIST = "list"                    # 手动提供URL列表
      LIST_PAGE = "list_page"          # 从列表页提取链接
      PAGINATION = "pagination"        # 分页列表
      URL_PATTERN = "url_pattern"      # URL规则生成
      RECURSIVE = "recursive"          # 递归爬取
      
      
      



根据我的需求，给出一个完整的解决方案，可以适当进行优化。

根据person_website.excel中的网站信息，登录谷歌首页，在搜索框输入高级搜索语句：biography site:{domain} filetype:pdf，替换site中的地址为excel中的网站地址，首先将所有搜索结果中的pdf链接保存在下来，需要翻页进行遍历；然后再使用合适工具读取这些链接，这些链接在浏览器打开都是pdf文件，将这些文件保存在以单位命名的文件夹下。



biography site:{domain} filetype:pdf





[

 "[{\"auto_id\":\"1fc0921177fa4c0d807453ac715b6d73\",\"channel_name\":\"塞尔维亚快乐电视台_首页\",\"channel_url\":\"http://www.happytv.tv\",\"channel_url_md5\":\"43fff168eb1779f88613c0e71cc2e754\",\"channel_url_sta\":\"happytv.tv\",\"comments_count\":0,\"content\":"","",\"country\":\"\",\"crawler_time\":\"2025-12-30 05:24:00\",\"data_source\":\"TRS-JW\",\"domain\":\"happytv.tv\",\"domain_pre\":\"happytv.tv\",\"file_info\":\"[]\",\"host\":\"happytv.tv\",\"image_info\":\"[]\",\"language\":\"155\",\"md5\":\"b50c94cd251e7d5f4e375b186245a3f0\",\"nation_category\":\"1\",\"pic_info\":\"\",\"pubtime\":\"2025-12-29 19:45:06\",\"pubtime_local\":\"2025-12-29 19:45:06\",\"pubtime_str\":\"*2025-12-29T19:45:06 **2025-12-30 05:23:49\",\"reprint_from_url\":\"\",\"repub\":\"\",\"screenshot_info\":\"\",\"screenshot_video\":\"\",\"serviceid\":0,\"site_name\":\"塞尔维亚快乐电视台\",\"subchannel_name\":\"\",\"time_type\":0,\"title\":\"NE PROPUSTITE „ĆIRILICU“ NA HAPPY TV: Rekapitulacija geostrateškog puta za 2025. godinu\",\"type\":\"\",\"update_time\":\"2025-12-30 05:24:00\",\"url\":\"https://happytv.rs/televizija/ne-propustite-cirilicu-na-happy-tv-rekapitulacija-geostrateskog-puta-za-2025-godinu/887168/\",\"user_description\":\"\",\"user_name\":\"\",\"user_profile_img_url\":\"\",\"user_url\":\"\",\"video_info\":\"\"},...]

 "07f67afb0da247d0a397ef5fd53aa124",

 "0",

 "gshx",

 "json",

 "news_channel",

 "utf-8",

 "",

 109,

 1767043600561,

 "{\"id\":109,\"publickey\":\"WPupOowt8jtu01AJyBYMXg==\",\"type\":1}",

 "[]"

]





一、热度排名追踪

  当前问题

  cl_luo 的 dm_article 表只记录 published_at（发布时间）和 created_time（入库时间），没
  有任何排名/热度随时间变化的追踪能力。一篇文章抓下来之后，热度信息就丢失了。

  TrendRadar 的做法

  两张表配合：

  news_items      → 文章主体，存 current rank
  rank_history    → 每次抓取时的 (news_item_id, rank, crawl_time)

  运行时重建为 rank_timeline: [{"time": "09:30", "rank": 1}, {"time": "10:00", "rank":
  0}, ...]，其中 0/None 表示下榜。

  cl_luo 的适配方案

  cl_luo 的数据源不是"热搜榜"而是 RSS/XPath/JSON/HTML 订阅源，没有天然的"排名"概念。但可
  以追踪的是文章在源站的存在状态和位置变化——本质上是"信息源中的可见度追踪"。

  方案：新增 dm_article_visibility_log 表

  class ArticleVisibilityLog(Base):
      """文章可见度变化日志"""
      __tablename__ = 'dm_article_visibility_log'

      id: Mapped[id_key]
      article_uuid: Mapped[str] = mapped_column(String(64), index=True)
      feed_uuid: Mapped[str] = mapped_column(String(36), index=True)
      crawl_time: Mapped[datetime] = mapped_column(TimeZone)
      position: Mapped[int | None]          # 在 feed 列表中的位置，None=下榜
      is_visible: Mapped[bool]              # 本次抓取是否仍在列表中
      importance_score: Mapped[float | None] # 本次 LLM 评分（可选）

  数据采集时机： 在 dm_dispatcher_crawler.py 的 do_one_feed_logic 中，步骤
  2（过滤重复）目前直接丢弃已存在 URL。改为：

  已存在的文章 → 不重新下载/分析，但记录一条 visibility_log（position=当前位置,
  is_visible=True）
  本次未出现的旧文章 → 记录 visibility_log（position=None, is_visible=False）
  新文章 → 正常流程 + 记录第一条 visibility_log

  这比 TrendRadar 更有价值的地方： TrendRadar 追踪的是热搜榜排名（纯数字），cl_luo
  可以追踪文章在信息源中的持续存在时长 + 位置变化 + LLM
  重要性评分变化，形成更立体的热度曲线。

  在 dm_article 表新增汇总字段：

  # 在 Article 模型中增加
  visibility_count: Mapped[int | None]          # 出现在抓取结果中的次数
  first_seen_at: Mapped[datetime | None]        # 首次出现时间
  last_seen_at: Mapped[datetime | None]         # 最后出现时间
  peak_position: Mapped[int | None]             # 历史最高位置（数字越小越靠前）
  visibility_trend: Mapped[str | None]          #
  趋势标记：rising/stable/falling/delisted

  改造量评估： 新增 1 个模型 + 修改 1 个模型 + 修改 do_one_feed_logic
  中的去重逻辑。不影响现有流程。

---
  二、宏观态势 AI 分析（五维框架）

  当前问题

  cl_luo 的 LLM 分析是单篇文章级别的：

  # llm.py 中 sem_async_chat 对每篇文章独立做 4 次调用
  article = await async_chat(article, "summary",    source_key="_original_content")
  article = await async_chat(article, "keywords",   source_key="_original_content")
  article = await async_chat(article, "importance",  source_key="_original_content")
  article = await async_chat(article, "categories",  source_key="_original_content")

  每篇文章得到独立的摘要/关键词/重要性/分类，但没有跨文章的宏观分析——无法回答"今天整体态
  势如何？有什么异常信号？"

  TrendRadar 的五维框架
  维度: core_trends
  分析目标: 跨平台热点主线 + 微观证据
  数据输入: 全部文章标题+排名+平台
  ────────────────────────────────────────
  维度: sentiment_controversy
  分析目标: 情绪光谱 + 核心矛盾
  数据输入: 全部文章标题
  ────────────────────────────────────────
  维度: signals
  分析目标: 时间维度（排名轨迹异动）+ 空间维度（跨平台共振）
  数据输入: 排名时间线
  ────────────────────────────────────────
  维度: rss_insights
  分析目标: 专业源 vs 大众热搜的信息差
  数据输入: RSS 文章 vs 热搜文章
  ────────────────────────────────────────
  维度: outlook_strategy
  分析目标: 面向不同角色的研判建议
  数据输入: 上述四维分析结果
  cl_luo 的适配方案

  核心思路： 在现有单篇分析之上，新增一个聚合分析层（Aggregate
  Analysis），定时/按需对一个时间窗口内的文章做跨源综合研判。

  新增 service：macro_analysis_service.py

  class MacroAnalysisService:
      """宏观态势分析服务"""

      async def analyze(
          self,
          time_window_hours: int = 24,
          feed_uuids: list[str] | None = None,
      ) -> MacroAnalysisResult:
          # 1. 查询时间窗口内的文章（带 visibility_log）
          # 2. 按 feed 源/分类/关键词 分组
          # 3. 构建输入文本
          # 4. 调用 LLM 做五维分析
          # 5. 存储分析结果

  五维框架适配为 cl_luo 的场景：
  TrendRadar 原始维度: core_trends（跨平台热点）
  cl_luo 适配维度: 核心态势：跨信息源的主题聚类和关联
  适配原因: cl_luo 的"平台"是不同 feed 源
  ────────────────────────────────────────
  TrendRadar 原始维度: sentiment_controversy（舆论争议）
  cl_luo 适配维度: 舆情风向：正面/负面/争议性内容识别
  适配原因: 保留，与 14 个安全领域结合
  ────────────────────────────────────────
  TrendRadar 原始维度: signals（异动弱信号）
  cl_luo 适配维度: 异动检测：新出现的高频主题、突然消失的持续话题、可见度急变
  适配原因: 结合 visibility_log 数据
  ────────────────────────────────────────
  TrendRadar 原始维度: rss_insights（RSS 深度洞察）
  cl_luo 适配维度: 信息源差异：不同类型源（官媒 vs 自媒体 vs 技术源）的视角差异
  适配原因: 利用 feed 的 category 分组
  ────────────────────────────────────────
  TrendRadar 原始维度: outlook_strategy（研判建议）
  cl_luo 适配维度: 研判建议：按安全领域分类的风险提示和关注建议
  适配原因: 结合现有的 14 安全领域 prompt
  输入数据构建（关键）：

  TrendRadar 的输入格式非常值得借鉴，每条数据包含：

  - [来源] 标题 | 排名:X-Y | 时间:HH:MM~HH:MM | 出现:N次 |
    轨迹:1(09:30)→0(10:00)→2(10:30)

  cl_luo 适配后的格式：

  - [feed名称/分类] 标题 | 重要性:0.85 | 关键词:AI,芯片 | 首现:09:30 持续:3次 |
    位置变化:2→1→1→下榜

  这样 LLM 一次调用就能拿到全局信息，而不是一篇篇独立分析。

  分析结果模型：

  class MacroAnalysisResult(Base):
      """宏观态势分析结果"""
      __tablename__ = 'dm_macro_analysis'

      id: Mapped[id_key]
      uuid: Mapped[str] = mapped_column(String(64), unique=True)
      analysis_time: Mapped[datetime] = mapped_column(TimeZone)
      time_window_start: Mapped[datetime] = mapped_column(TimeZone)
      time_window_end: Mapped[datetime] = mapped_column(TimeZone)
      article_count: Mapped[int]                    # 分析覆盖的文章数
      feed_count: Mapped[int]                       # 涉及的信息源数
    
      core_trends: Mapped[str | None]               # 核心态势
      sentiment_direction: Mapped[str | None]        # 舆情风向
      anomaly_signals: Mapped[str | None]            # 异动检测
      source_divergence: Mapped[str | None]          # 信息源差异
      outlook_strategy: Mapped[str | None]           # 研判建议
    
      model_used: Mapped[str | None]                 # 使用的模型
      token_consumed: Mapped[int | None]             # 消耗的 token 数

  触发方式：

  - Celery Beat 定时任务（如每 6 小时一次）
  - API 手动触发（用于即时分析）
  - 与现有单篇分析并行，不影响抓取流程

  Prompt 工程的关键借鉴点：

  TrendRadar 的 prompt 中有几个设计值得直接采用：

  1. 角色定义：高级情报分析师，带 4 个思维模型（见微知著/交叉验证/反直觉/结构化）
  2. 轨迹量化解读指南：明确告诉 LLM "排名数字变小=热度上升"、"0=下榜"、"回榜=新发展"
  3. 跨源特征：5+ 源出现=全面扩散，1-2 源=圈层热点
  4. 输出约束：纯 JSON 字符串值、\n 换行、禁止 Markdown/emoji、【标签】 做结构分隔

---
  三、关键词分组过滤

  当前问题

  cl_luo 的分类完全依赖 LLM 输出（CATEGORIES_PROMPT 返回 10 个固定分类之一）。用户无法自
  定义"我关注哪些主题"、"哪些关键词属于同一组"、"排除哪些内容"。

  TrendRadar 的关键词系统

  [半导体与芯片]
  半导体 芯片 晶圆              ← 必选词（全部出现才匹配）
  | 台积电 | 英伟达 | ASML      ← 可选词（任一出现即匹配）
  !广告 !推广                    ← 排除词
  /\bEUV\b/ => EUV光刻          ← 正则+显示名

  cl_luo 的适配方案

  新增两个模型：

  class KeywordGroup(Base):
      """关键词分组"""
      __tablename__ = 'dm_keyword_group'

      id: Mapped[id_key]
      uuid: Mapped[str] = mapped_column(String(64), unique=True)
      name: Mapped[str] = mapped_column(String(100))           #
  分组名，如"半导体与芯片"
      user_uuid: Mapped[str] = mapped_column(String(36), index=True)  # 创建者
      is_global: Mapped[bool] = mapped_column(default=False)   # 是否全局可用
      priority: Mapped[int] = mapped_column(default=0)         # 排序优先级
      is_enabled: Mapped[bool] = mapped_column(default=True)


  class KeywordRule(Base):
      """关键词规则"""
      __tablename__ = 'dm_keyword_rule'

      id: Mapped[id_key]
      group_uuid: Mapped[str] = mapped_column(String(64),
  ForeignKey('dm_keyword_group.uuid'))
      rule_type: Mapped[str]    # required / optional / exclude / regex
      pattern: Mapped[str]      # 关键词或正则表达式
      display_name: Mapped[str | None]  # 正则的显示名（如 "EUV光刻"）

  与现有系统的集成点：

  关键词过滤不应替代 LLM 分类，而是作为用户视角的筛选层叠加在上面：

  抓取 → LLM单篇分析(summary/keywords/importance/categories)
                              ↓
                关键词分组匹配（对 title + keywords + summary 做匹配）
                              ↓
                标记 article 命中了哪些 keyword_group
                              ↓
                宏观分析时按 keyword_group 分组输入

  新增关联表：

  class ArticleKeywordMatch(Base):
      """文章-关键词分组匹配记录"""
      __tablename__ = 'dm_article_keyword_match'

      id: Mapped[id_key]
      article_uuid: Mapped[str] = mapped_column(String(64), index=True)
      group_uuid: Mapped[str] = mapped_column(String(64), index=True)
      matched_field: Mapped[str]     # title / keywords / summary
      matched_pattern: Mapped[str]   # 命中的具体规则

  匹配引擎（新增 keyword_matcher.py）：

  class KeywordMatcher:
      def __init__(self, groups: list[KeywordGroup]):
          self._compiled = self._compile_groups(groups)

      def match(self, article: dict) -> list[MatchResult]:
          """对文章的 title + keywords + summary 做匹配"""
          text = f"{article.get('title','')} {article.get('keywords','')}
  {article.get('summary','')}"
          results = []
          for group in self._compiled:
              # 1. 检查排除词 → 命中则跳过
              # 2. 检查必选词 → 全部出现才通过
              # 3. 检查可选词 → 任一出现即通过
              # 4. 检查正则 → 匹配即通过
          return results

  调用时机： 在 save_articles_to_db 之后，对新入库文章批量跑一次匹配，写入
  dm_article_keyword_match。

  对宏观分析的价值：

  有了关键词分组后，宏观分析的输入可以从"全量文章"变为"按关注主题分组的文章"，输入文本格
  式变为：

  ## 半导体与芯片（12篇）
  - [TechCrunch] TSMC reports record Q4... | 重要性:0.92 | 持续:5次
  - [新华社] 国产光刻机取得突破... | 重要性:0.88 | 持续:3次

  ## 地缘政治（8篇）
  - [Reuters] US-China trade talks resume... | 重要性:0.95 | 持续:7次

  这比不分组的全量输入，能让 LLM 产生更结构化、更有针对性的分析。

---
  三者的协同关系

                      ┌──────────────┐
                      │  抓取流程     │  现有能力，不变
                      │  (dispatcher) │
                      └──────┬───────┘
                             │
                ┌────────────┼────────────┐
                ▼            ▼            ▼
       ┌────────────┐ ┌───────────┐ ┌──────────────┐
       │ 单篇AI分析  │ │ 可见度日志 │ │ 关键词匹配    │
       │ summary    │ │ position  │ │ group match  │
       │ keywords   │ │ trend     │ │              │
       │ importance │ │           │ │              │
       │ categories │ │           │ │              │
       └─────┬──────┘ └─────┬─────┘ └──────┬───────┘
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                   ┌─────────────────┐
                   │   宏观态势分析    │   新能力
                   │   (五维框架)     │
                   │                 │
                   │  输入 = 分组文章  │
                   │  + 可见度轨迹    │
                   │  + 单篇分析结果  │
                   └─────────────────┘

  三个功能不是独立的——可见度追踪为宏观分析提供趋势数据，关键词分组为宏观分析提供结构化输
  入，五维分析消费前两者的结果产出最终研判。建议按 可见度追踪 → 关键词分组 → 宏观分析
  的顺序逐步实现，每一步都可以独立交付使用。



# 搜索质量优化 P1 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 在 P0（相关性排序、降噪、日志）基础上，升级 BM25 DSL、修正多查询融合策略、为查询扩展添加质量门禁。

**Architecture:** 仅修改 `es_search.py` 和 `es_query_expansion.py`；不改 mapping、不重建索引、不引入新依赖。

**Tech Stack:** FastAPI, Elasticsearch (IK analyzer, ik_smart), Python asyncio

**版本号：** 实现前向用户确认（不得自行递增）

------

## 背景（P0 已完成）

- `sort_by` 默认已改为 `_score`
- `RERANK_ENABLED` / `QUERY_EXPANSION_ENABLED` 默认已关闭
- 搜索链路日志已就位

------

## Task 1: 升级关键词搜索 DSL

**文件：** `backend/app/dynamic_monitor/service/search/es_search.py` **位置：** `_keyword_search()` 函数，约第 314 行

**问题：** 当前 DSL 只有一层 `multi_match best_fields`，无法区分"标题精确短语命中"与"摘要单词散点命中"；长查询（如"中美贸易关税影响"）只需 1 个词命中就能排名靠前，导致无关文档上榜。

**方案：** 保留 `multi_match` 在 `must`（保证召回），加 `match_phrase` 在 `should`（精确命中时加分），长查询在 `multi_match` 加 `minimum_should_match: '2'`（要求至少 2 词命中）。

**Step 1: 替换 `_keyword_search` 函数体内的 query 构建**

将原来的 `body` 中 `'query'` 部分（约第 325-340 行）从：



```python
body: dict[str, Any] = {
    'query': {
        'bool': {
            'must': [
                {
                    'multi_match': {
                        'query': q,
                        'fields': ['title^3', 'keywords^2', 'summary^1.5', 'description', 'site_title'],
                        'type': 'best_fields',
                        'analyzer': 'ik_smart',
                    },
                },
            ],
            'filter': filters,
        },
    },
    ...
}
```

改为：



```python
# 长查询（3词及以上）要求多词同时命中，避免单词散点召回
is_long_query = len(q.split()) >= 3
multi_match_clause: dict[str, Any] = {
    'query': q,
    'fields': ['title^3', 'keywords^2', 'summary^1.5', 'description', 'site_title'],
    'type': 'best_fields',
    'analyzer': 'ik_smart',
}
if is_long_query:
    multi_match_clause['minimum_should_match'] = '2'

body: dict[str, Any] = {
    'query': {
        'bool': {
            'must': [
                {'multi_match': multi_match_clause},
            ],
            'should': [
                # 标题短语精确命中时大幅加分（slop=1 允许词序微小错位）
                {'match_phrase': {'title': {'query': q, 'boost': 5.0, 'slop': 1}}},
            ],
            'filter': filters,
        },
    },
    'from': (page - 1) * page_size,
    'size': page_size,
    'sort': _build_sort(sort_by, sort_order),
    'highlight': _build_highlight(),
}
```

> **注意：** `should` 在有 `must` 的 `bool` 中不影响召回（文档不需要满足 `should`），只影响得分——标题短语命中的文档额外得到 5× boost。

**Step 2: 验证**

用以下两类查询测试：

- 短查询（1词，如"贸易"）：应正常召回，无 `minimum_should_match` 限制
- 长查询（3词，如"中美贸易摩擦"）：查看日志 `[ES Search] DONE ... total=...`，结果中标题含完整短语的文章应排在前面
- 边界：查询完全不相关的词（如"火星移民"），应返回 total=0 或极少结果

------

## Task 2: 多查询融合改为加权策略

**文件：** `backend/app/dynamic_monitor/service/search/es_search.py` **位置：** `_multi_query_search()` 函数，约第 166 行

**问题：** 当前对所有查询（原始 + 扩展）平等取最高分。扩展词召回的文档与原始查询召回的文档得分相同，扩展词误召回的结果可能顶到 Top3，用户看到跑题内容。

**方案：**

- `queries[0]` = 原始查询，权重 `1.0`（得分不变）
- `queries[1:]` = 扩展查询，权重 `0.5`（得分减半）
- 同一文档取加权后的最大值
- 高亮优先取原始查询（index=0）的结果

**Step 1: 重写 `_multi_query_search` 函数体**

将函数内的合并逻辑从（约第 189-215 行）：



```python
# 合并去重
merged_scores: dict[str, float] = {}
merged_highlights: dict[str, dict] = {}
max_total = 0
total_took_ms = 0

for result in results:
    max_total = max(max_total, result['total'])
    total_took_ms += result['took_ms']
    for uuid in result['uuids']:
        score = result['scores'].get(uuid, 0.0)
        if uuid not in merged_scores or score > merged_scores[uuid]:
            merged_scores[uuid] = score
        if uuid not in merged_highlights and uuid in result['highlights']:
            merged_highlights[uuid] = result['highlights'][uuid]
```

改为：



```python
# 加权融合：原始查询 1.0，扩展查询 0.5
ORIGINAL_WEIGHT = 1.0
EXPANSION_WEIGHT = 0.5

merged_scores: dict[str, float] = {}
merged_highlights: dict[str, dict] = {}
total_took_ms = 0

for i, result in enumerate(results):
    weight = ORIGINAL_WEIGHT if i == 0 else EXPANSION_WEIGHT
    total_took_ms += result['took_ms']
    for uuid in result['uuids']:
        weighted = result['scores'].get(uuid, 0.0) * weight
        if uuid not in merged_scores or weighted > merged_scores[uuid]:
            merged_scores[uuid] = weighted
        # 高亮优先取原始查询（i=0）
        if i == 0 and uuid in result['highlights']:
            merged_highlights[uuid] = result['highlights'][uuid]
        elif uuid not in merged_highlights and uuid in result['highlights']:
            merged_highlights[uuid] = result['highlights'][uuid]
```

同时把 `total` 计算从 `len(merged_scores)` 改法保持不变（已是正确实现）。

同时删除原来不再用到的 `max_total` 变量（第 192 行和 196 行）。

**Step 2: 验证**

在 `.env` 中临时设置 `SEARCH_QUERY_EXPANSION_ENABLED=true`，搜索一个容易产生歧义的多词查询（如 `"中美 贸易 关系"`）。

- 日志中应出现 `expansion=True`
- 结果前几条标题应包含原始查询词，而非仅扩展词

------

## Task 3: 查询扩展质量门禁

**文件：** `backend/app/dynamic_monitor/service/search/es_query_expansion.py` **位置：** `expand_query()` 函数，约第 25 行

**问题：** 单字/双字短查询（如"AI"、"中美"）触发 LLM 扩展意义不大且容易扩散；LLM 返回的扩展词可能有重复、超长或与原始查询相同。

**方案：**

- 入口门禁：`len(stripped) < 4 OR len(words) < 2` → 直接返回 `[query]`，不调 LLM
- 出口过滤：扩展词长度 5–100 字符；去重（忽略大小写 + 首尾空格）；不与原始查询重复
- 数量上限：最终取前 `QUERY_EXPANSION_COUNT` 条

**Step 1: 替换 `expand_query` 函数**



```python
async def expand_query(query: str) -> list[str]:
    """将用户查询扩展为多个相关查询（带质量门禁）

    门禁规则：
    1. 短查询跳过（< 4 字符 或 < 2 词）
    2. 扩展词长度限制（5–100 字符）
    3. 去重（忽略大小写 / 首尾空格，不与原始查询重复）
    4. 数量上限（QUERY_EXPANSION_COUNT）

    Returns:
        [原始查询, ...扩展词]；门禁拦截或失败时返回 [query]
    """
    stripped = query.strip()
    words = stripped.split()
    if len(stripped) < 4 or len(words) < 2:
        log.debug(f'查询扩展跳过（查询过短）: {query!r}')
        return [query]

    try:
        from backend.database.db import async_db_session
        from backend.plugin.ai.schema.chat import AIChat
        from backend.plugin.ai.service.chat_service import ai_chat_service
        from backend.plugin.ai.utils.model_selector import select_model

        count = settings.SEARCH.QUERY_EXPANSION_COUNT
        system_prompt = EXPANSION_SYSTEM_PROMPT.format(count=count)

        async with async_db_session() as db:
            provider_id, model_id = await select_model(db, capability='text')
            chat = AIChat(
                provider_id=provider_id,
                model_id=model_id,
                system_prompt=system_prompt,
                user_prompt=stripped,
                temperature=settings.SEARCH.QUERY_EXPANSION_TEMPERATURE,
                max_tokens=500,
                timeout=float(settings.SEARCH.QUERY_EXPANSION_TIMEOUT),
            )
            result = await ai_chat_service.complete(db=db, chat=chat)
    except Exception as e:
        log.warning(f'查询扩展失败: {e}')
        return [query]

    raw_lines = [ln.strip() for ln in result.content.strip().splitlines() if ln.strip()]

    # 长度过滤（5–100 字符）
    length_ok = [ln for ln in raw_lines if 5 <= len(ln) <= 100]

    # 去重（不与原始查询重复，忽略大小写）
    seen: set[str] = {stripped.lower()}
    deduped: list[str] = []
    for ln in length_ok:
        key = ln.lower()
        if key not in seen:
            seen.add(key)
            deduped.append(ln)

    final = deduped[:count]
    log.debug(f'查询扩展完成: {query!r} -> {final}')
    return [query, *final]
```

**Step 2: 验证**

手动测试以下用例（可直接在 Python shell 中 `asyncio.run(expand_query(q))`，也可通过启动服务后搜索）：

| 输入             | 预期行为                                                     |
| ---------------- | ------------------------------------------------------------ |
| `"AI"`           | 返回 `["AI"]`（< 4 字符，跳过）                              |
| `"中美"`         | 返回 `["中美"]`（< 2 词，跳过）                              |
| `"中美贸易摩擦"` | 返回 `["中美贸易摩擦", ...扩展词]`，扩展词无重复、长度 5-100 |
| LLM 超时         | 返回 `["原始查询"]`（graceful fallback，不抛异常）           |

------

## Task 4: CHANGELOG 与 package.json 同步

**实现前：** 向用户确认版本号

**Files:**

- `/home/inProjects/cl_luo_front/apps/web-antd/src/views/dashboard/changelog/CHANGELOG.md`
- `/home/inProjects/cl_luo_front/apps/web-antd/package.json`

CHANGELOG 分类：

- `**IMPROVEMENTS**`：升级关键词搜索 DSL（`match_phrase` 标题短语 5× boost + 长查询 `minimum_should_match`）；多查询融合改为加权策略（原始查询 1.0、扩展查询 0.5）
- `**OTHERS**`：查询扩展新增质量门禁（短查询跳过、扩展词去重与长度过滤）

------

## 验收标准

| 检查点                                    | 预期结果                                                     |
| ----------------------------------------- | ------------------------------------------------------------ |
| 长查询（3词+）在无关字段仅有1词命中的文章 | 不在 top10 中出现                                            |
| 标题含完整查询短语的文章                  | 相比仅摘要命中的文章得分更高，排序更靠前                     |
| `expand_query("AI")`                      | 返回 `["AI"]`，无 LLM 调用                                   |
| 扩展后文章排序                            | 原始查询召回的文章排在仅扩展词召回的文章之前（可通过日志对比 scores 验证） |



| 4    | Critical  | `_multi_query_search` 第 2 页及以后：`fetch_total = page * page_size` 若结果集 < fetch_total，返回空列表 | 仅 expansion 开启时有影响，当前已关闭 |
| ---- | --------- | ------------------------------------------------------------ | ------------------------------------- |
| 5    | Critical  | `total` 返回 `len(merged_scores)`（本地 fetch 数），不是 ES 真实总数，前端分页失效 | 同上                                  |
| 6    | Important | `sorted(..., key=merged_scores.get)` 应改为 `lambda k: merged_scores[k]` | 当前不崩溃，但语义不严                |
| 7    | Minor     | `total_took_ms` 把并发请求时间相加，前端显示虚高延迟         | 展示问题，无功能影响                  |



| `playwright` → `patchright` 直接替换              | 高   | 极小（改导入） | 反检测能力提升 |
| ------------------------------------------------- | ---- | -------------- | -------------- |
| 为 Cloudflare 站点增加 `StealthyFetcher` 作为旁路 | 中   | 小             | 解决 CF 拦截   |
| 引入 `Selector` 替换部分 XPath 提取               | 低   | 中             | 自适应解析     |


Installation Complete


Kasm UI Login Credentials

------------------------------------
  username: admin@kasm.local
  password: HL6GxKWoixkS5
------------------------------------
  username: user@kasm.local
  password: Qz7tMsfu0xI4S
------------------------------------

Kasm Database Credentials
------------------------------------
  username: kasmapp
  password: qoP0kW1ZBZfK9M1X6Dhz
------------------------------------

Kasm Redis Credentials
------------------------------------
  password: 31LilvWNBNz1VfSs6tSE
------------------------------------

Kasm Manager Token
------------------------------------
  password: pOpFsPhVTCu4IM1bvXSM
------------------------------------

Service Registration Token
------------------------------------
  password: iZOQaUf2q2joorq6ZWZ2
------------------------------------

~~~
docker run -d -p 5000:5000 --name registry3 --restart=always -v /home/wlz/docker-registry/data:/var/lib/registry registry:3
~~~





