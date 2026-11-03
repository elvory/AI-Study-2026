import torch

# 梯度
# requires_grad = True    #告诉 PyTorch:这个 Tensor 需要参与梯度计算，请记录相关运算,并不意味着已经计算出了梯度，只是开启了梯度跟踪

x = torch.tensor(3.0, requires_grad=True)

y = x ** 2

# backward() 沿着计算图反向传播，计算梯度

# 第一次反向传播
y.backward()
print("第一次梯度：", x.grad)

# 梯度清零
x.grad.zero_()
print("清零后：", x.grad)

# 重新计算 y，创建新的计算图
y = x ** 2

# 第二次反向传播
y.backward()
print("第二次梯度：", x.grad)



# 关闭梯度跟踪
with torch.no_grad():
    y_no_grad = x ** 2

print("是否跟踪梯度：", y_no_grad.requires_grad)


# 综合练习
x = torch.tensor(2.0, requires_grad=True)

y = (3*x**2)+(2*x)+1

y.backward()

print("y",y)
print("x.grad",x.grad)


## 梯度累积（Gradient Accumulation）
x = torch.tensor(2.0, requires_grad=True)

y = 3 * x ** 2 + 2 * x + 1
y.backward()
print("第一次：", x.grad)

# 重新计算 y，创建新的计算图
y = 3 * x ** 2 + 2 * x + 1
y.backward()
print("第二次：", x.grad)




# detach()
x_detach = torch.tensor(2.0, requires_grad=True)

y_detach = x_detach ** 2

y_stop = y_detach.detach()

print(y_detach.requires_grad)   # 仍然跟踪梯度
print(y_stop.requires_grad)     # 已经从计算图中分离



# 综合练习
x = torch.tensor(3.0, requires_grad=True)

y = x ** 2
z = y.detach()

loss = y * 2 + z * 3

loss.backward()

print("loss:", loss)
print("x.grad:", x.grad)
