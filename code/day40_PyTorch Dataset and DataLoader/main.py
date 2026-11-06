import torch

# 房屋面积（特征）
features = torch.tensor([
    [50.0],
    [80.0],
    [100.0],
    [120.0]
])

# 房屋价格（标签）
labels = torch.tensor([
    100.0,
    160.0,
    200.0,
    240.0
])

print("特征：", features)
print("标签：", labels)

print("特征形状：", features.shape)
print("标签形状：", labels.shape)



from torch.utils.data import TensorDataset, DataLoader

# 创建数据集
train_dataset = TensorDataset(features, labels)

# 查看数据集大小
print("数据集大小：", len(train_dataset))

# 获取第一条数据
print("第一条数据：", train_dataset[0])

print("第三条数据：",train_dataset[2])


### DataLoader（数据加载器）
# 创建数据加载器
train_loader = DataLoader(
    train_dataset,  #加载和分批数据
    batch_size=3,   #每批数据量
    shuffle=False,  #是否打乱数据
    drop_last=True  #是否丢弃不完整批次
)

# 遍历每一个批次
for batch_idx, (batch_features, batch_labels) in enumerate(train_loader):
    print("批次编号：", batch_idx)
    print("当前批次特征：", batch_features)
    print("当前批次标签：", batch_labels)

### drop_last
### len(train_loader)




#  综合练习
practice_features = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0]
])

practice_labels = torch.tensor([
    2.0, 4.0, 6.0, 8.0, 10.0
])


train_dataset_test = TensorDataset(practice_features,practice_labels)


train_loader_test = DataLoader(
    train_dataset_test,  #加载和分批数据
    batch_size=2,   #每批数据量
    shuffle=False,  #是否打乱数据
    drop_last=False  #是否丢弃不完整批次
)

print("数据集大小：", len(train_dataset_test))
print("批次数量：", len(train_loader_test))

for batch_idx, (batch_features, batch_labels) in enumerate(train_loader_test):
    print("批次编号：", batch_idx)
    print("当前批次特征：", batch_features)
    print("当前批次标签：", batch_labels)
