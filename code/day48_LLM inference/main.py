import torch
from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM

model_name = r"D:\AI-models\Qwen2.5-0.5B-Instruct"

# 加载本地分词器
tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    local_files_only=True
)

# 加载本地模型
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype=torch.float16,
    local_files_only=True
)

# 将模型移动到 GPU
model = model.to("cuda")

# 切换到评估模式
model.eval()

print("模型加载成功")
print("运行设备：", model.device)
print("模型精度：", model.dtype)
print()







history_messages = [
    {
        "role": "system",
        "content": "你是一名Python编程老师。"
    }
]


while True:
    # 构建对话消息
    user_question = input("请输入你的问题：")

    if user_question == "exit":
            break


    history_messages.append({
        "role": "user",
        "content": user_question
    })

    # 应用对话模板
    prompt_text = tokenizer.apply_chat_template(
        history_messages,
        tokenize=False,
        add_generation_prompt=True
    )

    # 将文本转换为张量，并移动到GPU
    model_inputs = tokenizer(
        prompt_text,
        return_tensors="pt"
    ).to(model.device)

    print("输入文本：", prompt_text)
    print("输入Token IDs：", model_inputs["input_ids"])
    print("输入形状：", model_inputs["input_ids"].shape)
    print("输入设备：", model_inputs["input_ids"].device)


    # model_inputs = model_inputs.to(model.device)
    #解决输入数据在CPU,但是模型在GPU上的运行错误


    # 使用模型生成 Token
    with torch.no_grad():
        generated_ids = model.generate(
            **model_inputs,
            max_new_tokens=256,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.9
        )

    print("输入形状：", model_inputs["input_ids"].shape)
    print("生成形状：", generated_ids.shape)
    print("生成结果：", generated_ids)



    # 获取原始输入长度
    input_length = model_inputs["input_ids"].shape[1]

    # 提取新生成的 Token
    new_token_ids = generated_ids[:,input_length:]

    print("新生成的Token：", new_token_ids)
    print("新生成的Token形状：", new_token_ids.shape)


    # 将新生成的 Token 解码为文本
    response_text = tokenizer.decode(
        new_token_ids[0],
        skip_special_tokens=True
    )

    print("AI 回答：", response_text)

    history_messages.append({
        "role":"assistant",
        "content": response_text
    })
