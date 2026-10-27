import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [20, 21, 19],
    "score": [90, 85, 95]
}

df = pd.DataFrame(data)

print(df.shape)     #输出行列信息
print(df.columns)   #输出所有列名
print(df.index)     #行 索引从0开始，到3之前结束，步长为1


#提取某一列
print(df["name"])
print()

#同时提取多列
print(df[["name", "score"]])
print()



result = df[df["age"] < 21]
print(result)
print()


# 计算所有学生的平均年龄
print(df["age"].mean())  # 平均年龄
print()



#查看数据 head()
print(df.head(2))
print()



# 读取 CSV 文件
# df = pd.read_csv("students.csv")


# 综合练习
# 任务 1： 提取所有学生的姓名和成绩
print(df[["name","score"]])

# 任务 2： 筛选出成绩大于等于 90 分的学生
print(df[df["score"] >= 90 ])

# 任务 3： 计算所有学生的平均成绩
print(df["score"].mean())
