import numpy as np
import pandas as pd


# numpy 练习
scores = np.array([78, 92, 65, 88, 95])

# 找出所有大于等于 80 分的成绩
result_np = scores[scores >= 80]
print(result_np)
print()

# 计算所有学生的平均成绩
average_np = sum(scores) / len(scores)     #也可写成 average = scores.mean()
print(average_np)
print()


# pandas 练习
students_df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David"],
    "score": [90, 75, 85, 95]
})

# 筛选出成绩大于等于 85 分的学生
result_pd = students_df[students_df["score"] >= 85]
print(result_pd)
print()


# 计算所有学生的平均成绩
average_pd = students_df["score"].mean()
print(average_pd)
print()
