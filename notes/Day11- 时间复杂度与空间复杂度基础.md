---
tags:
  - 主题/算法
  - 类型/每日笔记
aliases:
  - "Day11"
---

# Day11 - 时间复杂度与空间复杂度基础

## 今日学习内容

- 时间复杂度是什么
- `O(1)`
- `O(log n)`
- `O(n)`
- `O(n log n)`
- `O(n²)`
- 空间复杂度
- `list` 查找复杂度
- `set` 查找复杂度
- `dict` 查找复杂度
- 为什么哈希结构能优化查找
- 如何分析一段代码的复杂度

---

# 1. 什么是时间复杂度

时间复杂度用来描述：

> 随着输入数据规模 `n` 增大，程序执行工作量大概如何增长。

例如：

```python
for num in numbers:
    print(num)
```

如果 `numbers` 有：

```text
n 个元素
```

循环大约执行：

```text
n 次
```

所以时间复杂度：

```text
O(n)
```

---

# 2. O(1)

`O(1)` 表示：

> 执行时间基本不随着输入规模增长。

例如：

```python
numbers = [10, 20, 30, 40]

x = numbers[2]
```

列表按索引访问：

```python
numbers[2]
```

通常是：

```text
O(1)
```

因为不需要从头一个个查找。

---

# 3. O(n)

如果需要遍历所有元素：

```python
for num in numbers:
    print(num)
```

时间复杂度：

```text
O(n)
```

例如线性查找：

```python
target = 100

for num in numbers:
    if num == target:
        print("找到")
```

最坏情况下需要看完整个列表：

```text
O(n)
```

---

# 4. O(n²)

双层遍历：

```python
for i in numbers:
    for j in numbers:
        print(i, j)
```

外层：

```text
O(n)
```

内层：

```text
O(n)
```

所以：

```text
O(n) × O(n)
=
O(n²)
```

---

# 5. 不能只看有几层 for

例如：

```python
for num in numbers:
    if num in numbers:
        print(num)
```

表面上只有一个 `for`。

但是：

```python
num in numbers
```

如果 `numbers` 是 `list`，查找本身最坏是：

```text
O(n)
```

所以：

```text
for            → O(n)

list 查找      → O(n)
```

整体：

```text
O(n²)
```

---

# 6. list 查找

例如：

```python
numbers = [1, 2, 3, 4, 5]

5 in numbers
```

列表通常需要从前往后寻找。

所以：

```text
target in list
```

最坏时间复杂度：

```text
O(n)
```

---

# 7. set 查找

例如：

```python
numbers = {1, 2, 3, 4, 5}

5 in numbers
```

`set` 基于哈希结构。

平均情况下：

```text
target in set
```

复杂度：

```text
O(1)
```

---

# 8. dict 查找

例如：

```python
scores = {
    "Alice": 88,
    "Bob": 95
}

score = scores["Bob"]
```

按 key 查找：

```text
平均 O(1)
```

---

# 9. list / set / dict 查找对比

```text
list

按索引访问
O(1)

查找元素
O(n)
```

```text
set

查找元素
平均 O(1)
```

```text
dict

按 key 查找
平均 O(1)
```

---

# 10. 为什么 set / dict 能优化代码

例如原代码：

```python
for num in numbers:
    if num in other_list:
        print(num)
```

假设：

```text
numbers 长度 = n
other_list 长度 = n
```

外层遍历：

```text
O(n)
```

列表查找：

```text
O(n)
```

整体：

```text
O(n²)
```

---

如果先转成集合：

```python
other_set = set(other_list)

for num in numbers:
    if num in other_set:
        print(num)
```

建立集合：

```text
O(n)
```

遍历：

```text
O(n)
```

set 查找平均：

```text
O(1)
```

所以整体：

```text
O(n)
```

忽略常数后：

```text
O(n) + O(n)
=
O(n)
```

---

# 11. 哈希优化思想

以后做 LeetCode 时，如果看到：

```text
频繁查找
是否出现过
是否存在
去重
匹配
```

应该考虑：

```python
set
```

或者：

```python
dict
```

核心思想：

> 用额外空间换更快的查找速度。

---

# 12. 空间复杂度

空间复杂度描述：

> 随着输入规模增大，程序额外需要多少内存。

---

# 13. O(1) 空间

例如：

```python
total = 0

for num in numbers:
    total += num
```

虽然循环执行 `n` 次，

但是额外只用了固定变量：

```text
total
num
```

变量数量不会随着 `n` 增长。

所以空间复杂度：

```text
O(1)
```

时间复杂度：

```text
O(n)
```

---

# 14. O(n) 空间

例如：

```python
result = []

for num in numbers:
    result.append(num * 2)
```

如果输入有：

```text
n 个元素
```

最终：

```python
result
```

也可能保存：

```text
n 个元素
```

所以空间复杂度：

```text
O(n)
```

同时循环一次：

```text
时间复杂度 O(n)
```

---

# 15. 时间复杂度和空间复杂度不同

例如：

```python
total = 0

for num in numbers:
    total += num
```

结果：

```text
时间复杂度：O(n)

空间复杂度：O(1)
```

而：

```python
result = []

for num in numbers:
    result.append(num)
```

结果：

```text
时间复杂度：O(n)

空间复杂度：O(n)
```

所以：

```text
时间复杂度 ≠ 空间复杂度
```

需要分别分析。

---

# 16. append() 的复杂度

例如：

```python
result.append(num)
```

通常看作：

```text
O(1)
```

所以：

```python
for num in numbers:
    result.append(num)
```

不是：

```text
O(n²)
```

而是：

```text
O(n) × O(1)
=
O(n)
```

---

# 17. O(log n)

`O(log n)` 最典型的是：

> 每一步都把问题规模缩小一半。

例如二分查找：

```text
8
↓
4
↓
2
↓
1
```

如果数据量是：

```text
n
```

执行次数大约：

```text
log₂(n)
```

所以：

```text
O(log n)
```

---

# 18. 二分思想

例如有序列表：

```python
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
```

如果使用普通查找：

```text
一个一个找
```

可能是：

```text
O(n)
```

如果每次判断中间位置，然后砍掉一半：

```text
O(log n)
```

---

# 19. O(n log n)

常见排序算法的复杂度：

```text
O(n log n)
```

例如 Python：

```python
sorted(numbers)
```

学习阶段可以记作：

```text
O(n log n)
```

---

# 20. 常见复杂度排序

从通常更快到更慢：

```text
O(1)

↓

O(log n)

↓

O(n)

↓

O(n log n)

↓

O(n²)
```

---

# 21. 直观比较

假设：

```text
n = 1000
```

大概可以理解成：

```text
O(1)
≈ 1

O(log n)
≈ 10

O(n)
≈ 1000

O(n log n)
≈ 10000

O(n²)
≈ 1000000
```

数字只是帮助理解，不需要死记。

重点：

> 数据规模越大，复杂度差距越明显。

---

# 22. sorted()

例如：

```python
sorted(numbers)
```

时间复杂度学习阶段记：

```text
O(n log n)
```

不要误认为：

```text
O(n²)
```

---

# 23. 今日综合练习

## 练习 1

```python
numbers = [1, 2, 3, 4, 5]

x = numbers[2]
```

时间复杂度：

```text
O(1)
```

---

## 练习 2

```python
for num in numbers:
    print(num)
```

时间复杂度：

```text
O(n)
```

---

## 练习 3

```python
for num in numbers:
    if num in numbers:
        print(num)
```

分析：

```text
for
→ O(n)

num in list
→ O(n)
```

所以：

```text
O(n²)
```

---

## 练习 4

```python
number_set = set(numbers)

for num in numbers:
    if num in number_set:
        print(num)
```

分析：

```text
set(numbers)
→ O(n)

for
→ O(n)

set 查找
→ 平均 O(1)
```

整体：

```text
O(n)
```

---

## 练习 5

```python
result = []

for num in numbers:
    result.append(num * 2)
```

时间复杂度：

```text
O(n)
```

空间复杂度：

```text
O(n)
```

---

# 24. 今日容易出错的点

## 错误 1：看到循环里还有操作就直接乘 n

例如：

```python
for num in numbers:
    result.append(num)
```

不能认为：

```text
for O(n)
append O(n)
```

实际上：

```text
append 平均 O(1)
```

所以：

```text
O(n)
```

---

## 错误 2：只看 for 层数

例如：

```python
for num in numbers:
    if num in numbers:
        ...
```

虽然只有一层显式 `for`，

但是：

```python
num in numbers
```

本身也是：

```text
O(n)
```

所以整体：

```text
O(n²)
```

---

## 错误 3：把 sorted() 当成 O(n²)

当前阶段记：

```python
sorted()
→ O(n log n)
```

---

# 25. Day11 核心思维

以后分析代码时，不要只问：

```text
有几个循环？
```

而要问：

```text
1. 每个操作本身复杂度是多少？

2. 循环执行多少次？

3. 嵌套操作需要相乘吗？

4. 顺序执行需要相加吗？

5. 有没有额外创建随 n 增长的数据结构？
```

---

# 26. 时间复杂度分析口诀

```text
索引访问
→ O(1)

遍历一遍
→ O(n)

每次减半
→ O(log n)

高效排序
→ O(n log n)

两次 n 级操作嵌套
→ O(n²)
```

---

# 27. 数据结构选择口诀

```text
需要顺序数据
→ list


需要快速判断是否存在
→ set


需要 key → value
→ dict


需要统计频率
→ Counter


需要队列 / BFS
→ deque
```

---

# 28. 与 LeetCode 的联系

以后 LeetCode 经常会要求：

```text
时间复杂度：
O(?)

空间复杂度：
O(?)
```

做完题之后需要养成习惯：

```text
先写出解法
↓
分析时间复杂度
↓
分析空间复杂度
↓
看看能不能优化
```

例如：

```text
暴力查找
O(n²)

↓

使用 set / dict

↓

优化到 O(n)
```

这是后面算法学习中非常常见的路线。

---

# 29. Day11 完成情况

- [x] 时间复杂度概念
- [x] `O(1)`
- [x] `O(log n)`
- [x] `O(n)`
- [x] `O(n log n)`
- [x] `O(n²)`
- [x] 空间复杂度
- [x] `list` 查找复杂度
- [x] `set` 查找复杂度
- [x] `dict` key 查找复杂度
- [x] `append()` 基础复杂度
- [x] 哈希优化思想
- [x] `sorted()` 复杂度
- [x] 综合复杂度判断

# Day11 完成 ✅

---

## 知识关联

- 主题入口：[[maps/数据结构与算法|数据结构与算法]]
