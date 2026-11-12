# Tensor 自动求导
x = torch.tensor(3.0, requires_grad=True)

y = x ** 2

y.backward()

print(x.grad)



# 神经网络结构
class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3, 8)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(8, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x


# 数据加载
dataset = TensorDataset(features, labels)

loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True
)

# 完整训练循环
for epoch in range(num_epochs):

    model.train()

    for x, y in train_loader:

        optimizer.zero_grad()

        prediction = model(x)

        loss = loss_fn(prediction, y)

        loss.backward()

        optimizer.step()
