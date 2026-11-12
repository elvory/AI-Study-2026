

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

dz/dx = dz/dy × dy/dx

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
    
- Average Loss：一个 Epoch 内各批次损失的平均值。
    

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