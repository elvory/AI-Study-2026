---
tags:
  - 主题/深度学习
  - 类型/每日笔记
aliases:
  - "Day39"
---

# Day39：PyTorch 神经网络基础



## 一、nn.Module
- PyTorch 神经网络模型的基类。
- 自定义模型通常继承 nn.Module。
- __init__() 定义网络层。
- forward() 定义前向传播。

## 二、常见网络组件
- nn.Linear(in_features, out_features)：全连接层。
- nn.ReLU()：激活函数，将负数变为 0。
- nn.MSELoss()：均方误差损失函数。

## 三、模型训练流程
1. optimizer.zero_grad()：清空旧梯度。
2. output = model(input_data)：前向传播。
3. loss = loss_fn(output, target)：计算损失。
4. loss.backward()：反向传播，计算梯度。
5. optimizer.step()：更新模型参数。

## 四、SGD 参数更新
w_new = w_old - lr × grad

## 五、重要区别
- zero_grad()：清空梯度，不清空权重。
- backward()：计算梯度，不直接更新权重。
- step()：根据梯度更新权重。
- PyTorch 默认梯度累积，需要及时清零。

## 六、今日总结
理解了 nn.Module、Linear、ReLU、MSELoss，以及完整的模型训练流程。通过实际运行验证了梯度计算和 SGD 参数更新。

---

## 知识关联

- 主题入口：[[maps/PyTorch与深度学习|PyTorch与深度学习]]
- 相关知识：[[notes/Day38：PyTorch 自动求导与梯度计算|Day38]]
