

## 一、学习目标

- 掌握 Tensor 索引与元素访问
    
- 掌握 Tensor 切片
    
- 理解 reshape() 的使用
    
- 理解 view() 的使用
    
- 理解 Tensor 底层数据共享机制
    

## 二、Tensor 索引

```
import torch

tensor_index = torch.tensor([
    [10, 20, 30],
    [40, 50, 60]
])
```

### 1. 获取指定行

```
tensor_index[1]
```

获取第二行：

```
tensor([40, 50, 60])
```

### 2. 获取指定元素

```
tensor_index[0, 2]
```

获取第一行第三列：

```
tensor(30)
```

## 三、Tensor 切片

基本格式：

```
tensor[起始位置:结束位置]
```

注意：结束位置不包含在结果中。

### 1. 获取指定行的部分元素

```
tensor_index[1, 0:2]
```

结果：

```
tensor([40, 50])
```

### 2. 获取指定列

```
tensor_index[:, 1]
```

结果：

```
tensor([20, 50])
```

其中：

- `:` 表示所有行
    
- `1` 表示第二列
    

### 3. 获取多列

```
tensor_index[:, 1:3]
```

获取所有行的第二列和第三列。

## 四、reshape() 形状变换

reshape() 用于改变 Tensor 的形状。

```
tensor_index.reshape(3, 2)
```

原来的形状：

```
[2, 3]
```

变换后的形状：

```
[3, 2]
```

重要规则：

变换前后元素总数量必须一致。

例如：

- 2×3 → 3×2：合法
    
- 2×3 → 1×6：合法
    
- 2×3 → 1×4：不合法
    

## 五、view() 形状变换

```
tensor_view = tensor_index.view(3, 2)
```

view() 创建一个共享底层数据的视图。

修改视图中的元素：

```
tensor_view[0, 0] = 999
```

原 Tensor 中对应元素也会改变。

## 六、reshape() 与 view() 的区别

|对比|reshape()|view()|
|---|---|---|
|改变形状|支持|支持|
|是否一定复制|不一定|不复制|
|是否共享底层数据|可能|是|
|内存布局要求|更灵活|必须兼容|

重要理解：

1. reshape() 优先尝试返回视图，如果无法实现才复制数据。
    
2. view() 返回共享底层数据的视图，如果内存布局不兼容则报错。
    
3. 两者都不会直接改变原 Tensor 的 shape。
    

## 七、综合练习

```
tensor_text = torch.tensor([
    [1, 2, 3],
    [4, 5, 6]
])

# 获取第二列和第三列
selected = tensor_text[:, 1:3]

# 变成一行四列
result = selected.reshape(1, 4)

print(selected)
print(result)
```

输出：

```
tensor([[2, 3],
        [5, 6]])

tensor([[2, 3, 5, 6]])
```

## 八、今日总结

今天掌握了：

- Tensor 索引
    
- Tensor 切片
    
- 获取指定行和列
    
- reshape() 形状变换
    
- view() 共享数据机制
    
- 切片与形状变换的组合使用
    

## 九、下一步

Day38：PyTorch 自动求导（Autograd）。

学习：

- requires_grad
    
- 计算图
    
- backward()
    
- grad
    

为后续神经网络训练和梯度下降打基础。