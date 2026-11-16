
**学习阶段：** Week7  
**学习日期：** 2026-11-16  
**学习状态：** 代码验收通过，待 Git 收尾

## 1. Token 是什么？

Token 是大语言模型处理文本时使用的基本单位。

Token 可能是：

- 一个汉字
    
- 一个英文单词
    
- 一个子词
    
- 一个字符
    
- 标点或其他文本符号
    

注意：Token 不等于字符，也不等于单词。

## 2. 字符、单词与 Token

|概念|示例|
|---|---|
|Character|a、b、你、好|
|Word|apple、hello|
|Token|字符、单词或子词等|

同一段文本经过不同 Tokenizer，可能产生不同的 Token 数量。

Python 的 len() 计算字符串字符数量，不代表真实 Token 数量。

## 3. Tokenization 处理流程

文本 → Token → Token ID → Embedding

- Tokenizer：负责切分文本。
    
- Token ID：Token 在词表中对应的整数编号。
    
- Embedding：将 Token ID 映射为向量。
    

## 4. Token 数量为什么重要？

1. API 成本：很多模型 API 按输入和输出 Token 计费。
    
2. 上下文长度：模型能够处理的 Token 数量存在限制。
    
3. 推理效率：Token 数量会影响计算量和生成耗时。
    

## 5. BPE 算法

BPE（Byte Pair Encoding）是一种常见的子词分词算法。

核心思想：

不断寻找出现频率最高的相邻符号对，将它们合并成新的符号。

基本过程：

1. 初始化文本符号。
    
2. 统计相邻符号对出现次数。
    
3. 找到频率最高的符号对。
    
4. 合并符号对。
    
5. 重复执行，逐渐构建词表。
    

示例：

原始文本：

- abab
    
- abac
    
- abab
    

字符对统计：

- ab：5 次
    
- ba：3 次
    
- ac：1 次
    

因此优先合并 ab。

## 6. Hugging Face Tokenizer 实践

使用 Transformers 加载 Qwen2.5-0.5B 的 Tokenizer。

```
from transformers import AutoTokenizer

qwen_tokenizer = AutoTokenizer.from_pretrained(
    "Qwen/Qwen2.5-0.5B"
)

sample_text = "我喜欢学习人工智能"

encoded_result = qwen_tokenizer(
    sample_text,
    add_special_tokens=False
)

token_id_list = encoded_result["input_ids"]

token_pieces = qwen_tokenizer.convert_ids_to_tokens(
    token_id_list
)

print(token_pieces)
print(token_id_list)
```

实际运行结果：

原始文本：我喜欢学习人工智能

Token IDs：

```
[109366, 100134, 104455]
```

Token 数量：3

注意：具体切分结果取决于 Tokenizer 和其词表。

## 7. Encode 与 Decode

常用操作：

|方法|作用|
|---|---|
|tokenizer()|文本编码|
|convert_ids_to_tokens()|ID 转 Token|
|decode()|Token ID 还原文本|

实践代码：

```
decoded_text = qwen_tokenizer.decode(token_id_list)

print(decoded_text)
print(decoded_text == sample_text)
```

运行结果：

```
我喜欢学习人工智能
True
```

说明编码和解码成功。

## 8. 本日知识总结

- 理解 Token 的概念
    
- 区分字符、单词和 Token
    
- 理解 Token ID
    
- 理解 Token 数量的意义
    
- 理解 BPE 基本原理
    
- 安装 Transformers
    
- 使用 Qwen Tokenizer
    
- 完成 Encode 和 Decode 实践
    

## 9. 下一步学习

Day45：Embedding（词嵌入）

学习内容：

1. 为什么需要 Embedding？
    
2. Token ID 如何变成向量？
    
3. Embedding 维度是什么意思？
    
4. PyTorch Embedding 层实践。
    

**本日总结：**

通过 Day44 的学习，我理解了大语言模型如何将自然语言转换成 Token ID，并成功使用 Qwen Tokenizer 完成实际编码与解码，为后续学习 Embedding 和 RAG 奠定基础。