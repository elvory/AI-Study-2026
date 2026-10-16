import numpy as np

arr = np.arange(1,7)

#调整为2行3列
arr = arr.reshape(2,3)
print(arr)

#每个元素乘以10
arr = arr*10
print(arr)

#求每一列的和
arr_sum = arr.sum(axis=0)
print(arr_sum)
