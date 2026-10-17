# Day23 - NumPy 数组操作

## 一、今日学习目标

掌握 NumPy 数组展平、拼接、排序和统计操作。

## 二、数组展平

### 1. flatten()

将多维数组展平为一维数组，始终返回副本。

```
arr = np.array([[1, 2], [3, 4]])
result = arr.flatten()
```

修改 `result` 不会影响原数组。

### 2. ravel()

将多维数组展平为一维数组，尽可能返回视图。

```
result = arr.ravel()
```

如果返回的是视图，修改结果会影响原数组。

区别：

- `flatten()`：始终复制数据。
    
- `ravel()`：尽可能不复制数据。
    

## 三、数组拼接

### 1. concatenate()

```
np.concatenate((arr1, arr2))
```

一维数组拼接。

二维数组可以指定方向：

```
np.concatenate((arr1, arr2), axis=0)  # 上下拼接
np.concatenate((arr1, arr2), axis=1)  # 左右拼接
```

### 2. vstack() 和 hstack()

```
np.vstack((arr1, arr2))  # 上下拼接
np.hstack((arr1, arr2))  # 左右拼接
```

对于形状兼容的二维数组，分别相当于 `concatenate()` 的 `axis=0` 和 `axis=1`。

## 四、数组排序

### 1. sort()

返回排序后的新数组，不修改原数组。

```
arr = np.array([5, 2, 8, 1])
result = np.sort(arr)
```

结果：

```
[1 2 5 8]
```

### 2. argsort()

返回元素升序排列时对应的原索引。

```
arr = np.array([40, 10, 30])
print(np.argsort(arr))
```

结果：

```
[1 2 0]
```

区别：

- `sort()`：返回排序后的数值。
    
- `argsort()`：返回排序后的索引。
    

## 五、常用统计方法

```
arr.mean()  # 平均值
arr.max()   # 最大值
arr.min()   # 最小值
arr.sum()   # 元素总和
```

例如：

```
arr = np.array([2, 4, 6, 8])

print(arr.mean())  # 5.0
print(arr.max())   # 8
print(arr.min())   # 2
print(arr.sum())   # 20
```

## 六、综合练习

```
import numpy as np

array_a = np.array([8, 3, 5])
array_b = np.array([2, 9, 4])

combined = np.concatenate((array_a, array_b))
sorted_arr = np.sort(combined)

print(sorted_arr)
print(combined.mean())
print(combined.max())
print(combined.min())
```

输出：

```
[2 3 4 5 8 9]
5.166666666666667
9
2
```

## 七、今日总结

1. `flatten()`：展平并复制数据。
    
2. `ravel()`：展平，尽可能返回视图。
    
3. `concatenate()`：按照指定方向拼接数组。
    
4. `vstack()`：上下拼接。
    
5. `hstack()`：左右拼接。
    
6. `sort()`：返回排序后的数值。
    
7. `argsort()`：返回排序后的原索引。
    
8. `mean()`、`max()`、`min()`、`sum()`：常用统计方法。
    

## 八、学习状态

- Day23：已完成。
    
- 下一步：Day24 - NumPy 索引、切片与广播。