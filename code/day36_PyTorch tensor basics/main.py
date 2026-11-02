import torch

# tensor 张量
tensor_a = torch.tensor([10,20,30,40])
print(tensor_a)

# tensor的三个重要属性 shape形状 ndim维度 dtype数据类型
print(tensor_a.shape)
print(tensor_a.ndim)
print(tensor_a.dtype)


# 创建二维 Tensor
tensor_b = torch.tensor([
    [1,2,3],
    [4,5,6]
])
print(tensor_b)
print(tensor_b.shape)
print(tensor_b.ndim)
print(tensor_b.dtype)



# Tensor 基本运算
print(tensor_b+tensor_b)    # 加法

# *	对应位置相乘（逐元素乘法）
# @ 矩阵乘法
print(tensor_b * tensor_b)

tensor_c = torch.tensor([
    [1, 2],
    [3, 4],
    [5, 6]
])
print(tensor_b @ tensor_c)


# Tensor 与数字运算
#标量运算
print(tensor_b + 10)
