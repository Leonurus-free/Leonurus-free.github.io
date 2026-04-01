### 相关参数说明：

## **--model**

- **说明**: 使用的Hugging Face模型名称或路径。
- **默认**: “facebook/opt-125m”

**--task**

- **说明**: 任务类型，支持的选项包括：auto, generate, embedding, embed, classify, score, reward, transcription。
- **默认**: “auto”

**--tokenizer**

- **说明**: 使用的Hugging Face分词器名称或路径。如果未指定，将使用模型名称或路径。

**--skip-tokenizer-init**

- **说明**: 跳过分词器和反分词器的初始化。

**--revision**

- **说明**: 使用的具体模型版本，可以是分支名、标签名或提交ID。未指定时将使用默认版本。

**--code-revision**

- **说明**: 使用的模型代码的具体修订版本。

**--tokenizer-revision**

- **说明**: 使用的Hugging Face分词器的修订版本。

**--tokenizer-mode**

- **说明**: 分词器模式，支持选项：auto, slow, mistral, custom。
- **默认**: “auto”

**--trust-remote-code**

- **说明**: 信任来自Hugging Face的远程代码。

**--allowed-local-media-path**

- **说明**: 允许API请求从指定的服务器文件系统目录读取本地图像或视频。此选项存在安全风险，仅在可信环境中启用。

**--download-dir**

- **说明**: 下载和加载权重的目录，默认为Hugging Face的默认缓存目录。

**--load-format**

- **说明**: 加载模型权重的格式，支持选项：auto, pt, safetensors, npcache, dummy, tensorizer, sharded_state, gguf, bitsandbytes, mistral, runai_streamer。
- **默认**: “auto”

**--config-format**

- **说明**: 加载模型配置的格式，支持选项：auto, hf, mistral。
- **默认**: “auto”

**--dtype**

- **说明**: 模型权重和激活的数值类型，支持选项：auto, half, float16, bfloat16, float, float32。
- **默认**: “auto”

**--kv-cache-dtype**

- **说明**: kv缓存存储的数据类型，支持选项：auto, fp8, fp8_e5m2, fp8_e4m3。
- **默认**: “auto”

**--max-model-len**

- **说明**: 模型上下文长度。如果未指定，将自动从模型配置中推导。

**--guided-decoding-backend**

- **说明**: 默认使用的引导解码引擎，支持选项：outlines-dev/outlines, mlc-ai/xgrammar, noamgat/lm-format-enforcer。
- **默认**: “xgrammar”

**--logits-processor-pattern**

- **说明**: 可选的正则表达式模式，指定有效的logits处理器名称。

**--model-impl**

- **说明**: 使用的模型实现，支持选项：auto, vllm, transformers。
- **默认**: “auto”

**--distributed-executor-backend**

- **说明**: 用于分布式模型工作者的后端，支持选项：ray, mp, uni, external_launcher。

**--pipeline-parallel-size, -pp**

- **说明**: 管道阶段的数量。
- **默认**: 1

**--tensor-parallel-size, -tp**

- **说明**: 张量并行副本的数量。
- **默认**: 1

**--max-parallel-loading-workers**

- **说明**: 在多个批次中顺序加载模型，以避免RAM OOM（内存不足）。

**--ray-workers-use-nsight**

- **说明**: 如果指定，则使用nsight对Ray工作者进行性能分析。

**--block-size**

- **说明**: 连续token块的大小，支持选项：8, 16, 32, 64, 128。

**--enable-prefix-caching, --no-enable-prefix-caching**

- **说明**: 启用或禁用自动前缀缓存。

**--disable-sliding-window**

- **说明**: 禁用滑动窗口，限制为滑动窗口大小。

**--num-lookahead-slots**

- **说明**: 实验性调度配置，必要用于投机解码。

**--seed**

- **说明**: 操作的随机种子。
- **默认**: 0

**--swap-space**

- **说明**: 每个GPU的CPU交换空间大小（GiB）。
- **默认**: 4

**--cpu-offload-gb**

- **说明**: 每个GPU的CPU卸载空间（GiB）。默认为0，表示不卸载。

**--gpu-memory-utilization**

- **说明**: 用于模型执行的GPU内存占用比例，范围从0到1。
- **默认**: 0.9

**--num-gpu-blocks-override**

- **说明**: 如果指定，忽略GPU分析结果并使用此数量的GPU块。

**--max-num-batched-tokens**

- **说明**: 每次迭代的最大批处理token数量。

**--max-num-partial-prefills**

- **说明**: 对于分块预填充，最大并发部分预填充的数量。
- **默认**: 1

**--max-long-partial-prefills**

- **说明**: 对于分块预填充，最大并发预填充的长请求数量。
- **默认**: 1

**--long-prefill-token-threshold**

- **说明**: 对于分块预填充，如果请求的长度超过此token数量，则视为长请求。
- **默认**: 0

**--max-num-seqs**

- **说明**: 每次迭代的最大序列数量。

**--max-logprobs**

- **说明**: 返回的最大log概率数量。
- **默认**: 20

**--disable-log-stats**

- **说明**: 禁用日志统计。

**--quantization, -q**

- **说明**: 用于量化权重的方法，支持多种选项。

**--rope-scaling**

- **说明**: RoPE缩放配置，使用JSON格式。

**--rope-theta**

- **说明**: RoPE theta，与rope_scaling一起使用。

**--hf-overrides**

- **说明**: Hugging Face配置的额外参数，以JSON字符串格式传递。

**--enforce-eager**

- **说明**: 始终使用急切模式的PyTorch。

**--max-seq-len-to-capture**

- **说明**: CUDA图覆盖的最大序列长度。

**--disable-custom-all-reduce**

- **说明**: 见ParallelConfig。

**--tokenizer-pool-size**

- **说明**: 用于异步分词的分词器池大小。默认为0，表示使用同步分词。

**--tokenizer-pool-type**

- **说明**: 用于异步分词的分词器池类型。默认为“ray”。

**--tokenizer-pool-extra-config**

- **说明**: 分词器池的额外配置，以JSON字符串格式传递。

**--limit-mm-per-prompt**

- **说明**: 对于每个多模态插件，限制每个提示允许的输入实例数量。

**--mm-processor-kwargs**

- **说明**: 多模态输入映射/处理的覆盖参数。

**--disable-mm-preprocessor-cache**

- **说明**: 如果为真，则禁用多模态预处理器/映射器的缓存。

**--enable-lora**

- **说明**: 如果为真，启用LoRA适配器的处理。

**--enable-lora-bias**

- **说明**: 如果为真，启用LoRA适配器的偏置。

**--max-loras**

- **说明**: 单个批次中LoRA的最大数量。
- **默认**: 1

**--max-lora-rank**

- **说明**: 最大LoRA秩。
- **默认**: 16

**--lora-extra-vocab-size**

- **说明**: LoRA适配器中可以存在的额外词汇的最大大小。
- **默认**: 256

**--lora-dtype**

- **说明**: LoRA的数据类型，支持选项：auto, float16, bfloat16。
- **默认**: “auto”

**--long-lora-scaling-factors**

- **说明**: 指定多个缩放因子以允许同时使用多个LoRA适配器。

**--max-cpu-loras**

- **说明**: 存储在CPU内存中的LoRA最大数量。

**--fully-sharded-loras**

- **说明**: 启用完全分片的LoRA计算。

**--enable-prompt-adapter**

- **说明**: 如果为真，启用PromptAdapters的处理。

**--max-prompt-adapters**

- **说明**: 批次中PromptAdapters的最大数量。
- **默认**: 1

**--max-prompt-adapter-token**

- **说明**: 最大PromptAdapters token数量。
- **默认**: 0

**--device**

- **说明**: vLLM执行的设备类型，支持选项：auto, cuda, neuron, cpu, openvino, tpu, xpu, hpu。
- **默认**: “auto”

**--num-scheduler-steps**

- **说明**: 每个调度器调用的最大前向步骤。
- **默认**: 1

**--multi-step-stream-outputs**

- **说明**: 如果为假，则多步骤将在所有步骤结束时流式输出。
- **默认**: True

**--scheduler-delay-factor**

- **说明**: 在调度下一个提示之前应用延迟（延迟因子乘以前一个提示延迟）。

**--enable-chunked-prefill**

- **说明**: 如果设置，预填充请求可以根据max_num_batched_tokens进行分块。

**--speculative-model**

- **说明**: 在投机解码中使用的草稿模型名称。

**--speculative-model-quantization**

- **说明**: 投机模型权重的量化方法。

**--num-speculative-tokens**

- **说明**: 在投机解码中从草稿模型采样的投机token数量。

**--speculative-disable-mqa-scorer**

- **说明**: 如果设置为真，则在投机中禁用MQA评分器。

**--speculative-draft-tensor-parallel-size, -spec-draft-tp**

- **说明**: 投机解码中草稿模型的张量并行副本数量。

**--speculative-max-model-len**

- **说明**: 草稿模型支持的最大序列长度。

**--speculative-disable-by-batch-size**

- **说明**: 如果排队请求的数量超过此值，则禁用新请求的投机解码。

**--ngram-prompt-lookup-max**

- **说明**: 在投机解码中，ngram提示查找的最大窗口大小。

**--ngram-prompt-lookup-min**

- **说明**: 在投机解码中，ngram提示查找的最小窗口大小。

**--spec-decoding-acceptance-method**

- **说明**: 在投机解码中使用的接受方法，支持选项：rejection_sampler, typical_acceptance_sampler。
- **默认**: “rejection_sampler”

**--typical-acceptance-sampler-posterior-threshold**

- **说明**: 设置接受的后验概率的下限阈值。

**--typical-acceptance-sampler-posterior-alpha**

- **说明**: 接受样本中基于熵的阈值的缩放因子。

**--disable-logprobs-during-spec-decoding**

- **说明**: 如果设置为真，则在投机解码期间不返回token的log概率。

**--model-loader-extra-config**

- **说明**: 模型加载器的额外配置，以JSON字符串格式传递。

**--ignore-patterns**

- **说明**: 加载模型时要忽略的模式，默认为original/**/*。

**--preemption-mode**

- **说明**: 预占模式，支持选项：recompute, swap。

**--served-model-name**

- **说明**: 在API中使用的模型名称。如果提供多个名称，服务器将响应任何提供的名称。

**--qlora-adapter-name-or-path**

- **说明**: QLoRA适配器的名称或路径。

**--show-hidden-metrics-for-version**

- **说明**: 启用自指定版本以来隐藏的过时Prometheus指标。

**--otlp-traces-endpoint**

- **说明**: 发送OpenTelemetry跟踪的目标URL。

**--collect-detailed-traces**

- **说明**: 收集详细跟踪的模块，选项包括：model, worker, all。

**--disable-async-output-proc**

- **说明**: 禁用异步输出处理。

**--scheduling-policy**

- **说明**: 调度策略，支持选项：fcfs（先到先服务），priority（优先级）。
- **默认**: “fcfs”

**--scheduler-cls**

- **说明**: 使用的调度器类。

**--override-neuron-config**

- **说明**: 覆盖或设置神经设备配置。

**--override-pooler-config**

- **说明**: 覆盖或设置池化模型的池化方法。

**--compilation-config, -O**

- **说明**: 模型的torch.compile配置。

**--kv-transfer-config**

- **说明**: 分布式KV缓存传输的配置。

**--worker-cls**

- **说明**: 用于分布式执行的工作者类。
- **默认**: “auto”

**--generation-config**- **说明**: 生成配置的文件夹路径。

**--override-generation-config**- **说明**: 以JSON格式覆盖或设置生成配置。

**--enable-sleep-mode**- **说明**: 启用引擎的睡眠模式（仅支持cuda平台）。

**--calculate-kv-scales**- **说明**: 启用动态计算kv缓存的k_scale和v_scale。

**--additional-config**- **说明**: 指定平台的额外配置，以JSON格式传递。