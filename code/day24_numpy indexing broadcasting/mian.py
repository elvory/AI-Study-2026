import numpy as np



#1.高级索引（布尔索引）

arr = np.array([12, 5, 28, 7, 35, 18])
#arr[arr > 15] 会筛选出所有大于 15 的元素，并保持它们原来的顺序。
result = arr[arr > 15]

print(result)



#2.切片（左闭右开，包含起始下标，不包含结束下标）
# arr = np.array([10, 20, 30, 40, 50, 60])
# print(arr[2:5])


#3.多个条件筛选
# arr = np.array([5, 15, 25, 35, 45])
# result = arr[(arr > 10) & (arr < 40)]
# print(result)

#规则：& 表示并且（AND）。
#     每个条件都要用括号括起来。



#广播机制（Broadcasting）

# 广播允许 NumPy 对形状不同但兼容的数组进行运算。
# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# print(arr + np.array([10, 20, 30]))

#结果：[[11 22 33]
#      [14 25 36]]



#综合练习
arr_1 = np.array([10, 20, 30, 40, 50, 60])

result_1 = arr_1[arr_1 >= 30] # 1. 筛选出大于等于 30 的元素
result_2 = arr_1[1:3] # 2. 取下标 1 到 3 的元素（包含1，不包含3）

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

result_3 = matrix + np.array([1, 2, 3])  # 3. 将 [1, 2, 3] 加到二维数组的每一行

print(result_1)
print(result_2)
print(result_3)

