# Day28 - 综合练习与 Week4 周复盘

## 一、今日综合练习

### 1. NumPy 条件筛选

```
import numpy as np

scores = np.array([78, 92, 65, 88, 95])

# 筛选大于等于80分的成绩
result = scores[scores >= 80]
print(result)

# 计算平均成绩
average = scores.mean()
print(average)
```

输出：

```
[92 88 95]
83.6
```

知识点：

- 布尔索引：`arr[条件]`
    
- 多条件筛选：使用 `&` 或 `|`，每个条件需要括号。
    
- 平均值：`mean()`
    

### 2. Pandas 条件筛选与统计

```
import pandas as pd

students_df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David"],
    "score": [90, 75, 85, 95]
})

# 筛选成绩大于等于85分的学生
result_pd = students_df[students_df["score"] >= 85]
print(result_pd)

# 计算平均成绩
average_pd = students_df["score"].mean()
print(average_pd)
```

输出：

```
      name  score
0    Alice     90
2  Charlie     85
3    David     95

86.25
```

注意：定义了哪个结果变量，就要打印对应的变量，例如 `print(result_pd)`，避免误打印其他练习的结果。

## 二、Week4 知识回顾

### Day22 - NumPy 基础

- 创建 NumPy 数组
    
- 数组运算
    
- `shape`、`size`、`dtype`
    

### Day23 - NumPy 数组操作

- `reshape()`：改变数组形状
    
- `flatten()`：展平并返回副本
    
- `ravel()`：展平，通常返回视图
    
- `concatenate()`：拼接数组
    
- `sort()`、`mean()`、`max()`、`min()`
    

### Day24 - 索引、切片与广播

- 布尔索引
    
- 数组切片
    
- 多条件筛选
    
- 广播机制
    

### Day25 - Pandas 基础

- `Series` 与 `DataFrame`
    
- `shape`、`columns`、`index`
    
- 单列与多列提取
    
- 条件筛选
    
- `mean()`、`max()`、`min()`
    
- `head()`、`tail()`、`read_csv()`
    

### Day26 - Pandas 数据处理

- `isnull()`：识别缺失值
    
- `dropna()`：删除缺失值
    
- `fillna()`：填补缺失值
    
- `sort_values()`：排序
    
- `groupby()`：分组统计
    

### Day27 - 机器学习基础概念

- 机器学习：从数据中学习规律
    
- 监督学习与无监督学习
    
- 特征 X 与标签 y
    
- 训练集与测试集
    
- 过拟合与泛化能力
    
- 回归与分类
    

### Day28 - 综合练习与周复盘

- NumPy 条件筛选与平均值计算
    
- Pandas 条件筛选与平均值计算
    
- 完成3道周复盘题，全部答对
    

## 三、Week4 学习总结

本周完成了 NumPy、Pandas 的基础学习，并初步认识了机器学习。

当前需要继续巩固：

1. 独立编写 NumPy 和 Pandas 代码。
    
2. 熟练掌握数组索引、广播和 DataFrame 筛选。
    
3. 能够根据实际问题选择合适的数据处理方法。
    

## 四、下一阶段

Day29 起进入下一周，继续推进 AI 基础学习。

建议后续逐步加入：

- 机器学习实际代码
    
- 模型训练与评估
    
- PyTorch 与神经网络基础
    

目标仍然是为 AI / 算法实习做好准备。