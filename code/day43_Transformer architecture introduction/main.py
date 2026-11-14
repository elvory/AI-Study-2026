# Transformer 的基本处理流程（概念演示）

steps = [
    "Tokenization",
    "Embedding",
    "Positional Encoding",
    "Transformer Blocks",
    "Output Layer"
]


# GPT 使用GPT 使用 Decoder-only


# Masked Self-Attention（带掩码的自注意力）
# Causal Mask（因果掩码）
for index, step in enumerate(steps, start=1):
    print(f"步骤{index}: {step}")

tokens = ["我", "喜欢", "学习", "AI"]

for i in range(len(tokens)):
    mask = []

    for j in range(len(tokens)):
        if j <= i:
            mask.append(1)
        else:
            mask.append(0)

    print(tokens[i], mask)







import torch

# Query
q_vec = torch.tensor([1.0, 0.0])

# Key
k_vecs = torch.tensor([
    [1.0, 0.0],
    [0.0, 1.0],
    [0.8, 0.2]
])

# Value
v_vecs = torch.tensor([
    [10.0, 0.0],
    [0.0, 20.0],
    [8.0, 2.0]
])

# 计算相关程度
scores = q_vec @ k_vecs.T

# 转换为注意力权重
weights = torch.softmax(scores, dim=0)

# 加权提取信息
output = weights @ v_vecs

print("注意力分数：", scores)
print("注意力权重：", weights)
print("最终输出：", output)





import torch
import torch.nn as nn

# 创建多头注意力
multihead_attn = nn.MultiheadAttention(
    embed_dim=8,
    num_heads=2,
    batch_first=True
)

# 模拟输入数据
hidden_states = torch.randn(1, 4, 8)

# 执行自注意力
attn_output, attn_weights = multihead_attn(
    hidden_states,
    hidden_states,
    hidden_states
)

print("输入形状：", hidden_states.shape)
print("输出形状：", attn_output.shape)
print("注意力权重：", attn_weights.shape)





# 创建前馈神经网络
ffn = nn.Sequential(
    nn.Linear(8, 16),
    nn.GELU(),
    nn.Linear(16, 8)
)   #简化

# 模拟输入
token_features = torch.randn(1, 4, 8)

# FFN 处理
ffn_output = ffn(token_features)

print("输入形状：", token_features.shape)
print("输出形状：", ffn_output.shape)



# Residual Connection（残差连接）
import torch

# 原始输入
residual_input = torch.tensor([1.0, 2.0, 3.0])

# 模拟网络层输出
residual_branch = torch.tensor([0.5, 0.5, 0.5])

# 残差连接
residual_output = residual_input + residual_branch

print("原始输入：", residual_input)
print("网络输出：", residual_branch)
print("残差输出：", residual_output)





# Layer Normalization（层归一化）
import torch
import torch.nn as nn

# 创建 LayerNorm
layer_norm = nn.LayerNorm(8)

# 模拟输入数据
norm_input = torch.randn(1, 4, 8)

# 执行归一化
norm_output = layer_norm(norm_input)

print("输入形状：", norm_input.shape)
print("输出形状：", norm_output.shape)

# 检查每个 Token 的特征均值
print("归一化后的均值：")
print(norm_output.mean(dim=-1))
