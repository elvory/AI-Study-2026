
## 一、TensorDataset

作用：将特征和标签组合成一个数据集。

```
from torch.utils.data import TensorDataset

train_dataset = TensorDataset(features, labels)
```

常用操作：

- `len(train_dataset)`：获取数据集大小。
    
- `train_dataset[0]`：获取第一条数据。
    

## 二、DataLoader

作用：加载数据、分批训练。

```
from torch.utils.data import DataLoader

train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True,
    drop_last=False
)
```

### 常用参数

|参数|作用|
|---|---|
|batch_size|每批数据量|
|shuffle|是否打乱数据|
|drop_last|是否丢弃不完整批次|

## 三、shuffle

- `True`：随机打乱样本顺序。
    
- `False`：按照原始顺序读取。
    

通常训练集使用 True，验证集和测试集使用 False。

## 四、drop_last

- `True`：丢弃最后不足一个完整批次的数据。
    
- `False`：保留最后一个不完整批次。
    

例如：10 条数据，batch_size=3。

- False：3 + 3 + 3 + 1，共 4 批。
    
- True：3 + 3 + 3，共 3 批。
    

## 五、len()

```
len(train_dataset)  # 数据集样本数量
len(train_loader)   # 批次数量
```

批次数量计算：

- drop_last=False：向上取整。
    
- drop_last=True：向下取整。
    

## 六、enumerate()

作用：同时获取循环索引和数据。

```
for batch_idx, (batch_features, batch_labels) in enumerate(train_loader):
    print(batch_idx)
    print(batch_features)
    print(batch_labels)
```

注意：索引从 0 开始。

## 七、完整数据加载流程

```
features = torch.tensor([[1.0], [2.0], [3.0]])
labels = torch.tensor([2.0, 4.0, 6.0])

dataset = TensorDataset(features, labels)

loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True,
    drop_last=False
)

for batch_idx, (x, y) in enumerate(loader):
    print(batch_idx, x, y)
```

## 八、Day40 核心收获

1. 理解 TensorDataset 的作用。
    
2. 掌握 DataLoader 的创建和使用。
    
3. 理解 batch_size、shuffle、drop_last。
    
4. 能够计算数据集的批次数量。
    
5. 掌握 enumerate() 遍历批次。
    
6. 能够独立编写完整的数据加载流程。
    

**下一步：Day41 - PyTorch 模型训练流程与训练循环。**