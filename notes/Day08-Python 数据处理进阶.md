---
tags:
  - 主题/Python
  - 类型/每日笔记
aliases:
  - "Day08"
---

# Day08 - Python 数据处理进阶

## 今日学习内容

- 列表推导式
- 字典推导式
- `enumerate()`
- `zip()`
- 元组解包
- `sorted()`
- `reverse=True`
- `key=`
- `lambda`
- 综合练习

---

# 1. 列表推导式 List Comprehension

列表推导式可以用更简洁的方式创建一个新的列表。

## 基本语法

```python
[表达式 for 变量 in 可迭代对象]
```

如果需要筛选：

```python
[表达式 for 变量 in 可迭代对象 if 条件]
```

---

## 示例 1：筛选奇数

普通写法：

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = []

for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

print(odd_numbers)
```

列表推导式：

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = [
    num
    for num in numbers
    if num % 2 != 0
]

print(odd_numbers)
```

输出：

```text
[1, 3, 5, 7, 9]
```

---

## 示例 2：筛选偶数并计算平方

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [
    num ** 2
    for num in numbers
    if num % 2 == 0
]

print(squares)
```

输出：

```text
[4, 16, 36, 64, 100]
```

---

## 核心结构

```text
[放入新列表的内容 for 变量 in 原数据 if 条件]
```

例如：

```python
[num ** 2 for num in numbers if num % 2 == 0]
```

可以拆成：

```text
num ** 2
↓
新列表中要保存什么

for num in numbers
↓
遍历数据

if num % 2 == 0
↓
筛选条件
```

---

# 2. 字典推导式 Dict Comprehension

字典推导式可以快速创建字典。

## 基本语法

```python
{key: value for 变量 in 可迭代对象}
```

带条件：

```python
{key: value for 变量 in 可迭代对象 if 条件}
```

---

## 示例：偶数及其平方

```python
numbers = [1, 2, 3, 4, 5, 6]

squares = {
    num: num ** 2
    for num in numbers
    if num % 2 == 0
}

print(squares)
```

输出：

```python
{2: 4, 4: 16, 6: 36}
```

其中：

```text
key   → num
value → num ** 2
```

---

# 3. 列表、集合、字典推导式的区别

## 列表推导式

使用：

```python
[]
```

例如：

```python
[name for name, score in students]
```

结果：

```python
["Alice", "Bob"]
```

---

## 集合推导式

使用：

```python
{}
```

但是里面没有：

```text
key: value
```

例如：

```python
{name for name, score in students}
```

结果是：

```python
{"Alice", "Bob"}
```

---

## 字典推导式

使用：

```python
{key: value}
```

例如：

```python
{name: score for name, score in students}
```

结果：

```python
{
    "Alice": 88,
    "Bob": 95
}
```

---

## 快速记忆

```text
[]             → list

{value}        → set

{key: value}   → dict
```

---

# 4. enumerate()

当遍历一个序列时，如果同时需要：

- 索引
- 元素

可以使用：

```python
enumerate()
```

---

## 普通写法

```python
students = ["Alice", "Bob", "Charlie"]

for i in range(len(students)):
    print(i, students[i])
```

---

## enumerate 写法

```python
students = ["Alice", "Bob", "Charlie"]

for i, name in enumerate(students):
    print(i, name)
```

输出：

```text
0 Alice
1 Bob
2 Charlie
```

---

## 从 1 开始编号

默认情况下：

```python
enumerate()
```

从：

```text
0
```

开始。

如果想从 1 开始：

```python
students = ["Alice", "Bob", "Charlie"]

for i, name in enumerate(students, start=1):
    print(i, name)
```

输出：

```text
1 Alice
2 Bob
3 Charlie
```

---

## 核心理解

```text
enumerate()
=
索引 + 元素
```

适用于：

```text
既需要元素本身
又需要元素位置
```

---

# 5. zip()

`zip()` 用于：

> 将多个可迭代对象中相同位置的元素配对。

例如：

```python
products = ["苹果", "香蕉", "橙子"]

prices = [5, 3, 6]
```

使用：

```python
for product, price in zip(products, prices):
    print(product, price)
```

输出：

```text
苹果 5
香蕉 3
橙子 6
```

---

## 可以理解为

```text
products      prices

苹果    ←→      5

香蕉    ←→      3

橙子    ←→      6
```

每次循环相当于得到：

```python
("苹果", 5)

("香蕉", 3)

("橙子", 6)
```

---

## zip 和解包

下面：

```python
for product, price in zip(products, prices):
```

实际上包含两件事情：

```text
zip()
↓
负责配对

product, price
↓
负责解包
```

所以：

```text
zip() ≠ 解包

zip() → 配对

变量1, 变量2 → 解包
```

---

# 6. zip() 长度不一致

例如：

```python
names = ["A", "B", "C"]

scores = [90, 80]
```

使用：

```python
for name, score in zip(names, scores):
    print(name, score)
```

输出：

```text
A 90
B 80
```

`C` 不会被处理。

原因：

> `zip()` 会按照最短的可迭代对象结束。

---

# 7. 元组解包 Tuple Unpacking

例如：

```python
student = ("Alice", 88)
```

可以：

```python
name, score = student
```

此时：

```python
name
```

得到：

```text
Alice
```

而：

```python
score
```

得到：

```text
88
```

---

## 等价于

```python
name = student[0]

score = student[1]
```

---

## 在循环中解包

例如：

```python
students = [
    ("Alice", 88),
    ("Bob", 95),
    ("Charlie", 72)
]

for name, score in students:
    print(name, score)
```

每一次循环：

```text
("Alice", 88)

↓ 解包

name = "Alice"
score = 88
```

---

# 8. sorted()

`sorted()` 用于对数据进行排序。

## 升序排列

```python
numbers = [5, 2, 8, 1, 3]

result = sorted(numbers)

print(result)
```

输出：

```python
[1, 2, 3, 5, 8]
```

---

# 9. reverse=True

如果需要降序：

```python
scores = [88, 95, 72, 100, 85]

sorted_scores = sorted(
    scores,
    reverse=True
)

print(sorted_scores)
```

输出：

```python
[100, 95, 88, 85, 72]
```

所以：

```text
reverse=False
```

默认：

```text
从小到大
```

而：

```text
reverse=True
```

表示：

```text
从大到小
```

---

# 10. sorted() 和 .sort() 的区别

这是一个重要区别。

## sorted()

```python
numbers = [3, 1, 2]

new_numbers = sorted(numbers)
```

特点：

- Python 内置函数
- 返回一个新的列表
- 不修改原列表

结果：

```python
numbers
```

还是：

```python
[3, 1, 2]
```

而：

```python
new_numbers
```

是：

```python
[1, 2, 3]
```

---

## .sort()

```python
numbers = [3, 1, 2]

numbers.sort()
```

特点：

- `list` 的方法
- 直接修改原列表
- 不返回新的排序列表

现在：

```python
numbers
```

变成：

```python
[1, 2, 3]
```

---

## 快速记忆

```text
sorted()
↓
返回新列表
不修改原数据


.sort()
↓
直接修改原列表
```

---

# 11. key=

`key=` 用来：

> 指定排序依据。

例如：

```python
students = [
    ("Alice", 88),
    ("Bob", 95),
    ("Charlie", 72),
    ("David", 100)
]
```

每个学生都是：

```python
("Alice", 88)
```

其中：

```python
student[0]
```

是：

```text
Alice
```

而：

```python
student[1]
```

是：

```text
88
```

---

## 定义一个函数取成绩

```python
def get_score(student):
    return student[1]
```

测试：

```python
print(get_score(("Alice", 88)))
```

输出：

```text
88
```

---

## 使用 key 排序

```python
sorted_students = sorted(
    students,
    key=get_score
)
```

意思是：

> 对 `students` 排序，但是排序的时候使用 `get_score(student)` 返回的成绩作为依据。

Python 可以理解为：

```text
("Alice", 88)
↓
get_score()
↓
88


("Bob", 95)
↓
get_score()
↓
95
```

真正参与比较的是：

```text
88
95
72
100
```

但是最终排列的仍然是：

```python
("Alice", 88)
```

这样的学生数据。

---

# 12. key= 不是筛选

这一点需要注意。

```text
if
↓
筛选数据


key=
↓
指定排序依据
```

例如：

```python
if score >= 90
```

意思是：

> 只留下成绩大于等于 90 的数据。

而：

```python
key=lambda student: student[1]
```

意思是：

> 排序时按照成绩进行比较。

---

# 13. lambda

`lambda` 可以创建一个简单的匿名函数。

## 基本语法

```python
lambda 参数: 返回值
```

例如：

```python
lambda x: x * 2
```

意思：

> 接收一个 x，然后返回 x * 2。

如果传入：

```text
5
```

返回：

```text
10
```

---

# 14. lambda 和普通函数

普通函数：

```python
def get_score(student):
    return student[1]
```

可以写成：

```python
lambda student: student[1]
```

两者核心作用相同：

```text
接收 student

↓

返回 student[1]
```

---

# 15. sorted() + lambda

原来的写法：

```python
def get_score(student):
    return student[1]

sorted_students = sorted(
    students,
    key=get_score,
    reverse=True
)
```

可以简化成：

```python
sorted_students = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)
```

---

## 完整理解

```python
sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)
```

可以翻译成：

```text
对 students 排序

↓

排序的时候取 student[1]

↓

student[1] 是成绩

↓

按照成绩排序

↓

reverse=True

↓

成绩从高到低
```

---

# 16. lambda 参数必须前后一致

错误写法：

```python
lambda studnet: student[1]
```

这里：

```text
studnet
```

和：

```text
student
```

不是同一个变量。

会报：

```text
NameError
```

正确：

```python
lambda student: student[1]
```

---

# 17. Day08 综合练习

原始数据：

```python
students = [
    ("Alice", 88),
    ("Bob", 95),
    ("Charlie", 72),
    ("David", 100),
    ("Eva", 85)
]
```

---

## 综合练习 1：按成绩从高到低排序

```python
sorted_students = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print(sorted_students)
```

结果：

```python
[
    ("David", 100),
    ("Bob", 95),
    ("Alice", 88),
    ("Eva", 85),
    ("Charlie", 72)
]
```

---

# 18. 使用 enumerate 添加排名

因为已经排好序，所以应该遍历：

```python
sorted_students
```

而不是原来的：

```python
students
```

代码：

```python
for rank, student in enumerate(
    sorted_students,
    start=1
):
    print(rank, student)
```

输出：

```text
1 ('David', 100)

2 ('Bob', 95)

3 ('Alice', 88)

4 ('Eva', 85)

5 ('Charlie', 72)
```

---

# 19. 找出成绩 >= 90 的学生姓名

使用列表推导式：

```python
students_names = [
    name
    for name, score in students
    if score >= 90
]

print(students_names)
```

结果：

```python
["Bob", "David"]
```

这里：

```text
name
↓
放入新列表的内容


for name, score in students
↓
遍历并解包


if score >= 90
↓
筛选条件
```

---

# 20. 把学生转换成字典

要求：

```text
key   → 姓名

value → 成绩
```

代码：

```python
students_dict = {
    name: score
    for name, score in students
}

print(students_dict)
```

结果：

```python
{
    "Alice": 88,
    "Bob": 95,
    "Charlie": 72,
    "David": 100,
    "Eva": 85
}
```

---

# 21. Day08 综合代码

```python
students = [
    ("Alice", 88),
    ("Bob", 95),
    ("Charlie", 72),
    ("David", 100),
    ("Eva", 85)
]


# 1. 按成绩从高到低排序

sorted_students = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print(sorted_students)


# 2. 给学生添加排名

for rank, student in enumerate(
    sorted_students,
    start=1
):
    print(rank, student)


# 3. 找出成绩 >= 90 的学生姓名

students_names = [
    name
    for name, score in students
    if score >= 90
]

print(students_names)


# 4. 将学生信息转换为字典

students_dict = {
    name: score
    for name, score in students
}

print(students_dict)
```

---

# 22. 今日踩坑记录

## 坑 1：reverse 拼写错误

错误：

```python
reversed=True
```

正确：

```python
reverse=True
```

---

## 坑 2：reverse 写到了 print() 里面

错误：

```python
print(sorted_scores, reverse=True)
```

`print()` 没有这个参数。

正确：

```python
sorted_scores = sorted(
    scores,
    reverse=True
)

print(sorted_scores)
```

---

## 坑 3：lambda 参数拼写不一致

错误：

```python
lambda studnet: student[1]
```

正确：

```python
lambda student: student[1]
```

原则：

> 参数定义叫什么，后面就必须用相同的变量名。

---

## 坑 4：enumerate 遍历错数据

已经得到：

```python
sorted_students
```

如果要生成排名：

错误：

```python
enumerate(students, start=1)
```

正确：

```python
enumerate(sorted_students, start=1)
```

因为：

> 排名应该基于排序后的结果。

---

## 坑 5：把列表推导式写成字典推导式

如果要求：

```python
["Bob", "David"]
```

应该使用：

```python
[
    name
    for name, score in students
    if score >= 90
]
```

而不是：

```python
{
    name: name
    for name, score in students
    if score >= 90
}
```

因为：

```text
[] → list

{} + key:value → dict
```

---

## 坑 6：把字典推导式写成集合推导式

错误：

```python
{
    (name, score)
    for name, score in students
}
```

这是：

```text
set
```

正确字典推导式：

```python
{
    name: score
    for name, score in students
}
```

---

# 23. 今日核心知识总结

## 列表推导式

```python
[结果 for 变量 in 数据 if 条件]
```

用途：

```text
遍历
+
筛选
+
转换
```

---

## 字典推导式

```python
{
    key: value
    for 变量 in 数据
    if 条件
}
```

---

## enumerate()

```text
索引 + 元素
```

常见：

```python
for index, value in enumerate(data):
```

---

## zip()

```text
将多个可迭代对象相同位置的数据配对
```

例如：

```python
zip(names, scores)
```

---

## 元组解包

```python
name, score = ("Alice", 88)
```

---

## sorted()

```text
排序
+
返回新列表
+
不修改原数据
```

---

## .sort()

```text
直接修改原列表
```

---

## reverse=True

```text
降序排序
```

---

## key=

```text
指定排序依据
```

---

## lambda

```python
lambda 参数: 返回值
```

例如：

```python
lambda student: student[1]
```

意思：

```text
接收 student
↓
返回 student[1]
```

---

# 24. 今日快速记忆

```text
列表推导式
[结果 for x in data if 条件]


字典推导式
{key: value for x in data}


enumerate()
索引 + 元素


zip()
对应位置元素配对


元组解包
name, score = student


sorted()
排序并返回新列表


.sort()
修改原列表


reverse=True
从大到小


key=
指定排序依据


lambda
lambda 参数: 返回值
```

---

# 25. Day08 完成情况

- [x] 列表推导式
- [x] 字典推导式
- [x] 列表 / 集合 / 字典推导式区别
- [x] `enumerate()`
- [x] `enumerate(start=1)`
- [x] `zip()`
- [x] 元组解包
- [x] `sorted()`
- [x] `.sort()` 与 `sorted()` 区别
- [x] `reverse=True`
- [x] `key=`
- [x] `lambda`
- [x] `sorted() + lambda`
- [x] 综合练习
- [x] 错误排查
- [x] 知识回顾

# Day08 完成 ✅

---

## 知识关联

- 主题入口：[[maps/Python基础|Python基础]]
