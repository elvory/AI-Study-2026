import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader

# 1. 准备训练数据
features = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0]
])

labels = torch.tensor([
    2.0,
    4.0,
    6.0,
    8.0,
    10.0
])

# 2. 创建数据集
train_dataset = TensorDataset(features, labels)

# 3. 创建数据加载器
train_loader = DataLoader(
    train_dataset,
    batch_size=2,
    shuffle=True
)

print("特征形状：", features.shape)
print("标签形状：", labels.shape)
print("数据集大小：", len(train_dataset))
print("批次数量：", len(train_loader))


# 4. 创建神经网络模型
class PriceModel(nn.Module):

    def __init__(self):
        super().__init__()

        # 输入1个特征，输出1个预测值
        self.fc = nn.Linear(1, 1)

    def forward(self, x):

        x = self.fc(x)

        return x


# 创建模型
model = PriceModel()

print("模型结构：", model)


test_input = torch.tensor([[3.0]])

prediction = model(test_input)

print("预测结果：", prediction)
print("预测形状：", prediction.shape)




# 5. 定义损失函数
loss_fn = nn.MSELoss()

# 创建优化器
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)

num_epochs = 5

for epoch in range(num_epochs):
    total_loss = 0.0
    batch_count = 0

    for batch_features, batch_labels in train_loader:

        # 清空梯度
        optimizer.zero_grad()

        # 调整标签形状
        batch_labels = batch_labels.reshape(-1, 1)

        # 前向传播
        batch_predictions = model(batch_features)

        # 计算损失
        loss = loss_fn(batch_predictions, batch_labels)

        # 反向传播
        loss.backward()

        # 更新参数
        optimizer.step()

        total_loss += loss.item()
        batch_count += 1

    avg_loss = total_loss / batch_count

    print(
        f"Epoch: {epoch + 1}, "
        f"Average Loss: {avg_loss:.4f}"
    )
