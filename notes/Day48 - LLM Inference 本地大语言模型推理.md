
**学习阶段：** Week7  
**学习状态：** 代码验收通过，待 Git 提交

## 1. 本地模型运行环境

- GPU：NVIDIA GeForce RTX 4060 Laptop GPU
    
- 显存：8GB
    
- PyTorch：2.6.0+cu124
    
- CUDA：可用
    
- 模型：Qwen2.5-0.5B-Instruct
    
- 模型精度：FP16
    
- 推理设备：cuda:0
    

模型存储路径：

`D:\AI-models\Qwen2.5-0.5B-Instruct`

## 2. 本地模型加载

```
from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM
import torch

model_name = r"D:\AI-models\Qwen2.5-0.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    local_files_only=True
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype=torch.float16,
    local_files_only=True
)

model = model.to("cuda")
model.eval()
```

参数说明：

- local_files_only：仅加载本地文件。
    
- float16：半精度浮点数，减少显存占用。
    
- model.to("cuda")：将模型移动到 GPU。
    
- model.eval()：切换到评估模式。
    

## 3. LLM 完整推理流程

用户输入  
→ Chat Template  
→ Tokenizer  
→ 输入张量移动到 GPU  
→ model.generate()  
→ 提取新生成的 Token  
→ Decode  
→ 输出回答

## 4. Chat Template

常见对话角色：

|role|作用|
|---|---|
|system|设置模型身份和行为规则|
|user|用户输入|
|assistant|模型回答|

```
prompt_text = tokenizer.apply_chat_template(
    history_messages,
    tokenize=False,
    add_generation_prompt=True
)
```

Chat Template 将结构化消息转换成模型所需要的对话格式。

## 5. Tokenizer 编码与设备转换

```
model_inputs = tokenizer(
    prompt_text,
    return_tensors="pt",
    add_special_tokens=False
).to(model.device)
```

说明：

- return_tensors="pt"：返回 PyTorch Tensor。
    
- to(model.device)：将输入移动到模型所在设备。
    
- 已经应用 Chat Template 时，通常应避免重复添加特殊 Token。
    

模型参数与输入张量应位于兼容的计算设备上。

## 6. model.generate()

```
with torch.no_grad():
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=256,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.9
    )
```

|参数|含义|
|---|---|
|max_new_tokens|最大新生成 Token 数|
|do_sample|是否启用随机采样|
|temperature|调节概率分布|
|top_k|限制候选 Token 数量|
|top_p|限制候选累计概率|

## 7. 提取新生成的 Token

Decoder-only 模型的 generate() 默认返回包含输入和新生成内容的完整序列。

```
input_length = model_inputs["input_ids"].shape[1]

new_token_ids = generated_ids[:, input_length:]
```

本次实际运行：

- 输入形状：(1, 57)
    
- 完整输出形状：(1, 62)
    
- 新生成 Token 形状：(1, 5)
    

## 8. Decode 解码

```
response_text = tokenizer.decode(
    new_token_ids[0],
    skip_special_tokens=True
)
```

注意：

- [0]：取出第一条序列。
    
- [0:]：从第零行开始切片，仍保留原有维度。
    
- skip_special_tokens=True：跳过特殊 Token。
    
- True 是布尔值，不是字符串。
    

## 9. while 循环连续问答

```
while True:
    user_question = input("请输入你的问题：")

    if user_question == "exit":
        break

    # 构建输入
    # 模型推理
    # 解码输出
```

模型应该在循环外加载一次。

用户输入、编码、推理和解码应该在循环内重复执行。

## 10. Conversation History

在循环外初始化历史列表：

```
history_messages = [
    {
        "role": "system",
        "content": "你是一名Python编程老师。"
    }
]
```

在循环内保存用户消息：

```
history_messages.append({
    "role": "user",
    "content": user_question
})
```

模型生成回答后保存助手消息：

```
history_messages.append({
    "role": "assistant",
    "content": response_text
})
```

每次推理时将完整历史列表传入 Chat Template。

对话历史保存在内存中，程序退出后会丢失。

## 11. 对话历史与模型训练的区别

多轮对话历史管理不会修改模型权重。

它只是通过增加输入上下文，让模型能够利用之前的对话信息。

这属于 Inference 和 Context Management，不属于 Fine-tuning。

## 12. 工程问题与解决方案

### Hugging Face 下载超时

使用 ModelScope 下载模型，再从本地加载。

### 模型权重不完整

发现 model.safetensors.incomplete 文件，说明下载尚未完成。

通过重新下载缺失文件解决。

### 解码结果带有列表格式

原因：向 decode 传入二维张量。

解决：使用 new_token_ids[0]。

### while 循环无法执行

错误写法：while not exit。

解决：使用 while True，并判断用户输入是否等于字符串 "exit"。

### 模型生成错误知识

模型正常运行不代表生成内容一定正确，需要额外进行准确性验证。

## 13. 本日学习成果

- 本地部署小型 LLM
    
- 使用 GPU 进行模型推理
    
- 理解 Chat Template
    
- 掌握 model.generate()
    
- 掌握生成 Token 的切片与解码
    
- 实现连续交互
    
- 实现多轮对话历史管理
    

## 14. 后续复习重点

- 张量索引与切片
    
- 函数参数及参数类型
    
- Python 循环与条件判断
    
- 数据流分析
    
- 独立编写 LLM 推理代码
    

## 15. 后续优化方向

- 上下文长度控制
    
- 对话历史持久化
    
- 流式输出
    
- 模型回答质量评估
    
- RAG 知识库接入
    

**本日核心收获：**

将 Transformer、Tokenization、Embedding、Attention 和 LLM 生成原理与实际工程应用联系起来，成功实现基于 Qwen 的本地多轮对话 AI 助手。