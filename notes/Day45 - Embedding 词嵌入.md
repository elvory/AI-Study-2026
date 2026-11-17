
**学习阶段：** Week7  
**学习日期：** 2026-11-17  
**学习状态：** 代码验收通过

## 1. Embedding 是什么？

Embedding 是将离散的 Token ID 映射成连续向量的技术。

Token ID 本身只是词表中的索引，不直接表达语义。

基本流程：

文本 → Tokenization → Token ID → Embedding Vector

## 2. PyTorch Embedding 层

```
import torch
import torch.nn as nn

embedding_layer = nn.Embedding(6, 4)

sample_token_ids = torch.tensor([1, 3, 5])

embedded_vectors = embedding_layer(sample_token_ids)

print(embedded_vectors.shape)
```

输出：

```
torch.Size([3, 4])
```

参数说明：

- `num_embeddings`：词表大小
    
- `embedding_dim`：向量维度
    

Embedding 参数量：

**词表大小 × 向量维度**

例如：

`nn.Embedding(1000, 128)`

参数量为 128,000。

注意：Embedding 初始化时通常是随机权重，需要通过训练学习有用的表示。

## 3. Embedding 维度

Embedding 维度越大，表示容量通常越高，但参数数量和计算资源需求也会增加。

维度越大不代表模型效果一定越好。

## 4. Cosine Similarity（余弦相似度）

余弦相似度用于衡量两个向量的方向相似程度。

取值范围为 -1 到 1。

- 1：方向相同
    
- 0：方向正交
    
- -1：方向相反
    

PyTorch 实现：

```
import torch.nn.functional as F

similarity = F.cosine_similarity(
    apple_vec,
    banana_vec,
    dim=0
)
```

余弦相似度常用于 RAG 语义检索。

## 5. Token Embedding 与 Sentence Embedding

|类型|作用|
|---|---|
|Token Embedding|每个 Token 对应一个向量|
|Sentence Embedding|将整个句子映射为一个向量|

RAG 通常使用文本片段级 Embedding 进行向量检索。

真实语义检索需要使用经过训练的文本向量模型。

## 6. Top-K 向量检索

Top-K 的作用是选择相似度最高的 K 个候选结果。

```
retrieval_scores = torch.tensor([
    0.92, 0.35, 0.78, 0.85, 0.20
])

top_values, top_indices = torch.topk(
    retrieval_scores,
    k=2
)

print(top_values)
print(top_indices)
```

实际输出：

```
tensor([0.9200, 0.8500])
tensor([0, 3])
```

说明检索到了索引为 0 和 3 的两个文档。

## 7. 本日易错点

**变量引用错误**

第一次 Top-K 练习中误用了之前的 `similarities`，而不是当前练习的 `retrieval_scores`。

虽然程序可以正常运行，但输出不是期望结果。

解决方法：

- 使用语义明确的变量名称。
    
- 检查函数输入是否正确。
    
- 不仅检查程序是否报错，还要验证输出是否符合预期。
    

## 8. 本日总结

- 理解 Embedding 的基本原理
    
- 掌握 nn.Embedding
    
- 理解 Embedding 维度和参数量
    
- 掌握余弦相似度计算
    
- 理解 Sentence Embedding 的用途
    
- 使用 torch.topk 实现 Top-K 检索
    

**核心收获：**

理解了向量表示与相似度检索的基本原理，为后续学习真实 Embedding 模型、向量数据库和 RAG 系统打下基础。