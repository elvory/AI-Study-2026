---
tags:
  - 主题/复习
  - 类型/周复习
aliases:
  - "Day42"
  - "Week06"
---

# Day42 · Week6：PyTorch 基础复盘


## 一、本周学习目标

掌握 PyTorch Tensor、自动求导、神经网络结构、数据加载和基本模型训练流程。

## 二、Day36–Day37：Tensor 基础

- Tensor 创建、索引、切片。
    
- shape、dtype。
    
- view() 与 reshape()。
    
- contiguous()。
    
- Tensor 内存共享。
    

重点：

- view() 返回共享底层数据的视图。
    
- reshape() 可能返回视图，也可能创建副本。
    
- 修改共享数据可能影响原 Tensor。
    

## 三、Day38：自动求导

核心知识：

- requires_grad=True：开启梯度跟踪。
    
- backward()：执行反向传播。
    
- grad：查看梯度。
    
- zero_()：清零梯度。
    
- torch.no_grad()：关闭梯度计算。
    
- detach()：从原计算图分离。
    

链式法则：

$$
\frac{dz}{dx}=\frac{dz}{dy}\frac{dy}{dx}
$$

## 四、Day39：神经网络基础

- nn.Module：模型基类。
    
- nn.Linear：全连接层。
    
- nn.ReLU：激活函数。
    
- nn.MSELoss：均方误差损失。
    
- SGD：随机梯度下降优化器。
    

## 五、Day40：数据加载

- TensorDataset：组合特征和标签。
    
- DataLoader：批量加载数据。
    
- batch_size：批次大小。
    
- shuffle：是否打乱数据。
    
- drop_last：是否丢弃不完整批次。
    
- enumerate：获取批次索引。
    

## 六、Day41：完整模型训练

基本流程：

1. optimizer.zero_grad()
    
2. model(x)
    
3. loss_fn(prediction, target)
    
4. loss.backward()
    
5. optimizer.step()
    

重要概念：

- Batch：一次处理一批数据。
    
- Epoch：完整遍历一次训练数据集。
    
- Iteration：一次批次训练迭代。
    
- Average Loss：原练习记录各 Batch 平均损失的等权平均；最后一批较小时，它与按样本平均可能不同，详见 [[notes/Day41 - PyTorch 神经网络训练流程|Day41 的统计说明]]。
    

## 七、Day42：综合复习

复习内容：

- TensorDataset 数据索引。
    
- DataLoader 批次计算。
    
- 自动求导与梯度计算。
    
- Linear 输入输出形状推导。
    
- view 与 reshape 区别。
    
- train() 与 eval()。
    
- detach()。
    
- 链式求导。
    

需要继续加强：

1. nn.Linear() 的形状推导。
    
2. 自动求导链式法则。
    
3. 独立编写完整训练循环。
    

## 八、本周总结

本周完成了从 Tensor 基础到神经网络训练的入门学习。

已经能够理解并编写简单的 PyTorch 神经网络，使用 DataLoader 加载数据，并通过反向传播和优化器更新模型参数。

下一阶段：Transformer、Tokenization、Embedding 与 LLM 基础。

## 九、复盘速查

| 容易混淆的操作 | 准确含义 |
|---|---|
| `model.train()` / `model.eval()` | 切换训练或评估模式，影响 Dropout、BatchNorm 等层；不直接关闭梯度记录 |
| `torch.no_grad()` | 在作用域内关闭通常的反向自动求导记录；不会替代 `eval()` 切换层的行为 |
| `nn.Linear(8, 16)` | 变换最后一个维度：`(B, T, 8)` → `(B, T, 16)` |
| `view()` / `reshape()` | 前者要求形状与步长兼容；后者必要时复制，不能依赖它一定共享数据 |

常见推理组合：

```python
model.eval()
with torch.no_grad():
    prediction = model(features)
```

回到训练前，调用 `model.train()`。这些速查说明不改变上面记录的本周成果与待加强项目。

## 参考资料

- [PyTorch：Module.eval / train](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.eval)
- [PyTorch：torch.no_grad](https://docs.pytorch.org/docs/stable/generated/torch.no_grad.html)
- [PyTorch：MSELoss](https://docs.pytorch.org/docs/stable/generated/torch.nn.MSELoss.html)

---

## 知识关联

- 复习入口：[[maps/复习与实践|复习与实践]]
- 知识主题：[[maps/PyTorch与深度学习|PyTorch 与深度学习]]
- 本周学习记录：[[notes/Day36：PyTorch 基础与 Tensor|Day36]] · [[notes/Day37：PyTorch Tensor 索引、切片与形状变换|Day37]] · [[notes/Day38：PyTorch 自动求导与梯度计算|Day38]] · [[notes/Day39：PyTorch 神经网络基础|Day39]] · [[notes/Day40 - PyTorch Dataset 与 DataLoader|Day40]] · [[notes/Day41 - PyTorch 神经网络训练流程|Day41]]
