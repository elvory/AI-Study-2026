import torch
import torch.nn as nn

# 创建 Embedding 层
embedding_layer = nn.Embedding(
    num_embeddings=6,
    embedding_dim=4
)


# 输入 Token ID
sample_token_ids = torch.tensor([1, 3, 5])

# 转换成向量
embedded_vectors = embedding_layer(sample_token_ids)

print("Token IDs：", sample_token_ids)
print("Embedding 向量：")
print(embedded_vectors)

print("输出形状：", embedded_vectors.shape)


# 比较不同 Embedding 的参数数量

embedding_small = nn.Embedding(1000, 64)
embedding_large = nn.Embedding(1000, 256)

print("Small 参数量：",
      embedding_small.weight.numel())

print("Large 参数量：",
      embedding_large.weight.numel())


# Cosine Similarity（余弦相似度）
import torch.nn.functional as F

# 定义三个示例向量
apple_vec = torch.tensor([1.0, 0.0])
banana_vec = torch.tensor([0.8, 0.6])
car_vec = torch.tensor([0.0, 1.0])

# 计算余弦相似度
sim_fruit = F.cosine_similarity(
    apple_vec, banana_vec, dim=0
)

sim_car = F.cosine_similarity(
    apple_vec, car_vec, dim=0
)

print("苹果与香蕉：", sim_fruit.item())
print("苹果与汽车：", sim_car.item())




# Token Embedding 与 Sentence Embedding
# 模拟三个文档向量
document_vectors = torch.tensor([
    [1.0, 0.0],
    [0.0, 1.0],
    [0.8, 0.6]
])

# 模拟用户问题向量
query_vector = torch.tensor([1.0, 0.0])

# 计算问题与所有文档的余弦相似度
similarities = F.cosine_similarity(
    query_vector.unsqueeze(0),
    document_vectors,
    dim=1
)

print("相似度：", similarities)

# 找出最相似的文档
best_index = torch.argmax(similarities).item()

print("最相似的文档索引：", best_index)




# Top-K 向量检索
# Day45 综合练习：Top-K 检索

retrieval_scores = torch.tensor([
    0.92, 0.35, 0.78, 0.85, 0.20
])

# TODO：使用 torch.topk 取出最高的两个分数
top_values, top_indices = torch.topk(retrieval_scores , k=2)

print("Top-2 相似度：", top_values)
print("Top-2 文档索引：", top_indices)
