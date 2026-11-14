# 

**学习阶段：** Week7  
**学习主题：** Transformer Architecture  
**学习日期：** 2026-11-14  
**学习状态：** 理论学习完成，代码待验收

## 1. Transformer 是什么？

Transformer 是一种基于 Attention（注意力机制）的深度学习架构。

2017 年论文《Attention Is All You Need》提出。

核心特点：

- 利用 Attention 建模不同 Token 之间的关系。
    
- 支持输入序列的并行处理。
    
- 是现代大语言模型的重要基础。
    

## 2. Encoder 和 Decoder

|架构|代表模型|主要用途|
|---|---|---|
|Encoder-only|BERT|文本理解|
|Decoder-only|GPT|文本生成|
|Encoder-Decoder|T5|文本转换任务|

GPT 使用 Decoder-only 架构，核心任务是根据之前的 Token 预测下一个 Token。

这个过程叫作自回归生成（Autoregressive Generation）。

## 3. Causal Mask（因果掩码）

作用：防止模型在预测当前位置时看到未来的 Token。

例如：

|Token|我|喜欢|学习|AI|
|---|---|---|---|---|
|我|1|0|0|0|
|喜欢|1|1|0|0|
|学习|1|1|1|0|
|AI|1|1|1|1|

1 表示可以关注，0 表示不能关注。

## 4. Q、K、V 注意力机制

|符号|英文|作用|
|---|---|---|
|Q|Query|查询信息|
|K|Key|匹配相关性|
|V|Value|提供实际信息|

计算公式：

Attention(Q,K,V) = Softmax(QKᵀ / √dₖ)V

计算流程：

1. Q 与 K 计算相关程度。
    
2. Softmax 转换为注意力权重。
    
3. 权重与 V 相乘。
    
4. 得到 Attention 输出。
    

记忆：Q 和 K 决定关注谁，V 决定获取什么信息。

## 5. Multi-Head Attention

多头注意力机制。

作用：让模型从不同角度学习 Token 之间的关系。

主要过程：

1. 将输入分别投影为多组 Q、K、V。
    
2. 多个 Attention Head 并行计算。
    
3. 拼接各个 Head 的输出。
    
4. 经过线性变换得到最终结果。
    

## 6. Feed Forward Network（FFN）

前馈神经网络。

作用：进一步加工每个 Token 的特征。

典型结构：

Input → Linear → GELU → Linear → Output

例如：

8 → 16 → GELU → 8

Attention 负责 Token 之间的信息交互，FFN 负责特征加工。

## 7. Residual Connection（残差连接）

残差连接公式：

y = F(x) + x

作用：

- 保留原始输入信息。
    
- 帮助梯度传播。
    
- 使深层神经网络更容易训练。
    

## 8. Layer Normalization（层归一化）

作用：对每个 Token 的特征进行归一化，帮助稳定模型训练。

基本公式：

y = (x - μ) / √(σ² + ε)

PyTorch 实现：

```
layer_norm = nn.LayerNorm(8)
output = layer_norm(input)
```

## 9. Transformer Block 完整结构

典型 GPT Pre-LN Decoder Block：

第一部分：

x' = x + Attention(LN(x))

第二部分：

y = x' + FFN(LN(x'))

主要组件：

- LayerNorm
    
- Masked Multi-Head Attention
    
- Residual Connection
    
- Feed Forward Network
    

多个 Transformer Block 堆叠，形成完整的 Transformer 模型主体。

## 10. GPT 整体处理流程

输入文本  
↓  
Tokenization  
↓  
Token Embedding + Position Information  
↓  
多个 Decoder Block  
↓  
Final LayerNorm  
↓  
Language Model Head  
↓  
预测下一个 Token

## 11. 本日核心知识检查

- 理解 Transformer 基本概念
    
- 理解 Encoder 和 Decoder
    
- 理解 Causal Mask
    
- 理解 Q、K、V
    
- 理解 Multi-Head Attention
    
- 理解 FFN
    
- 理解 Residual Connection
    
- 理解 Layer Normalization
    
- 理解 Transformer Block
    

## 12. 下一步学习

Day44：Tokenization（分词技术）

学习内容：

1. Token 的概念。
    
2. Token、字符和单词的区别。
    
3. BPE 分词算法。
    
4. Hugging Face Tokenizer 实践。
    

**本日总结：**

Transformer 是现代 LLM 的核心架构基础。理解了 Attention、FFN、残差连接和归一化之后，就能够进一步理解 GPT 等大语言模型的内部工作方式。