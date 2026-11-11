---
tags:
  - 主题/深度学习
  - 类型/每日笔记
aliases:
  - "Day41"
---

# Day41 - PyTorch 神经网络训练流程

## 一、今日学习目标

掌握 PyTorch 神经网络的完整训练流程，能够独立编写一个简单的模型训练循环。

## 二、核心知识

### 1. 神经网络模型

```
class PriceModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(1, 1)

    def forward(self, x):
        return self.fc(x)
```

- `nn.Module`：所有神经网络模型的基类。
    
- `nn.Linear(1, 1)`：输入一个特征，输出一个特征。
    
- `forward()`：定义模型前向传播过程。
    

### 2. 损失函数

```
loss_fn = nn.MSELoss()
loss = loss_fn(prediction, target)
```

MSELoss 用于计算预测值与真实值之间的均方误差。

[  
MSE=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2  
]

### 3. 完整训练流程

```
for epoch in range(num_epochs):

    for x, y in train_loader:

        optimizer.zero_grad()

        prediction = model(x)

        loss = loss_fn(prediction, y)

        loss.backward()

        optimizer.step()
```

执行顺序：

1. 清空梯度
    
2. 前向传播
    
3. 计算损失
    
4. 反向传播
    
5. 更新模型参数
    

### 4. Epoch 与 Batch

- Epoch：完整训练一次数据集。
    
- Batch：每次送入模型的一批数据。
    
- Batch Size：每批数据的数量。
    
- `drop_last=True`：丢弃不完整的最后一个 Batch。
    
- `drop_last=False`：保留不完整的最后一个 Batch。
    

计算关系：

总训练批次数 = Epoch 数量 × 每轮 Batch 数量。

### 5. 梯度清零

```
optimizer.zero_grad()
```

PyTorch 默认会累积梯度，因此每个 Batch 训练前需要清空梯度。

### 6. 平均 Loss

```
total_loss += loss.item()
batch_count += 1

avg_loss = total_loss / batch_count
```

注意：`total_loss` 和 `batch_count` 应在每个 Epoch 开始时重置，平均值应在 Batch 循环结束后计算。

## 三、今日重点

|方法|作用|
|---|---|
|`model(x)`|模型预测|
|`loss_fn()`|计算损失|
|`loss.backward()`|计算梯度|
|`optimizer.zero_grad()`|清空梯度|
|`optimizer.step()`|更新参数|
|`loss.item()`|获取损失数值|

## 四、今日练习结果

- Epoch：5
    
- 每轮平均 Loss 均呈下降趋势
    
- 标签形状调整：`reshape(-1, 1)`
    
- 训练循环：运行成功
    
- 综合小测：5/5 正确
    

## 五、今日总结

今天真正理解了 PyTorch 从数据输入到模型参数更新的完整过程。

核心记忆：

**清零 → 预测 → 算损失 → 反向传播 → 更新参数**

下一步：Day42，继续深度学习基础。

---

## 知识关联

- 主题入口：[[maps/PyTorch与深度学习|PyTorch与深度学习]]
- 相关知识：[[notes/Day39：PyTorch 神经网络基础|Day39]] · [[notes/Day40 - PyTorch Dataset 与 DataLoader|Day40]]
