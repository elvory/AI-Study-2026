import torch

# 模拟模型输出的 Logits（原始分数）
next_token_logits = torch.tensor([2.0, 1.0, 0.5])

# 转换为概率
next_token_probs = torch.softmax(
    next_token_logits,
    dim=0
)

# 选择概率最高的 Token
predicted_token_id = torch.argmax(next_token_probs)

print("预测概率：", next_token_probs)
print("预测 Token 索引：", predicted_token_id.item())




# Day47：Temperature 实验

temperature_logits = torch.tensor([2.0, 1.0, 0.5])

# 较低温度
low_temp_probs = torch.softmax(
    temperature_logits / 0.5,
    dim=0
)

# 较高温度
high_temp_probs = torch.softmax(
    temperature_logits / 2.0,
    dim=0
)

print("Temperature=0.5:", low_temp_probs)
print("Temperature=2.0:", high_temp_probs)



# Day47：Sampling 随机采样

sampling_probs = torch.tensor([0.7, 0.2, 0.1])

# 连续采样 5 次
for sample_index in range(5):
    sampled_token = torch.multinomial(
        sampling_probs,
        num_samples=1
    )

    print(
        f"第{sample_index + 1}次采样：",
        sampled_token.item()
    )

# Greedy Decoding（贪心解码）和 Sampling（采样）之间的基本区别



# Day47：Top-K Sampling

topk_probs = torch.tensor([
    0.4, 0.3, 0.15, 0.1, 0.05
])

# 保留概率最高的三个 Token
topk_values, topk_indices = torch.topk(
    topk_probs, k=3
)

# 重新归一化
topk_normalized = topk_values / topk_values.sum()

# 随机采样
topk_sample = torch.multinomial(
    topk_normalized, num_samples=1
)

# 获取原始 Token ID
selected_token = topk_indices[topk_sample]

print("保留的概率：", topk_values)
print("保留的索引：", topk_indices)
print("归一化概率：", topk_normalized)
print("采样 Token ID：", selected_token.item())


# Day47：Top-P Sampling

topp_probs = torch.tensor([
    0.4, 0.3, 0.15, 0.1, 0.05
])

# 按概率从大到小排序
sorted_probs, sorted_indices = torch.sort(
    topp_probs, descending=True
)

# 计算累计概率
cumulative_probs = torch.cumsum(
    sorted_probs, dim=0
)

# 保留累计概率首次达到阈值的 Token
keep_mask = (cumulative_probs - sorted_probs) < 0.8

# 获取保留的概率和索引
topp_values = sorted_probs[keep_mask]
topp_indices = sorted_indices[keep_mask]

# 重新归一化
topp_normalized = topp_values / topp_values.sum()

# 随机采样
topp_sample = torch.multinomial(
    topp_normalized, num_samples=1
)

print("累计概率：", cumulative_probs)
print("保留索引：", topp_indices)
print("采样 Token ID：",
      topp_indices[topp_sample].item())



# Day47：模拟模型推理
import torch.nn as nn

inference_model = nn.Linear(4, 3)

inference_input = torch.randn(1, 4)

# 切换到评估模式
inference_model.eval()

# 关闭梯度计算
with torch.no_grad():
    inference_output = inference_model(
        inference_input
    )

print("推理结果：", inference_output)
print("是否需要梯度：",
      inference_output.requires_grad)





# 模拟 SFT 训练数据
sft_samples = [
    {
        "instruction": "Python 如何创建列表？",
        "output": "使用 [] 创建列表。"
    },
    {
        "instruction": "什么是 Embedding？",
        "output": "将离散对象映射为向量的技术。"
    }
]

for sft_sample in sft_samples:
    print("指令：", sft_sample["instruction"])
    print("标准回答：", sft_sample["output"])






from transformers import AutoTokenizer

instruct_tokenizer = AutoTokenizer.from_pretrained(
    "Qwen/Qwen2.5-0.5B-Instruct"
)

chat_messages = [
    {
        "role": "system",
        "content": "你是一名Python编程老师。"
    },
    {
        "role": "user",
        "content": "什么是列表？"
    }
]

formatted_prompt = instruct_tokenizer.apply_chat_template(
    chat_messages,
    tokenize=False,
    add_generation_prompt=True
)

print(formatted_prompt)





# Day47 综合练习：模拟 LLM Token 生成

generation_logits = torch.tensor([
    3.0, 2.0, 1.5, 0.8, 0.2
])

generation_temperature = 0.7
generation_k = 3

# Step 1：Temperature 调节
adjusted_logits = generation_logits / generation_temperature

# Step 2：Softmax 转换为概率
generation_probs = torch.softmax(adjusted_logits , dim=0)

# Step 3：Top-K 筛选
candidate_probs, candidate_indices = torch.topk(generation_probs,generation_k)

# Step 4：重新归一化
normalized_probs = candidate_probs / candidate_probs.sum()

# Step 5：随机采样
sampled_index = torch.multinomial(normalized_probs , num_samples=1)

# 获取原始 Token ID
generated_token_id = candidate_indices[sampled_index]

print("原始分数：", generation_logits)
print("调整后概率：", generation_probs)
print("候选 Token ID：", candidate_indices)
print("归一化概率：", normalized_probs)
print("生成 Token ID：", generated_token_id.item())




# 独立复写训练
practice_logits = torch.tensor([
    1.0, 4.0, 0.5, 3.0, 2.0
])

practice_temperature = 0.8
practice_k = 3

# step 1
practice_tem = practice_logits / practice_temperature

# step 2
practice_probs = torch.softmax(practice_tem , dim=0)

# step 3
tk_probs,tk_indices = torch.topk(practice_probs , practice_k)

# step 4
nor_probs = tk_probs / tk_probs.sum()

# step 5
sam_index = torch.multinomial(nor_probs , num_samples=1)

# step 6
practice_Token_id = tk_indices[sam_index]

print("候选 Token ID：", tk_indices)
print("归一化概率：", nor_probs)
print("概率之和：", nor_probs.sum().item())
print("生成 Token ID：", practice_Token_id.item())
