

## 一、梯度跟踪

```
x = torch.tensor(3.0, requires_grad=True)
y = x ** 2
```

- `requires_grad=True`：开启梯度跟踪。
    
- 仅开启跟踪不代表已经计算梯度。
    

## 二、反向传播 backward()

```
y.backward()
print(x.grad)
```

作用：沿计算图反向传播，计算梯度。

例如：

[  
y=x^2,\quad x=3  
]

[  
\frac{dy}{dx}=2x=6  
]

## 三、梯度累积

PyTorch 默认累加梯度，不会自动清零。

```
x.grad.zero_()
```

训练模型时通常使用：

```
optimizer.zero_grad()
```

## 四、关闭梯度跟踪

```
with torch.no_grad():
    y = x ** 2
```

常用于模型推理，避免不必要的梯度计算。

## 五、detach()

```
y = x ** 2
z = y.detach()
```

- 从原计算图分离。
    
- 不再参与原计算图的梯度传播。
    
- 与原 Tensor 共享底层数据。
    
- 不改变原 Tensor 的计算图。
    

## 六、综合练习成果

```
x = torch.tensor(3.0, requires_grad=True)

y = x ** 2
z = y.detach()

loss = y * 2 + z * 3
loss.backward()

print(loss)
print(x.grad)
```

输出：

```
loss: tensor(45.)
x.grad: tensor(12.)
```

关键理解：detach() 只切断对应的梯度路径，不影响其他仍然连接计算图的路径。

## 七、易错点

1. requires_grad=True 不代表已经计算梯度。
    
2. backward() 默认累积梯度。
    
3. 重复 backward() 需要重新构建计算图，或者合理使用 retain_graph=True。
    
4. zero_() 清空梯度，但不会关闭梯度跟踪。
    
5. detach() 不会修改原 Tensor 的计算图。
    

## 今日总结

掌握了 PyTorch 自动求导的基本机制，理解了计算图、反向传播、梯度累积和梯度分离。