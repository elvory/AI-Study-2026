import torch

# Query 向量
query_vec = torch.tensor([1.0, 0.0])

# 三个 Key 向量
key_matrix = torch.tensor([
    [1.0, 0.0],
    [0.0, 1.0],
    [0.8, 0.2]
])

# 计算注意力分数
attention_scores = query_vec @ key_matrix.T

print("Attention Scores:", attention_scores)



# softmax 转换成能够表示关注程度的注意力权重
# 特点：
# 将每个分数转换为 0～1 之间的权重。
# 所有权重加起来等于 1。


# 将 Attention Scores 转换为权重
attention_weights = torch.softmax(
    attention_scores,
    dim=0
)

print("Attention Weights:", attention_weights)

# 检查权重之和
print("权重之和:", attention_weights.sum().item())



# Day46：Attention 加权求和

value_vectors = torch.tensor([
    [10.0, 0.0],
    [0.0, 20.0]
])

value_weights = torch.tensor([0.8, 0.2])

# 根据注意力权重计算输出
weighted_output = value_weights @ value_vectors  #这里的 @ 执行向量与矩阵的乘法，得到加权求和后的向量。

print("Attention Output:", weighted_output)



# Day46：Scaled Attention

# Key 向量维度
key_dim = key_matrix.shape[-1]

# 缩放注意力分数
scaled_scores = attention_scores / (key_dim ** 0.5)

print("原始分数：", attention_scores)
print("缩放分数：", scaled_scores)



## 综合练习:实现 Scaled Dot-Product Attention
# 三个Value向量，与前面的三个key对应
final_value_matrix = torch.tensor([
    [10.0,0.0],
    [0.0,20.0],
    [8.0,2.0]
])

# Step 1 和 Step 2 已经完成
# scaled_scores 是之前计算的缩放分数

# Step 3：转换成注意力权重
final_weights = torch.softmax(
    scaled_scores,
    dim=0
)

# Step 4：加权求和
final_output  = final_weights @ final_value_matrix

print("注意力权重：",final_weights)
print("最终输出：",final_output)
