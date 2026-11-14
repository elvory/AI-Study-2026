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

$$
\mathrm{MSE}=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat y_i)^2
$$

本例每个样本只有一个预测值，因此这里的 $n$ 是样本数；`nn.MSELoss()` 默认对全部损失元素取平均，多输出时分母还包含输出维度。

模型预测与标签应具有相同形状，例如均为 `(B, 1)`。预测是 `(B, 1)`、标签是 `(B,)` 时会发生广播，可能算出不是本意的损失；本例可将标签 `reshape(-1, 1)`。

### 3. 完整训练流程

```
for epoch in range(num_epochs):

    for x, y in train_loader:

        optimizer.zero_grad()

        prediction = model(x)

        y = y.reshape(-1, 1)  # 与单输出模型的 (B, 1) 保持一致

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

### 6. 平均 Loss：先明确统计方式

#### 原练习：各 Batch 均值的算术平均

```
total_loss += loss.item()
batch_count += 1

avg_loss = total_loss / batch_count
```

注意：`total_loss` 和 `batch_count` 应在每个 Epoch 开始时重置，平均值应在 Batch 循环结束后计算。

这段写法对每个 Batch 等权平均。原练习有 5 个样本、`batch_size=2`，批次大小为 2、2、1；最后一个小批次仍占相同权重，因此该指标不一定等于按全部样本平均的 Loss。原实验结果继续按这个指标记录。

#### 改进统计：按样本数加权

若需要按样本统计，把以下累加逻辑放入已有训练循环。这里假设单输出回归，或每个样本的输出元素数相同，且 `loss_fn` 使用 `reduction="mean"`。

```python
# 每个 Epoch 开始时重置
total_loss = 0.0
sample_count = 0

# 以下三行放在已有 Batch 循环中，计算出 loss 之后
batch_size = x.size(0)
total_loss += loss.item() * batch_size
sample_count += batch_size

# Batch 循环结束后计算；空数据集应先排查
if sample_count == 0:
    raise ValueError("当前 Epoch 没有样本")
avg_loss = total_loss / sample_count
```

例如，前一批 2 个样本的平均损失为 1，最后 1 个样本的损失为 9：按 Batch 平均是 5，按样本平均是 $11/3$。训练期间参数会随 Batch 更新，这个记录指标也不等于训练结束后固定模型再评估整个数据集的 Loss。

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

后续复盘：[[notes/Day42-Week6：PyTorch 基础复盘|Day42 · Week6 PyTorch 基础复盘]]。

## 参考资料

- [PyTorch：MSELoss 的 reduction 与形状要求](https://docs.pytorch.org/docs/stable/generated/torch.nn.MSELoss.html)

---

## 知识关联

- 主题入口：[[maps/PyTorch与深度学习|PyTorch与深度学习]]
- 相关知识：[[notes/Day39：PyTorch 神经网络基础|Day39]] · [[notes/Day40 - PyTorch Dataset 与 DataLoader|Day40]]
