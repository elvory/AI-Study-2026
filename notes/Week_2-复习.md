---
tags:
  - 主题/复习
  - 类型/周复习
aliases:
  - "Week02"
---

# Week02 复习总结

> 范围：Day08 ~ Day14

---

# 1. Day08：Python 数据处理

## enumerate()

同时获取：

```text
索引 + 元素
```

```python
for index, value in enumerate(nums):
    print(index, value)
```

注意顺序：

```text
index 在前
value 在后
```

---

## zip()

把多个序列相同位置的元素组合起来：

```python
names = ["A", "B"]
scores = [90, 95]

for name, score in zip(names, scores):
    print(name, score)
```

---

## sorted + lambda

例如按学生成绩从高到低排序：

```python
students = [
    {"name": "A", "score": 82},
    {"name": "B", "score": 95},
    {"name": "C", "score": 88}
]

result = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)
```

重点：

```text
sorted() 会把每个元素交给 key 函数
```

---

# 2. Day09：高级函数与装饰器

## *args

```text
接收多个位置参数
类型：tuple
```

```python
def func(*args):
    print(args)
```

---

## **kwargs

```text
接收多个关键字参数
类型：dict
```

```python
def func(**kwargs):
    print(kwargs)
```

---

## 装饰器结构

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print("函数开始执行")
        func(*args, **kwargs)

    return wrapper
```

使用：

```python
@log_call
def add(a, b):
    print(a + b)
```

调用：

```python
add(3, 5)
```

过程：

```text
add(3, 5)
↓
wrapper(3, 5)
↓
func(3, 5)
↓
原 add 执行
```

重点：

```text
外层装饰器接收函数
wrapper 接收实际参数
wrapper 再调用原函数
```

---

# 3. Day10：collections

## Counter

统计频率：

```python
from collections import Counter

nums = [3, 5, 3, 8, 5, 3]

count = Counter(nums)
```

结果：

```python
Counter({3: 3, 5: 2, 8: 1})
```

---

## most_common()

找最高频元素：

```python
count.most_common(2)
```

返回：

```python
[(3, 3), (5, 2)]
```

格式：

```text
(元素, 出现次数)
```

只取元素：

```python
[num for num, freq in count.most_common(2)]
```

---

## defaultdict(list)

适合：

```text
分组
```

例如异位词：

```python
from collections import defaultdict

groups = defaultdict(list)

for word in words:
    key = "".join(sorted(word))
    groups[key].append(word)
```

---

## deque

```python
from collections import deque
```

队列：

```text
先进先出 FIFO
```

```python
queue.append(x)
queue.popleft()
```

---

# 4. Day11：复杂度

## 常见复杂度

```text
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
```

## 常见操作

```text
list 按索引访问
→ O(1)

list 查找某个值
→ O(n)

set 判断元素存在
→ 平均 O(1)

dict key 查找
→ 平均 O(1)

sorted()
→ O(n log n)
```

---

# 5. Day12：数组、字符串、前缀和、双指针

## 前缀和

```python
nums = [3, 5, 2, 6]
```

前缀和：

```python
[0, 3, 8, 10, 16]
```

构造：

```python
prefix = [0]
running_sum = 0

for num in nums:
    running_sum += num
    prefix.append(running_sum)
```

---

## 区间和公式

区间：

```text
[L, R]
```

公式：

```text
prefix[R + 1] - prefix[L]
```

例如：

```text
L = 1
R = 3
```

```python
prefix[4] - prefix[1]
```

结果：

```text
13
```

复杂度：

```text
构建：O(n)
单次查询：O(1)
```

---

## 双指针

有序 Two Sum：

```text
sum < target
→ left 右移

sum > target
→ right 左移

sum == target
→ 找到
```

有序性让我们可以有方向地排除一半可能。

---

# 6. Day13：哈希

## set

适合：

```text
只判断元素是否出现
```

---

## dict

适合：

```text
key → 额外信息
```

Two Sum 中：

```text
数字 → 索引
```

---

## Two Sum

核心：

```python
seen = {}

for index, num in enumerate(nums):
    need = target - num

    if need in seen:
        print([seen[need], index])
        break

    seen[num] = index
```

重点：

```text
enumerate 返回：
index, num

seen 保存：
数字 → 索引
```

---

## 第一个不重复字符

```python
count = Counter(text)

for index, char in enumerate(text):
    if count[char] == 1:
        print(char)
        print(index)
        break
```

思路：

```text
第一遍统计频率
第二遍按原顺序找第一个频率为 1 的字符
```

---

# 7. Day14：栈和队列

## 栈 Stack

```text
后进先出 LIFO
```

```python
stack.append(x)
stack.pop()
stack[-1]
```

---

## 有效括号

核心：

```text
左括号
→ append()

右括号
→ 检查栈顶

匹配
→ pop()

不匹配
→ 非法
```

最终还必须：

```text
栈为空
```

才算完全匹配。

---

## 队列 Queue

```text
先进先出 FIFO
```

```python
queue.append(x)
queue.popleft()
queue[0]
```

---

# 8. Week02 易错点

## enumerate 顺序

正确：

```python
for index, num in enumerate(nums):
```

不是：

```python
for num, index in enumerate(nums):
```

---

## defaultdict 拼写

```python
defaultdict(list)
```

---

## 栈和队列

```text
栈：
append + pop

队列：
append + popleft
```

---

## Two Sum

```text
seen[num] = index
```

不是：

```text
seen[index] = num
```

---

## 前缀和

必须注意：

```text
[L, R]
→ prefix[R + 1] - prefix[L]
```

---

## sorted + lambda

如果元素是字典：

```python
key=lambda student: student["score"]
```

不是去索引整个列表。

---

## 装饰器

```text
装饰器外层
→ 接函数

wrapper
→ 接参数

wrapper 内
→ 调用原函数
```

---

# 9. Week02 掌握情况

- [x] enumerate
- [x] zip
- [x] sorted
- [x] lambda
- [x] *args
- [x] **kwargs
- [x] 装饰器
- [x] Counter
- [x] defaultdict
- [x] deque
- [x] 时间复杂度
- [x] 空间复杂度
- [x] 前缀和
- [x] 双指针
- [x] set / dict
- [x] Two Sum
- [x] 第一个不重复字符
- [x] 栈
- [x] 队列
- [x] 有效括号

# Week02 复习完成 ✅

---

## 知识关联

- 复习入口：[[maps/复习与实践|复习与实践]]
- 本周学习记录：[[notes/Day08-Python 数据处理进阶|Day08]] · [[notes/Day09-Python 函数进阶与高阶函数|Day09]] · [[notes/Day10-Python collections 常用工具|Day10]] · [[notes/Day11- 时间复杂度与空间复杂度基础|Day11]] · [[notes/Day12-数组、字符串与常见算法思想|Day12]] · [[notes/Day13-哈希表专题|Day13]] · [[notes/Day14-栈 Stack 与队列 Queue|Day14]]
