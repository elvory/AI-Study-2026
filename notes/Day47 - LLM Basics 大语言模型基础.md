
**学习阶段：** Week7  
**学习日期：** 2026-11-24  
**学习状态：** 代码验收通过，待 Git 提交

## 1. Autoregressive Generation（自回归生成）

根据已有 Token 预测下一个 Token，并不断重复这个过程，最终生成完整文本。

基本流程：

输入文本 → Tokenization → Embedding → Transformer → Logits → Token 选择 → 继续生成

## 2. Logits 与 Softmax

- Logits：模型输出的原始预测分数。
    
- Softmax：将原始分数转换成概率分布。
    
- Argmax：获取最大值对应的索引。
    

```
probs = torch.softmax(logits, dim=0)
token_id = torch.argmax(probs)
```

## 3. Temperature（温度参数）

公式：

$$P=Softmax(Logits/T)$$

- 低温：概率分布更加集中。
    
- 高温：概率分布更加平缓。
    
- Temperature=1：保持原始概率分布。
    
- 温度本身不会产生随机性，需要配合采样。
    

```
adjusted_logits = logits / temperature
probs = torch.softmax(adjusted_logits, dim=0)
```

## 4. Greedy Decoding 与 Sampling

|方法|特点|
|---|---|
|Greedy Decoding|选择概率最高的 Token|
|Sampling|根据概率分布随机选择 Token|

```
# 贪心解码
token_id = torch.argmax(probs)

# 随机采样
sampled_index = torch.multinomial(
    probs, num_samples=1
)
```

## 5. Top-K Sampling

保留概率最高的 K 个 Token，然后重新归一化并进行随机采样。

```
values, indices = torch.topk(probs, k=3)
normalized = values / values.sum()
```

返回结果：

- values：筛选后的数值。
    
- indices：对应的原始索引。
    

## 6. Top-P Sampling

按照概率从大到小排序，保留累计概率首次达到或超过阈值的最小候选集合。

常用方法：

```
sorted_probs, sorted_indices = torch.sort(
    probs, descending=True
)

cumulative_probs = torch.cumsum(
    sorted_probs, dim=0
)
```

记忆口诀：

**Top-K 管数量，Top-P 管累计概率。**

## 7. Training 与 Inference

|对比|Training|Inference|
|---|---|---|
|模型参数|更新|不更新|
|反向传播|通常需要|不需要|
|目的|学习能力|使用模型能力|

```
model.eval()

with torch.no_grad():
    output = model(inputs)
```

注意：eval() 不会自动关闭梯度计算。

AI Programming Tutor 和 AlgoMentor AI 调用 DeepSeek API 生成 Hint，属于模型推理。

## 8. LLM 典型训练阶段

|阶段|作用|
|---|---|
|Pre-training|学习语言规律与基础知识|
|SFT|学习遵循指令|
|RLHF|使模型行为更符合人类偏好|

并不是所有模型都必须经过上述三个阶段。

## 9. Base Model 与 Instruct Model

- Base Model：基础模型，主要学习文本预测规律。
    
- Instruct Model：经过指令训练，更适合对话和 AI 应用开发。
    

Chat Template 用于将 system、user、assistant 等角色消息组织为模型需要的输入格式。

```
formatted_prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
```

## 10. 综合实践：Token Sampling

```
practice_logits = torch.tensor([
    1.0, 4.0, 0.5, 3.0, 2.0
])

practice_temperature = 0.8
practice_k = 3

# Step 1：温度调节
practice_tem = practice_logits / practice_temperature

# Step 2：概率转换
practice_probs = torch.softmax(
    practice_tem, dim=0
)

# Step 3：Top-K 筛选
tk_probs, tk_indices = torch.topk(
    practice_probs, practice_k
)

# Step 4：重新归一化
nor_probs = tk_probs / tk_probs.sum()

# Step 5：随机采样
sam_index = torch.multinomial(
    nor_probs, num_samples=1
)

# Step 6：映射原始 Token ID
practice_token_id = tk_indices[sam_index]

print(practice_token_id.item())
```

实际运行结果：

- 候选 Token ID：[1, 3, 4]
    
- 归一化概率：[0.7307, 0.2093, 0.0600]
    
- 概率之和：约 1
    
- 本次采样结果：1
    

## 11. 常用函数模板

|方法|用途|
|---|---|
|torch.softmax(x, dim=0)|概率转换|
|torch.argmax(x)|获取最大值索引|
|torch.topk(x, k)|筛选前 K 个元素|
|x.sum()|求和|
|x / x.sum()|非负权重归一化|
|torch.multinomial(x, 1)|随机采样|
|torch.sort(x, descending=True)|降序排序|
|torch.cumsum(x, dim=0)|计算累计和|
|x.item()|单元素 Tensor 转 Python 数值|

## 12. 本日易错点

1. 混淆原始 Logits 与处理后的概率。
    
2. Softmax 遗漏 dim 参数。
    
3. Top-K 遗漏 k 参数。
    
4. 归一化时错误使用索引之和或全部概率之和。
    
5. 将 torch.topk() 错写成 torch.top()。
    
6. 混淆采样位置与原始 Token ID。
    

## 13. 独立编程训练记录

- 第一次综合练习：1/6 步正确。
    
- 逐步引导后独立复写：5/6 步正确。
    
- 修复函数名称后：全部通过。
    

后续训练重点：

- 加强数据流分析。
    
- 熟悉常用函数及参数。
    
- 减少对代码模板的依赖。
    
- 增加无提示复写和延迟复习。
    

**本日核心收获：**

理解了大语言模型生成 Token 的基本原理，并能够使用 PyTorch 实现单步 Token 采样流程。