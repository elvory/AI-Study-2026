# Day26 - Pandas 数据处理

## 一、今日学习目标

掌握缺失值识别、删除与填补、数据排序、分组统计。

## 二、识别缺失值

使用 `isnull()` 检查数据是否缺失。

```
df.isnull()           # 检查整个表格
df["score"].isnull()  # 检查成绩列
```

- `True`：数据缺失。
    
- `False`：数据不缺失。
    

## 三、删除缺失值

```
df_clean = df.dropna()
```

默认删除包含缺失值的行，返回新的 DataFrame，不直接修改原表格。

## 四、填补缺失值

```
df_filled = df.fillna(0)
```

把表格中的缺失值填为 0。

只填补成绩列：

```
df_filled = df.fillna({"score": 60})
```

区别：

- `dropna()`：删除缺失数据。
    
- `fillna()`：填补缺失数据。
    

## 五、数据排序

```
df_sorted = df.sort_values("score")
```

默认按照成绩升序排列。

```
df_sorted = df.sort_values("score", ascending=False)
```

按照成绩降序排列。

- `ascending=True`：升序。
    
- `ascending=False`：降序。
    

## 六、分组统计 groupby()

按班级统计平均成绩：

```
class_avg = df.groupby("class")["score"].mean()
```

执行过程：

1. 按 `class` 分组。
    
2. 选择每组的 `score` 列。
    
3. 使用 `mean()` 计算每组平均成绩。
    

## 七、今日综合练习

```
import pandas as pd

exercise_data = {
    "class": ["A", "A", "B", "B"],
    "name": ["Alice", "Bob", "Charlie", "David"],
    "score": [80, None, 70, 100]
}

exercise_df = pd.DataFrame(exercise_data)

# 1. 填补缺失成绩
filled_df = exercise_df.fillna({"score": 60})
print(filled_df)

# 2. 按成绩从高到低排序
sorted_df = filled_df.sort_values(
    "score", ascending=False
)
print(sorted_df)

# 3. 统计每个班的平均成绩
class_avg = filled_df.groupby("class")["score"].mean()
print(class_avg)
```

预期结果：

```
成绩降序排列：
David      100
Alice       80
Charlie     70
Bob         60

各班平均成绩：
A    70.0
B    85.0
```

## 八、今日总结

|方法|作用|
|---|---|
|`isnull()`|识别缺失值|
|`dropna()`|删除缺失数据|
|`fillna()`|填补缺失数据|
|`sort_values()`|按指定列排序|
|`groupby()`|按类别分组|
|`mean()`|计算平均值|

## 九、学习状态

- Day26：Pandas 数据处理已完成。
    
- 下一步：Day27 - 机器学习基础概念。