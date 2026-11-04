# torch.nn 是 PyTorch 提供的神经网络工具箱

# nn.Linear	    全连接层
# nn.ReLU	    激活函数
# nn.MSELoss	均方误差损失函数
# nn.Module	    神经网络模型的基类

import torch
import torch.nn as nn

# nn.Module 是 PyTorch 所有神经网络模型的基类
class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(2, 4)  #nn.Linear(输入特征数量, 输出特征数量)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        return x


model = MyModel()

input_data = torch.tensor([[1.0, 2.0]])

output = model(input_data)

print("输出：", output)
print("输出形状：", output.shape)



# MSELoss 均方误差损失函数

pred = torch.tensor([2.0, 4.0, 6.0])
target = torch.tensor([1.0, 5.0, 3.0])

loss_fn = nn.MSELoss()

loss = loss_fn(pred, target)

print("损失值：", loss)



## loss.backward()

# 使用模型输出计算损失
target_output = torch.tensor([[0.0, 1.0, 0.0, 1.0]])

criterion_model = nn.MSELoss()

model_loss = criterion_model(output, target_output)

# 清空模型参数的旧梯度
model.zero_grad()

# 反向传播
model_loss.backward()

# 查看模型参数梯度
print("权重梯度：", model.fc1.weight.grad)
print("偏置梯度：", model.fc1.bias.grad)



## optimizer.step()
# 创建 SGD 优化器
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)

# 保存更新前的权重
weight_before = model.fc1.weight.detach().clone()

# 更新参数
optimizer.step()

# 查看更新前后的权重
print("更新前：", weight_before)
print("更新后：", model.fc1.weight)
