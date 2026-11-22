
**学习阶段：** Week7  
**学习日期：** 2026-11-22  
**学习状态：** 代码验收通过，待 Git 提交

## 1. Attention 的核心公式

Scaled Dot-Product Attention：

[  
Attention(Q,K,V)=Softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V  
]

主要包含四个步骤：

1. QKᵀ：计算相关分数。
    
2. Scaling：缩放注意力分数。
    
3. Softmax：转换为注意力权重。
    
4. Weights × V：加权求和得到最终输出。
    

## 2. Q、K、V 的作用

|名称|作用|
|---|---|
|Query（Q）|查询相关信息|
|Key（K）|与 Query 进行匹配|
|Value（V）|提供最终需要提取的信息|

注意力分数：

```
attention_scores = query_vec @ key_matrix.T
```

## 3. Softmax

作用：将原始分数转换成注意力权重。

主要特点：

- 权重范围为 0～1。
    
- 所有权重之和等于 1。
    
- 原始分数越大，转换后的权重也越大。
    

PyTorch：

```
attention_weights = torch.softmax(
    attention_scores,
    dim=0
)
```

## 4. Attention 加权求和

根据注意力权重，对 Value 向量进行加权求和。

```
weighted_output = value_weights @ value_vectors
```

例如：

V1 = [2,4]

V2 = [6,8]

权重 = [0.75,0.25]

最终输出：

[3,5]

## 5. Scaling（缩放）

公式：

[  
ScaledScores=\frac{QK^T}{\sqrt{d_k}}  
]

其中 d_k 表示 Key 向量维度。

作用：

- 控制点积数值的规模。
    
- 避免 Softmax 因输入分数过大而过度集中。
    
- 帮助稳定训练。
    

PyTorch：

```
key_dim = key_matrix.shape[-1]

scaled_scores = attention_scores / (key_dim ** 0.5)
```

## 6. Scaled Dot-Product Attention 综合实践

核心代码：

```
final_weights = torch.softmax(
    scaled_scores,
    dim=0
)

final_output = final_weights @ final_value_matrix
```

实际运行结果：

```
注意力权重：
tensor([0.4235, 0.2088, 0.3677])

最终输出：
tensor([7.1765, 4.9118])
```

本次使用单个 Query、三个 Key 和三个 Value，暂未加入因果掩码。

## 7. 本日易错点

**错误：混淆原始分数与缩放分数。**

最初代码：

```
final_weights = torch.softmax(
    attention_scores,
    dim=0
)
```

虽然可以运行，但遗漏了 Scaling。

修正后：

```
final_weights = torch.softmax(
    scaled_scores,
    dim=0
)
```

经验：

- 变量名应当明确。
    
- 注意每个计算步骤的输入。
    
- 程序运行成功不代表算法逻辑一定正确。
    

## 8. 本日学习成果

- 理解 QKᵀ 点积
    
- 掌握 Softmax
    
- 理解 Value 加权求和
    
- 理解 Scaling 的作用
    
- 掌握 Scaled Dot-Product Attention 公式
    
- 使用 PyTorch 完成简化 Attention 实现
    
- 独立排查并修复变量引用错误
    

## 9. 下一步

Day47：LLM 基础

重点理解语言模型如何利用 Transformer，根据上下文预测下一个 Token，以及训练和推理之间的区别。

**本日总结：**

通过 Day46 的学习，我掌握了 Attention 的核心数学流程，并能够使用 PyTorch 实现简化的 Scaled Dot-Product Attention。这是后续理解 GPT、Qwen 等大语言模型的重要基础。