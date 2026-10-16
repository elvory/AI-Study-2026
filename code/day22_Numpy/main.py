import numpy as np

arr = np.array([1,2,3,4,5])

print(arr)
print(arr*2)
print(arr + 10)

print(arr.shape)
print(arr.size)
print(arr.dtype)
print()


arr2 = np.arange(1, 7)
arr2 = arr2.reshape(2, 3)

print(arr2)
print(arr2.shape)
