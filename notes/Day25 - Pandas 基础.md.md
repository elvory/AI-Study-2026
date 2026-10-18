# Day25 - Pandas 基础

## 一、今日学习目标

学习 Pandas 的基本数据结构、表格信息查看、列选择、条件筛选和简单统计。

## 二、Pandas 简介

Pandas 是 Python 常用的数据分析库，可以方便地处理表格数据。

导入：

```
import pandas as pd
```

## 三、Series 和 DataFrame

- `Series`：一维数据，可以理解为一列。
    
- `DataFrame`：二维表格，由行和列组成。
    

创建 DataFrame：

```
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [20, 21, 19],
    "score": [90, 85, 95]
}

df = pd.DataFrame(data)
print(df)
```

## 四、查看表格信息

```
df.shape    # 行数和列数
df.columns  # 所有列名
df.index    # 行索引
```

例如：

```
df.shape
# (3, 3)
```

`shape` 返回 `(行数, 列数)`。

## 五、提取列

### 1. 提取一列

```
df["name"]
```

返回 `Series`。

### 2. 提取多列

```
df[["name", "score"]]
```

返回 `DataFrame`。

注意：

- 一列：`df["name"]`
    
- 多列：`df[["name", "score"]]`
    

## 六、条件筛选

筛选年龄小于 21 岁的学生：

```
result = df[df["age"] < 21]
```

筛选成绩大于等于 90 分的学生：

```
result = df[df["score"] >= 90]
```

原理：

1. `df["score"] >= 90` 生成布尔条件。
    
2. 外层 `df[...]` 保留符合条件的整行数据。
    

## 七、常用统计方法

```
df["score"].mean()  # 平均值
df["score"].max()   # 最大值
df["score"].min()   # 最小值
df["score"].sum()   # 总和
```

例如，当前学生的平均成绩为：

```
90.0
```

## 八、查看部分数据

```
df.head()     # 默认查看前5行
df.head(2)    # 查看前2行
df.tail()     # 默认查看最后5行
df.tail(2)    # 查看最后2行
```

## 九、读取 CSV 文件

```
df = pd.read_csv("students.csv")
print(df.head())
```

`read_csv()` 用于读取 CSV 文件，文件路径必须正确。

## 十、今日综合练习

```
import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [20, 21, 19],
    "score": [90, 85, 95]
}

df = pd.DataFrame(data)

# 任务1：提取姓名和成绩
print(df[["name", "score"]])

# 任务2：筛选成绩大于等于90分的学生
print(df[df["score"] >= 90])

# 任务3：计算平均成绩
print(df["score"].mean())
```

结果：

- Alice：90 分
    
- Bob：85 分
    
- Charlie：95 分
    
- 平均成绩：90.0 分
    

## 十一、今日总结

1. `Series` 表示一维数据。
    
2. `DataFrame` 表示二维表格。
    
3. `shape` 查看行数和列数。
    
4. `columns` 查看列名。
    
5. `df["列名"]` 提取一列。
    
6. `df[["列1", "列2"]]` 提取多列。
    
7. `df[条件]` 筛选符合条件的行。
    
8. `mean()`、`max()`、`min()`、`sum()` 用于统计。
    
9. `head()`、`tail()` 查看部分数据。
    
10. `read_csv()` 读取 CSV 文件。
    

## 十二、学习进度

- Day25：Pandas 基础已完成。
    
- 下一步：Day26 - Pandas 数据处理。