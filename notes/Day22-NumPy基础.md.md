# Day22-NumPy基础

## 一、NumPy简介

NumPy 是 Python 中常用的数值计算库，主要用于：

- 数组和矩阵运算
- 数值计算
- 数据处理
- 机器学习 / 深度学习基础计算

导入：

import numpy as np

## 二、创建数组

arr = np.array([1, 2, 3, 4, 5])

## 三、向量化运算

NumPy 可以直接对整个数组进行运算：

arr + 2
arr - 2
arr * 2
arr / 2

例如：

arr = np.array([1, 2, 3])
arr * 2

结果：

[2 4 6]

Python 列表的 * 2 是重复列表，而 NumPy 数组的 * 2 是每个元素分别乘 2。

## 四、数组属性

### shape

查看数组形状：

arr.shape

二维数组：

(行, 列)

例如：

(2, 3) → 2行3列

### size

查看元素总数量：

arr.size

### dtype

查看元素的数据类型：

arr.dtype

常见类型：

- int
- float
- bool

## 五、数组索引

二维数组：

arr[行, 列]

下标从 0 开始。

例如：

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr[1, 2]

结果：

6

## 六、切片

arr[0, :]   # 第0行，所有列
arr[:, 0]   # 所有行，第0列
arr[:, 1]   # 所有行，第1列

## 七、修改元素

arr[2] = 10

可以直接修改指定位置的元素。

## 八、arange

np.arange(start, stop, step)

例如：

np.arange(1, 10, 2)

结果：

[1 3 5 7 9]

注意：

arange 遵循左闭右开原则，stop 不包含。

## 九、reshape

reshape 可以改变数组的形状，但不能改变元素总数。

例如：

arr = np.arange(1, 7)
arr = arr.reshape(2, 3)

结果：

[[1 2 3]
 [4 5 6]]

6个元素可以变成：

(2, 3)
(3, 2)
(6, 1)

但不能变成 (2, 4)，因为元素数量对不上。

## 十、sum

一维数组：

arr.sum()

求所有元素的和。

二维数组：

arr.sum(axis=0)   # 按列求和
arr.sum(axis=1)   # 按行求和

例如：

[[1 2 3]
 [4 5 6]]

axis=0：

[5 7 9]

axis=1：

[6 15]

## 十一、创建特殊数组

np.zeros(5)  # 创建全0数组
np.ones(3)   # 创建全1数组

## 十二、今日综合练习

arr = np.arange(1, 7)

arr = arr.reshape(2, 3)

arr = arr * 10

arr_sum = arr.sum(axis=0)

结果：

[[10 20 30]
 [40 50 60]]

[50 70 90]

## 十三、今日重点

1. NumPy 数组支持向量化运算
2. shape 表示数组形状
3. size 表示元素总数
4. dtype 表示数据类型
5. 二维数组使用 arr[行, 列]
6. reshape 改变形状但不改变元素数量
7. axis=0 按列计算
8. axis=1 按行计算
9. arange 是左闭右开