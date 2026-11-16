# Day44：模拟 Tokenization

text = "我 喜欢 学习 AI"

# 模拟 Tokenizer 切分
tokens = text.split()

# 模拟词表
vocab = {
    "我": 101,
    "喜欢": 102,
    "学习": 103,
    "AI": 104
}

# 将 Token 转换为 ID
token_ids = [vocab[token] for token in tokens]

print("原始文本：", text)
print("Tokens：", tokens)
print("Token IDs：", token_ids)
print("Token 数量：", len(tokens))


# 字符数量与 Token 数量的区别

chinese_sentence = "我喜欢学习人工智能"

# 计算字符数量
char_count = len(chinese_sentence)

print("原始文本：", chinese_sentence)
print("字符数量：", char_count)

# 注意：字符数量不等于 Token 数量



# Day44：BPE 字符对频率统计

bpe_corpus = ["abab", "abac", "abab"]

bpe_sequences = [list(word) for word in bpe_corpus]

pair_counts = {}

for symbols in bpe_sequences:
    for index in range(len(symbols) - 1):
        pair = (symbols[index], symbols[index + 1])

        pair_counts[pair] = pair_counts.get(pair, 0) + 1

print("字符对出现次数：", pair_counts)




from transformers import AutoTokenizer

# 加载 Qwen Tokenizer
qwen_tokenizer = AutoTokenizer.from_pretrained(
    "Qwen/Qwen2.5-0.5B"
)

# 准备文本
sample_text = "我喜欢学习人工智能"

# 执行分词
encoded_result = qwen_tokenizer(
    sample_text,
    add_special_tokens=False
)

# 获取 Token ID
token_id_list = encoded_result["input_ids"]

# 将 ID 转换成 Token
token_pieces = qwen_tokenizer.convert_ids_to_tokens(
    token_id_list
)

print("原始文本：", sample_text)
print("Tokens：", token_pieces)
print("Token IDs：", token_id_list)
print("Token 数量：", len(token_id_list))


# 将 Token ID 解码为原始文本
decoded_text = qwen_tokenizer.decode(token_id_list)

print("解码后的文本：", decoded_text)

# 检查是否还原成功
print("是否还原成功：", decoded_text == sample_text)



# Token ID 解码
decoded_sample_text = qwen_tokenizer.decode(token_id_list)

print("解码结果：", decoded_sample_text)

# 验证文本是否还原
print("是否还原成功：", decoded_sample_text == sample_text)
