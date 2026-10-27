import numpy as np

arr = np.array([
    [10,20],
    [30,40],
    [50,60]
])

#1.数组展平
#flatt()
#ravel()

#flatten(),数组展平，不改变原数组，一定复制数据
result = arr.flatten()

print(result)
print(result.shape)
print()

flat_copy = arr.flatten()
flat_copy[0] = 999

print("原数组：")
print(arr)

print("展平后的数组：")
print(flat_copy)
print()

#ravel()，数组展平，改变原数组,尽可能不复制数据
falt_view = arr.ravel()
falt_view[0] = 888

print("原数组：")
print(arr)

print("ravel结果：")
print(falt_view)



#2.数组拼接
#concatenate()

arr1 = np.array([10, 20])
arr2 = np.array([30, 40])

result = np.concatenate((arr2, arr1))

# np.concatenate((arr1, arr2), axis=0)  # 上下拼接
# np.concatenate((arr1, arr2), axis=1)  # 左右拼接


matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

vertical = np.concatenate((matrix_a, matrix_b), axis=0)
horizontal = np.concatenate((matrix_a, matrix_b), axis=1)

print("上下拼接：")
print(vertical)
print(vertical.shape)

print("左右拼接：")
print(horizontal)
print(horizontal.shape)



#3.vstack()和hstack()

# np.vstack((matrix_a, matrix_b))  # 上下拼接
# np.hstack((matrix_a, matrix_b))  # 左右拼接

a = np.array([[1, 2]])
b = np.array([[3, 4]])

print(np.vstack((a, b)))
print(np.hstack((a, b)))
print()

#4.sort() 返回排序后的新数组，原数组不变
#5.argsort() 返回这些数值排序前的索引

# np.sort(arr)：返回排序后的数值。
# np.argsort(arr)：返回排序后对应的原索引。


#6.求平均值mean()

# arr = np.array([2, 4, 6, 8])
# print(arr.mean())



#7.最大值与最小值

# arr = np.array([3, 8, 2, 10, 5])

# print(arr.max())  # 最大值：10
# print(arr.min())  # 最小值：2


#综合练习
array_a = np.array([8, 3, 5])
array_b = np.array([2, 9, 4])

combined = np.concatenate((array_a, array_b)) #拼接

sorted_arr = np.sort(combined)  #排序

print(sorted_arr)   #输出排序结果
print(combined.mean())  #输出平均值
print(combined.max())   #最大值
print(combined.min())   #最小值
