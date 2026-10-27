import pandas as pd



#1.识别缺失值 isnull()
import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "score": [90, None, 85]
}

df = pd.DataFrame(data)

print(df.isnull())

print(df["score"].isnull())
print()



#2.删除缺失值 dropna()
df_clean = df.dropna()

print(df_clean)
print()



#3.填补缺失值 fillna()
df_filled = df.fillna(0)

print(df_filled)
print()



#4.数据排序 sort_values()

#df = pd.DataFrame({
#    "name": ["Alice", "Bob", "Charlie"],
#    "score": [90, 75, 85]
#})

#print(df.sort_values("score", ascending=False))


# # ascending=True：升序，默认值。
# # ascending=False：降序。


#5.分组统计 groupby()
# import pandas as pd

# df = pd.DataFrame({
#     "class": ["A", "A", "B", "B"],
#     "score": [80, 90, 70, 100]
# })

# result = df.groupby("class")["score"].mean()
# print(result)




# 综合练习

exercise_data = {
    "class": ["A", "A", "B", "B"],
    "name": ["Alice", "Bob", "Charlie", "David"],
    "score": [80, None, 70, 100]
}

exercise_df = pd.DataFrame(exercise_data)

# 1. 把缺失成绩填成60
filled_df = exercise_df.fillna({"score": 60})
print("填补缺失值：")
print(filled_df)

# 2. 按成绩从高到低排序
sorted_df = filled_df.sort_values("score", ascending=False)
print("成绩降序排列：")
print(sorted_df)

# 3. 统计每个班的平均成绩
class_avg = filled_df.groupby("class")["score"].mean()
print("各班平均成绩：")
print(class_avg)
