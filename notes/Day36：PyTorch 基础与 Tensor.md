---
tags:
  - 主题/深度学习
  - 类型/每日笔记
aliases:
  - "Day36"
---


## 一、学习目标

- 了解 PyTorch 的基本用途
    
- 理解 Tensor（张量）
    
- 掌握 Tensor 的创建方式
    
- 掌握 Tensor 的基本属性
    
- 掌握 Tensor 的基本运算
    

## 二、PyTorch 环境

- PyTorch 版本：2.6.0+cu124
    
- CUDA available：True
    
- Python 环境：ai-study
    

PyTorch 是一个深度学习框架，主要用于构建和训练神经网络。

## 三、Tensor 基础

Tensor 是 PyTorch 中最核心的数据结构，可以表示不同维度的数据。

|类型|维度|
|---|---|
|标量|0维|
|向量|1维|
|矩阵|2维|
|高维张量|3维及以上|

### 1. 创建 Tensor

```
import torch

# 一维 Tensor
tensor_a = torch.tensor([10, 20, 30, 40])

# 二维 Tensor
tensor_b = torch.tensor([
    [1, 2, 3],
    [4, 5, 6]
])
```

注意：torch.tensor() 是函数，使用圆括号调用。

## 四、Tensor 三个重要属性

### 1. shape：形状

```
print(tensor_b.shape)
```

输出：`torch.Size([2, 3])`

表示 2 行 3 列。

### 2. ndim：维度

```
print(tensor_b.ndim)
```

输出：`2`

表示二维 Tensor。

### 3. dtype：数据类型

```
print(tensor_b.dtype)
```

输出：`torch.int64`

表示 64 位整数。

## 五、Tensor 基本运算

### 1. 加法

```
tensor_b + tensor_b
```

对应位置相加。

### 2. 逐元素乘法

```
tensor_b * tensor_b
```

对应位置相乘。

结果：

```
tensor([[ 1,  4,  9],
        [16, 25, 36]])
```

### 3. 矩阵乘法

```
tensor_c = torch.tensor([
    [1, 2],
    [3, 4],
    [5, 6]
])

print(tensor_b @ tensor_c)
```

矩阵乘法规则：

左边矩阵的列数必须等于右边矩阵的行数。

结果：

```
tensor([[22, 28],
        [49, 64]])
```

### 4. 标量运算

```
tensor_b * 2
```

Tensor 中每个元素都乘以 2。

## 六、重要知识点对比

|运算|含义|
|---|---|
|A + B|对应位置相加|
|A * B|逐元素相乘|
|A @ B|矩阵乘法|
|A * 2|每个元素乘以 2|

## 七、今日总结

今天掌握了：

1. Tensor 的创建。
    
2. Tensor 的维度与形状。
    
3. shape、ndim、dtype 三个属性。
    
4. Tensor 加法。
    
5. 逐元素乘法与矩阵乘法的区别。
    
6. Tensor 与标量的运算。
    

## 八、下一步

Day37：Tensor 索引、切片与形状变换。

继续学习 PyTorch，为自动求导和神经网络训练打基础。

---

## 知识关联

- 主题入口：[[maps/PyTorch与深度学习|PyTorch与深度学习]]
- 相关知识：[[notes/Day22-NumPy基础|Day22]]
