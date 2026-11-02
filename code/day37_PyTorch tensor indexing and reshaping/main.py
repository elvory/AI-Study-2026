import torch

tensor_index = torch.tensor([
    [10,20,30],
    [40,50,60]
])

# 获取第二行的索引
print(tensor_index[1])

# 获取第一行第三列的元素
print(tensor_index[0,2])

print(tensor_index[1, 0:2])

# 获取所有行的第1列
print(tensor_index[:,1])


### Tensor 形状变换 reshape()
tensor_reshape = tensor_index.reshape(3,2)
print(tensor_reshape)
print(tensor_reshape.shape)

# view()
tensor_view = tensor_index.view(3, 2)

print(tensor_view)
print(tensor_view.shape)

# reshape()：改变 Tensor 的形状
# view()：通过共享底层数据的视图改变形状（通常要求内存连续）

tensor_view[0, 0] = 999

print("view:", tensor_view)
print("original:", tensor_index)
print("reshape:", tensor_reshape)



# 综合练习
tensor_text = torch.tensor([
    [1,2,3],
    [4,5,6]
])

print(tensor_text[:, 1:3])
print(tensor_text[:, 1:3].reshape(1,4))
