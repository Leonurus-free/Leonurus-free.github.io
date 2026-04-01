# CodeX CLI 使用指南

> 基于官方文档整理：https://developers.openai.com/codex/cli
>
> GitHub 仓库：https://github.com/openai/codex

## 目录

1. [安装与更新](#1-安装与更新)
2. [使用别名](#2-使用别名)
3. [快捷命令（Slash Commands）](#3-快捷命令slash-commands)
4. [键盘操作](#4-键盘操作)
5. [中断请求与退出会话](#5-中断请求与退出会话)
6. [通过 API 使用](#6-通过-api-使用)
7. [初始化项目指导文件（AGENTS.md）](#7-初始化项目指导文件agentsmd)
8. [切换模型与推理等级](#8-切换模型与推理等级)
9. [切换授权模式（权限）](#9-切换授权模式权限)
10. [网络搜索](#10-网络搜索)
11. [引用文件](#11-引用文件)
12. [输入图像](#12-输入图像)
13. [非交互模式（脚本功能）](#13-非交互模式脚本功能)
14. [会话恢复](#14-会话恢复)
15. [代码审查](#15-代码审查)
16. [Fork 会话](#16-fork-会话)
17. [Plan 模式](#17-plan-模式)
18. [上下文压缩](#18-上下文压缩)
19. [查看配置和 Token 用量](#19-查看配置和-token-用量)
20. [主题与语法高亮](#20-主题与语法高亮)
21. [提示词编辑器](#21-提示词编辑器)
22. [Shell 自动补全](#22-shell-自动补全)
23. [Feature Flags](#23-feature-flags)
24. [Multi-Agent（实验性）](#24-multi-agent实验性)
25. [Codex Cloud](#25-codex-cloud)
26. [MCP 集成](#26-mcp-集成)
27. [更多配置](#27-更多配置)
28. [实用技巧汇总](#28-实用技巧汇总)

---

## 1. 安装与更新

```bash
# 使用 npm 安装
npm install -g @openai/codex

# 使用 Homebrew 安装（macOS）
brew install --cask codex

# 升级到最新版
npm i -g @openai/codex@latest
```

安装后直接运行 `codex` 启动，首次会提示登录（ChatGPT 账号或 API Key）。

> Codex CLI 支持 macOS 和 Linux，Windows 支持为实验性，建议在 WSL 中使用。

---

## 2. 使用别名

通过配置别名，启动时自动带上常用参数，避免每次手动输入。

**临时生效（当前会话）：**

```bash
alias codex='codex -m gpt-5.3-codex -c model_reasoning_effort="high" -c model_reasoning_summary_format=experimental --search --dangerously-bypass-approvals-and-sandbox'
```

**永久生效（Mac / zsh）：**

```bash
echo "alias codex='codex -m gpt-5.3-codex -c model_reasoning_effort=\"high\" --search'" >> ~/.zshrc
source ~/.zshrc
```

---

## 3. 快捷命令（Slash Commands）

在 CodeX 中输入 `/` 可调出所有支持的快捷命令：

| 命令 | 说明 |
|------|------|
| `/model` | 切换模型和推理等级 |
| `/permissions` | 设置授权模式（原 `/approvals`，后者仍可用作 alias） |
| `/plan` | 切换到 Plan 模式，先规划再执行 |
| `/personality` | 设置回复风格（friendly / pragmatic / none） |
| `/review` | 对当前工作区发起代码审查 |
| `/new` | 开启新的会话 |
| `/resume` | 恢复一个已保存的会话 |
| `/fork` | 将当前会话 Fork 成一个新线程 |
| `/init` | 初始化 AGENTS.md 项目指导文件 |
| `/compact` | 压缩上下文，避免触发上下文长度限制 |
| `/diff` | 显示 git 差异（含未追踪文件） |
| `/mention` | 引用某个文件附加到会话 |
| `/status` | 显示当前会话配置和 Token 用量 |
| `/statusline` | 配置 TUI 底部状态栏显示内容 |
| `/mcp` | 列出当前已配置的 MCP 工具 |
| `/agent` | 切换多 Agent 线程（实验性） |
| `/apps` | 浏览并插入 ChatGPT 连接器（Apps） |
| `/experimental` | 开关实验性功能（如 Multi-agents） |
| `/ps` | 查看后台运行中的终端及其输出 |
| `/debug-config` | 打印配置层级诊断信息 |
| `/feedback` | 向 Codex 团队发送日志/反馈 |
| `/logout` | 退出登录 |
| `/quit` / `/exit` | 退出当前会话 |
| `/theme` | 打开主题选择器 |

> 注意：`/approvals` 已被 `/permissions` 取代，但仍可作为 alias 使用，不再出现在命令弹窗中。

---

## 4. 键盘操作

| 快捷键 | 功能 |
|--------|------|
| `Option + Enter` 或 `Control + J` | 快速换行（不提交） |
| `Ctrl + G` | 打开外部编辑器编辑长提示词（使用 `$VISUAL` 或 `$EDITOR` 环境变量指定的编辑器） |
| `Enter`（Codex 运行中） | 向当前任务注入新指令 |
| `Tab`（Codex 运行中） | 将下一条提示词加入队列 |
| `Esc`（双击，编辑框为空时） | 编辑上一条消息，连按可继续往前，按 Enter 从该位置 Fork |
| `@` | 在编辑框中触发模糊文件搜索 |
| `!` 前缀 | 直接运行本地 Shell 命令（如 `!ls`），输出结果返回给 Codex |
| `Up / Down` | 在编辑框中浏览历史草稿 |

---

## 5. 中断请求与退出会话

- **中断当前请求**：按 `ESC` 或 `Control + C`
- **退出会话**：再次按 `Control + C`，或输入 `/quit` 或 `/exit`

---

## 6. 通过 API 使用

无付费订阅账户可通过 API Key 方式使用 CodeX。

**修改配置文件** `~/.codex/config.toml`，添加：

```toml
preferred_auth_method = "apikey"
```

**CLI 临时切换（不修改配置文件）：**

```bash
# 切换到 API Key 认证
codex --config preferred_auth_method="apikey"

# 切换回 ChatGPT 默认认证
codex --config preferred_auth_method="chatgpt"
```

**API 定价参考：** https://openai.com/api/pricing/

---

## 7. 初始化项目指导文件（AGENTS.md）

`AGENTS.md` 是给 AI Agent 准备的项目说明文件，类似 README，用于提供项目上下文和行为指令，帮助 Codex 更准确地完成任务。

**初始化命令：**

```
/init
```

执行后会在项目根目录生成 `AGENTS.md` 文件（默认英文）。

**转换为中文：**

```
把 AGENTS.md 转换成中文
```

可以在任意子目录运行 `/init`，生成该子目录范围的指导文件。

详细说明参考：https://agents.md/

---

## 8. 切换模型与推理等级

Codex 默认使用 `gpt-5.3-codex` 模型（ChatGPT Pro 订阅者还可使用更快的 `gpt-5.3-codex-spark` 研究预览版）。

**通过命令切换：**

```
/model
```

**启动时通过参数指定：**

```bash
# 切换模型
codex --model gpt-5.3-codex
codex -m gpt-5.3-codex -c model_reasoning_effort="high"

# 指定推理总结格式（none | experimental）
codex -m gpt-5.3-codex -c model_reasoning_summary_format=experimental
```

> `model_reasoning_effort` 支持 `low` / `medium` / `high` 三档。

---

## 9. 切换授权模式（权限）

**通过命令切换：**

```
/permissions
```

**三种模式对比：**

| 权限项 | Auto（默认） | Read Only | Full Access |
|--------|-------------|-----------|-------------|
| 读取文件 | ✅ | ✅ | ✅ |
| 编辑文件 | ✅ | ❌ | ✅ |
| 在工作目录运行命令 | ✅ | ❌ | ✅ |
| 访问工作目录外文件 | ❌（需确认） | ❌ | ✅ |
| 访问网络 | ❌（需确认） | ❌ | ✅ |

**通过启动参数精细控制：**

| 模式 | 参数 | 说明 |
|------|------|------|
| 自动（默认） | 无需参数 | 读/编辑/工作目录命令，沙箱外需确认 |
| 只读 | `--sandbox read-only --ask-for-approval never` | 只能读取文件，不请求批准 |
| 自动编辑，不可信命令需批准 | `--sandbox workspace-write --ask-for-approval untrusted` | 读写文件，不可信命令需确认 |
| 危险完全访问 | `--dangerously-bypass-approvals-and-sandbox`（别名 `--yolo`） | 无沙箱、无批准（谨慎使用） |

---

## 10. 网络搜索

**默认行为（无需参数）：** Codex 的网络搜索默认已开启，使用 OpenAI 维护的**缓存索引**（预先抓取的结果），避免直接加载任意网页带来的 Prompt 注入风险。

**启用实时搜索：** 传递 `--search` 参数获取最新数据：

```bash
codex --search
```

或在配置文件中持久化：

```toml
web_search = "live"
```

**关闭网络搜索：**

```toml
web_search = "disabled"
```

> 注意：使用 `--yolo`（完全访问模式）时，网络搜索默认切换为实时结果。

---

## 11. 引用文件

**方式一：`@` 快速引用**

在编辑框中输入 `@`，会触发模糊文件搜索，按 Tab 或 Enter 选中后路径会插入到消息中：

```
@src/main.py 帮我优化这个函数
```

**方式二：`/mention` 命令**

```
/mention src/lib/api.ts
```

精准引用让 Codex 专注于目标文件，避免误改。

---

## 12. 输入图像

**方式一：直接粘贴**

将图片复制后，直接粘贴到 Codex 输入框中。

**方式二：CLI 参数附加**

```bash
# 附加单张图片
codex -i screenshot.png "解释一下这个错误"

# 附加多张图片（逗号分隔）
codex --image img1.png,img2.jpg "总结一下这些图表"
```

支持 PNG、JPEG 等常见格式。

---

## 13. 非交互模式（脚本功能）

使用 `exec` 子命令以非交互方式运行 Codex，适合集成到脚本或 CI 流程中：

```bash
codex exec "修复这个报错的问题"
```

加 `--json` 可输出结构化结果：

```bash
codex exec --json "检查代码质量"
```

也可以带初始 prompt 启动交互模式：

```bash
codex "请解释一下这个代码库"
```

---

## 14. 会话恢复

Codex 会自动将会话记录保存在本地（`~/.codex/sessions/`），支持随时恢复。

```bash
# 打开会话选择器，选择后恢复
codex resume

# 显示所有目录的会话（不只当前目录）
codex resume --all

# 直接恢复最近一次会话（当前目录）
codex resume --last

# 直接恢复最近一次（不限目录）
codex resume --last --all

# 恢复指定 Session ID
codex resume <SESSION_ID>
```

非交互模式也支持恢复：

```bash
codex exec resume --last "继续修复之前发现的竞态条件"
codex exec resume <SESSION_ID> "执行上次的计划"
```

**在交互会话中恢复：**

```
/resume
```

---

## 15. 代码审查

在交互会话中运行 `/review` 触发本地代码审查，Codex 会启动一个独立的审查 Agent，读取你指定的 diff 并给出优先级排序的建议，不会修改工作树。

```
/review
```

支持以下审查类型：

- **Review against a base branch** — 与指定分支比较，找出最大风险（适合 PR 前）
- **Review uncommitted changes** — 检查所有已暂存、未暂存、未追踪的变更
- **Review a commit** — 选择某个 commit SHA 进行审查
- **Custom review instructions** — 自定义审查角度（如"聚焦可访问性回归"）

可在 `config.toml` 中设置默认审查模型：

```toml
review_model = "gpt-5.3-codex"
```

---

## 16. Fork 会话

将当前会话 Fork 为一个新线程，保留原始记录的同时探索不同方向：

```
/fork
```

也可以在终端对已保存的会话进行 fork：

```bash
codex fork
```

---

## 17. Plan 模式

Plan 模式让 Codex 先提出执行方案，再开始实施，适合需要仔细评估步骤的任务：

```
/plan
```

支持附加初始提示词：

```
/plan 为这个服务设计一个迁移方案
```

> 任务运行中时 `/plan` 暂时不可用。可在 `config.toml` 中设置 Plan 模式默认推理等级：
> ```toml
> plan_mode_reasoning_effort = "high"
> ```

---

## 18. 上下文压缩

当上下文长度接近限制时，使用 `/compact` 压缩：

```
/compact
```

Codex 会用简洁的摘要替换早期对话，保留关键信息的同时释放上下文空间。

> 输入框下方会实时显示当前剩余的上下文长度。

---

## 19. 查看配置和 Token 用量

```
/status
```

显示内容包括：账户信息、当前模型、推理等级、授权模式、可写根目录、Token 使用量等。

**自定义底部状态栏显示：**

```
/statusline
```

可选项包括：model、model+reasoning、context stats、rate limits、git branch、token counters、session id、current directory、Codex version 等，配置持久化到 `config.toml`。

---

## 20. 主题与语法高亮

TUI 支持对代码块和 diff 进行语法高亮，使用 `/theme` 切换主题：

```
/theme
```

打开主题选择器，实时预览，选择后保存到 `~/.codex/config.toml` 的 `tui.theme` 字段。

支持自定义 `.tmTheme` 文件，放置在 `$CODEX_HOME/themes/` 目录下即可在选择器中使用。

---

## 21. 提示词编辑器

编写长提示词时，可以切换到系统默认编辑器：

- 按 `Ctrl + G` 打开 `$VISUAL` 或 `$EDITOR` 环境变量指定的编辑器
- 编辑完成保存退出后，内容自动回到 Codex 编辑框

---

## 22. Shell 自动补全

为你的 Shell 安装自动补全脚本：

```bash
codex completion bash
codex completion zsh
codex completion fish
```

以 zsh 为例，在 `~/.zshrc` 末尾添加：

```bash
eval "$(codex completion zsh)"
```

如果出现 `command not found: compdef` 错误，在上面那行前加：

```bash
autoload -Uz compinit && compinit
```

---

## 23. Feature Flags

Codex 内置部分实验性功能开关，可通过 `features` 子命令管理：

```bash
# 列出所有功能及其状态
codex features list

# 启用某个功能
codex features enable unified_exec

# 禁用某个功能
codex features disable shell_snapshot
```

更改会写入 `~/.codex/config.toml`（或通过 `--profile` 指定的配置文件）。

也可以在交互会话中通过 `/experimental` 命令开关实验性功能。

---

## 24. Multi-Agent（实验性）

通过 Multi-agent 模式并行处理复杂任务：

**启用方式：**

1. 在交互会话中输入 `/experimental`，开启 Multi-agents 功能后重启 Codex
2. 或通过 `codex features enable` 命令启用

**配置（`config.toml`）：**

```toml
[agents]
# 配置 agent 角色和参数
```

**切换 Agent 线程：**

```
/agent
```

详见官方文档：https://developers.openai.com/codex/multi-agent

---

## 25. Codex Cloud

在终端内管理和启动 Codex Cloud 任务，无需打开网页：

```bash
# 打开交互选择器（浏览/应用云端任务）
codex cloud

# 直接启动云端任务
codex cloud exec --env <ENV_ID> "总结当前未解决的 Bug"

# 启动多次尝试（1-4 次）获得最优解
codex cloud exec --env <ENV_ID> --attempts 3 "重构这个模块"
```

在交互选择器中按 `Ctrl+O` 选择环境，完成后可直接将结果 diff 应用到本地项目。

---

## 26. MCP 集成

### 配置 MCP

在 `~/.codex/config.toml` 中添加 `mcp_servers` 配置（TOML 格式）：

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
env = { "API_KEY" = "your-key" }

[mcp_servers.puppeteer]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-puppeteer"]
```

支持 STDIO 和 streaming HTTP 两种协议，Codex 启动时自动连接配置的 MCP Server。

### 查看 MCP 工具

```
/mcp
```

列出当前会话中所有可用的 MCP 工具。

### 验证连接

CodeX 暂无专用验证命令。启动时若 MCP Server 连接失败，会在控制台输出错误信息；无报错则表示集成正常。

### 使用 MCP

配置完成后，在提示词中直接调用对应工具：

```
请使用 context7 获取最新的 Java 25 switch 语法，并写一个示例
```

### Codex 作为 MCP Server

Codex 本身也可以作为 MCP Server 运行，供其他 Agent 调用：

详见：https://developers.openai.com/codex/guides/agents-sdk

---

## 27. 更多配置

所有偏好设置存储在：`~/.codex/config.toml`

**配置示例：**

```toml
model = "gpt-5.3-codex"

# 项目信任级别
[projects."/Users/XX/project1"]
trust_level = "trusted"

# 网络搜索模式（cached | live | disabled）
web_search = "cached"

# Plan 模式推理等级
plan_mode_reasoning_effort = "medium"

# 代码审查专用模型
review_model = "gpt-5.3-codex"
```

**启动时指定工作目录（无需 cd）：**

```bash
codex --cd /path/to/project
```

**指定多个可写根目录：**

```bash
codex --cd apps/frontend --add-dir ../backend --add-dir ../shared
```

**配置参考文档：**
- 基础配置：https://developers.openai.com/codex/config-basic
- 高级配置：https://developers.openai.com/codex/config-advanced
- 完整配置参考：https://developers.openai.com/codex/config-reference
- GitHub 配置文档：https://github.com/openai/codex/blob/main/docs/config.md

---

## 28. 实用技巧汇总

- **提前准备好环境**：启动 Codex 前激活 Python 虚拟环境、启动所需服务、导出环境变量，避免浪费 Token 在环境探测上
- **`@` 引用文件**：比 `/mention` 更快，输入 `@` 即可模糊搜索工作区文件
- **`!` 运行 Shell 命令**：在编辑框输入 `!ls`，结果会返回给 Codex 作为上下文
- **Enter 注入指令**：Codex 运行中按 Enter 可追加新指令到当前任务
- **Esc 双击编辑历史**：编辑框为空时连按 Esc 可回溯之前的消息，按 Enter 从该位置 Fork
- **`codex --cd <path>`**：无需 `cd` 直接在指定目录启动
- **`--add-dir`**：跨多个项目协调修改时，用于扩展可写根目录
- **`/diff` 随时审查**：提交前用 `/diff` 检查 Codex 的全部改动
- **`/compact` 节省 Token**：长会话中定期压缩上下文
- **用 `/fork` 探索分支**：不确定某个方向时，先 Fork 再实验，不影响主线

---

## 注意事项

- 使用 `--dangerously-bypass-approvals-and-sandbox`（`--yolo`）模式时请务必谨慎，该模式下 Codex 拥有完全不受限的操作权限，且网络搜索会切换为实时模式
- Web 搜索结果仍属于不受信任的内容，即使是缓存模式也需注意
- API 使用方式与 ChatGPT 订阅方式可随时切换，按需选择
- Windows 原生支持为实验性，推荐在 WSL 环境下使用
