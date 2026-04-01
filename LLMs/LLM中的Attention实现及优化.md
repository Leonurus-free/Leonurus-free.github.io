# LLM中的Attention实现及优化

# Multi-Head Attention

![图片](./LLM中的Attention实现及优化/640.webp)

MHA 原理示意图

Attention的计算复杂度与文本长度的二次方成正比，相关的计算过程如下。

1.Embedding lookup table: 输入文本长度为n（n个token），经过embedding table后，每一个token返回一个大小为（1, d）的向量，d对应embedding的维度大小。对于长度为n的文本，embedding table给出embedding matrix矩阵$X$大小为(n, d)

2.MHA （Multi head Attention）:

- • 作用：MHA (Multi Head Attention layer)的目标在于重构文本中的token的embedding表示，重构的出发点在于(1)考虑context中token的语义相关性（2）token的位置相关性（通过position embedding 体现）。
- • 映射计算：embedding matrix X 进入MHA后，会并行处理h个head的attention layer。处理过程如下，X通过线性映射为h个head，得到Attention heads的Q、K、V。对应的维度信息为Q(h, n, k)、K(h, n, k) 和V(h, n, v)，其中hk=hv=O(d)。实现过程相当于X（n, d）与h个维度为（d, k）、(d, k)和（d, v）的矩阵相乘得到，对应的时间复杂为$O(hndk)=O(nd^2)$ 。矩阵相乘(a, b)(b, c)的时间复杂度为$O(abc)$ ，h对应矩阵个数也就是head个数。
- • Attention计算：简单来讲，n个token每个都要与其他token进行Attention的计算，时间复杂度为 O(n^2) 。详细的计算过程为： QK转置相乘(经过 Softmax 归一)然后与V相乘，获取最终的embedding。Q(h, n, k)、K(h, n, k)计算复杂度为$O(hnkn)=O(n^2hk)=O(nd^2)$ 。attention score维度为(h,n,n)，与V(h, n, v)相乘的时间复杂度为$O(hnnv)=O(n^2hv)=O(nd^2)$ 

通过上述分析可以看出MHA的整体复杂度为$O(n^2d)+O(nd^2)$。

MHA的整体复杂度与context 长度 n的二次方成正比，与模型的规模d(embedding size)的二次方成正比。

增大context的长度，会带来计算复杂度的二次方增大。

# Attention实现机制优化

### Multi-Query Attention (MQA)

对于multi-head attention，每个head对应的k矩阵和v矩阵不同，所以对于每个token都有h（head数目）个k矩阵和v矩阵。

在模型推理的过程中，为了防止重新计算，会缓存之前token对应的Keys和Values。因此GPU显存占用会随着预测的token数目而增加。

Multi-Query Attention 通过在不同head中共享K和V，即不同的head具有相同的key和value，降低了存储的k矩阵和v矩阵的数目，对于每个token存储的matrix数目由2h个，降低为两个matrix。同事也降低了计算复杂度。

Multi-Query Attention极大的提高了推理速度。

Group Query Attention

![图片](./LLM中的Attention实现及优化/640-1736078110843-3.webp)

Group Query Attention是对所有head的Query分组为不同的group，对一个group内的query，共享key和value。GQA的效果与MHA的效果相当，训练速度与MQA相当，提高了训练速度的同时，效果相比MQA有提高。

### GQA 的实现

![图片](./LLM中的Attention实现及优化/640-1736078117907-6.webp)

```python
# init时k和v用self.num_key_value_heads * self.head_dim初始化，当self.num_key_value_heads小于self.num_heads时，参数量变少
self.q_proj = nn.Linear(self.hidden_size, self.num_heads * self.head_dim, bias=False)
self.k_proj = nn.Linear(self.hidden_size, self.num_key_value_heads * self.head_dim, bias=False)
self.v_proj = nn.Linear(self.hidden_size, self.num_key_value_heads * self.head_dim, bias=False)

# forward时，通过repeat_kv方法，将hidden states 从(batch, num_key_value_heads, seqlen, head_dim) 变成 (batch, num_attention_heads, seqlen, head_dim)，相当于是复制了self.num_key_value_groups份
self.num_key_value_groups = self.num_heads // self.num_key_value_heads

key_states = key_states.view(bsz, q_len, self.num_key_value_heads, self.head_dim).transpose(1, 2)
value_states = value_states.view(bsz, q_len, self.num_key_value_heads, self.head_dim).transpose(1, 2)

key_states = repeat_kv(key_states, self.num_key_value_groups)
value_states = repeat_kv(value_states, self.num_key_value_groups)
```

### 内存开销计算

使用 MHA 结构的自回归模型，在推理过程中，会维护一个巨大的 k/v cache。它的内存开销公式为：

```
batch * max_seq_len * n_heads * head_dim * sizeof(half) * 2
```

而对于 GQA 来说，k/v cache 的内存开销公式变成：

```
batch * max_seq_len * n_kv_heads * head_dim * sizeof(half) * 2
```

n_heads / n_kv_heads 就是 group 的大小。可见，使用 GQA 可以把 k/v cache 降低到 MHA的1/group 的水平。非常利好 Attention 这种访存密集型的计算。

### SWA (Sliding Window Attention)

通过优化attention的实现，降低attention与context length的长度依赖关系。这种对attention结构的优化，会同时提升训练和推理的性能。

sliding window attention 将计算复杂度由变为$O(n^2)=O(n)$。

**注意力的时间复杂度是序列长度的二次方，空间复杂度是序列长度的一次方**。在推理时，由于缓存的可用性降低，会造成更高的延迟和更小的吞吐量。为了减少这样的问题，提出了窗口注意力机制，在每一个注意力层每个token最多能注意前W个token。

![图片](./LLM中的Attention实现及优化/640-1736078128533-9.webp)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HrMQ8SF1ApcoiadjPg1EDJPQBGaiaGhvC0wEv96ia5zmfumOuzP9vHdXuicF49JQBlaI8FJGpscWpmCBo78qqCsfvA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

注意力的传递通过层数的增加而向后传递。每一层注意力层，信息可以传递W tokens。经过两层注意力层，信息可以传递2W tokens。比如对于16k 序列长度和4k的滑动窗口，通过4层，信息可以实现整个序列长度的传递。因此序列越长，在滑动窗口长度固定的情况下，为了实现整个序列长度的传递，需要的注意力层数越多。

# Attention底层实现优化

### FlashAttention

FlashAttention 解决attention计算过程中，频繁访问HBM的问题，将attention计算block化，直接在SRAM中进行。

在GPU中底层对算子的优化，会同时提升模型的训练和推理性能。考虑到Attention在GPU的计算过程以及GPU的结构，优化Attention在GPU中的实现。

GPU中的两个核心部分，SRAM运算速度快但是存储量小，HBM运算速度慢但是存储量大。GPU中的operation运算过程，是从HBM拷贝数据进行运算，完成运算后再将数据存储到HBM.

![图片](./LLM中的Attention实现及优化/640-1736078156442-12.webp)

FlashAttention通过以下两个操作实现了attention的加速实现。

- • 1.利用了GPU中存储的差异性。将数据从HBM拷贝到SRAM中，计算时从SRAM中读取数据，SRAM相比HBM读取和写入速度更快。
- • 2.SRAM相比HBM速度快，但是存储量小，因此采用分块block的形式计算QK的矩阵乘法。即实现了并行block的softmax计算。为了保证分块block计算的softmax值与原有的softmax值不变，采用了block的 softmax计算。

FlashAttention将Q、K和V切分为block，进行block的计算，提高operation的处理速度。

![图片](./LLM中的Attention实现及优化/640-1736078158402-15.webp)

### PagedAttention

PagedAttention解决attention计算过程中的内存分配问题，防止内存的浪费，更好的分配内存，可以实现更大的batch size和吞吐量。

传统KV Cache存在的问题主要包括：

1.**显存占用大**：对于大型模型如LLaMA-13B中的单个序列，KV Cache可能占用高达1.7GB的内存。

2.**动态变化**：KV Cache的大小取决于序列长度，而序列长度具有高度可变和不可预测的特点，这对有效管理KV Cache构成挑战。

3.**内存碎片化和过度预留**：由于显存碎片和过度预留，现有系统浪费了60%-80%的显存。

4.**内部碎片化：在静态批处理策略下，一个请求结束后，其剩余的空间就被浪费掉了**。

5.**外部碎片化**：由于KV Cache是一个巨大的矩阵，且**必须占用连续内存**，操作系统如果**只分配大的连续内存，势必有很多小的内存空间被浪费掉**

### PagedAttention 的优势

相当于小空间内存的动态分配，可以实现非连续的内存存储，解决了传统KV Cache连续动态内存分配造成的内存空间浪费。