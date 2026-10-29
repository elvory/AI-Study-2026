---
tags:
  - 主题/Python
  - 类型/每日笔记
aliases:
  - "Day10"
---

# Day10 - Python collections 常用工具

## 今日学习内容

- `Counter`
- `Counter.most_common()`
- `defaultdict`
- `defaultdict(list)`
- `defaultdict(int)`
- `defaultdict(set)`
- `deque`
- `append()`
- `appendleft()`
- `pop()`
- `popleft()`

---

# 1. collections 模块

Python 标准库提供了：

```python
collections
```

里面包含一些非常实用的数据结构和工具。

Day10 主要学习：

```python
Counter
defaultdict
deque
```

这些工具以后在：

- LeetCode
- 数据处理
- BFS
- 字符统计
- 分组问题

中都会经常使用。

---

# 2. Counter

`Counter` 用来：

> 统计可迭代对象中每个元素出现的次数。

首先导入：

```python
from collections import Counter
```

例如：

```python
numbers = [1, 2, 2, 3, 3, 3]

count = Counter(numbers)

print(count)
```

输出：

```text
Counter({3: 3, 2: 2, 1: 1})
```

含义：

```text
1 出现 1 次
2 出现 2 次
3 出现 3 次
```

---

# 3. Counter 统计单词

例如：

```python
from collections import Counter

words = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple"
]

count = Counter(words)

print(count)
```

输出：

```text
Counter({'apple': 3, 'banana': 2, 'orange': 1})
```

可以直接访问：

```python
print(count["apple"])
```

输出：

```text
3
```

说明：

```text
apple 出现了 3 次
```

---

# 4. Counter 的本质

可以把 `Counter` 暂时理解为：

> 专门用于统计元素频率的字典。

例如：

```python
count["apple"]
```

得到：

```text
3
```

对应关系：

```text
key   → 元素
value → 出现次数
```

---

# 5. Counter 和普通字典统计

普通写法：

```python
words = [
    "apple",
    "banana",
    "apple"
]

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
```

使用 `Counter`：

```python
count = Counter(words)
```

明显更加简洁。

---

# 6. most_common()

`Counter` 提供：

```python
most_common()
```

用于：

> 按照出现次数从高到低排列。

例如：

```python
print(count.most_common())
```

输出：

```python
[
    ("apple", 3),
    ("banana", 2),
    ("orange", 1)
]
```

---

# 7. most_common(n)

如果只想取出现次数最多的前几个元素：

```python
count.most_common(2)
```

输出：

```python
[
    ("apple", 3),
    ("banana", 2)
]
```

所以：

```text
most_common()
↓
返回全部，按频率从高到低排列
```

```text
most_common(2)
↓
返回频率最高的前 2 个
```

---

# 8. most_common() 的返回类型

例如：

```python
count.most_common()
```

返回：

```python
[
    ("apple", 3),
    ("banana", 2),
    ("orange", 1)
]
```

这是：

```text
list
```

里面的每个元素是：

```text
tuple
```

也就是：

```text
list[tuple]
```

每个元组：

```python
("apple", 3)
```

表示：

```text
元素     出现次数
apple      3
```

---

# 9. Counter 常见使用场景

以后 LeetCode 中经常会遇到：

```text
字符出现次数
单词出现次数
元素频率
多数元素
Top K 高频元素
异位词
```

这些问题都可能使用：

```python
Counter
```

---

# 10. defaultdict

首先导入：

```python
from collections import defaultdict
```

`defaultdict` 可以理解为：

> 当字典中的 key 不存在时，自动创建一个默认值。

---

# 11. 普通 dict 的问题

例如：

```python
groups = {}
```

如果直接：

```python
groups["AI"].append("Alice")
```

会报错：

```text
KeyError
```

因为：

```python
groups["AI"]
```

还不存在。

---

# 12. 普通字典的解决方式

通常需要：

```python
if "AI" not in groups:
    groups["AI"] = []

groups["AI"].append("Alice")
```

如果很多数据需要分组，这样会比较麻烦。

---

# 13. defaultdict(list)

可以直接：

```python
groups = defaultdict(list)
```

意思：

> 如果 key 不存在，就自动创建一个空列表 `[]`。

例如：

```python
groups["AI"].append("Alice")
```

第一次访问 `"AI"` 时：

Python 相当于自动执行：

```python
groups["AI"] = []
```

然后：

```python
groups["AI"].append("Alice")
```

---

# 14. defaultdict 分组练习

原始数据：

```python
students = [
    ("Alice", "AI"),
    ("Bob", "CS"),
    ("Charlie", "AI"),
    ("David", "CS"),
    ("Eva", "AI")
]
```

按照专业分组：

```python
from collections import defaultdict

student_major_count = defaultdict(list)

for student, major in students:
    student_major_count[major].append(student)

print(student_major_count)
```

结果：

```python
{
    "AI": ["Alice", "Charlie", "Eva"],
    "CS": ["Bob", "David"]
}
```

---

# 15. 分组过程理解

第一次：

```python
("Alice", "AI")
```

执行：

```python
student_major_count["AI"].append("Alice")
```

由于：

```python
"AI"
```

不存在，

`defaultdict(list)` 自动创建：

```python
"AI": []
```

然后变成：

```python
"AI": ["Alice"]
```

接下来：

```python
("Charlie", "AI")
```

继续：

```python
student_major_count["AI"].append("Charlie")
```

结果：

```python
"AI": ["Alice", "Charlie"]
```

---

# 16. defaultdict(int)

可以：

```python
count = defaultdict(int)
```

默认值：

```text
0
```

例如：

```python
count["apple"] += 1
```

第一次 `"apple"` 不存在：

相当于：

```python
count["apple"] = 0
```

然后：

```python
count["apple"] += 1
```

变成：

```text
1
```

---

# 17. defaultdict(set)

还可以：

```python
groups = defaultdict(set)
```

默认值：

```python
set()
```

适合：

> 每个 key 对应一组不重复的数据。

---

# 18. defaultdict 常见默认值

```text
defaultdict(list)
↓
默认 []
↓
常用于分组
```

```text
defaultdict(int)
↓
默认 0
↓
常用于计数
```

```text
defaultdict(set)
↓
默认 set()
↓
常用于保存不重复的数据
```

---

# 19. defaultdict 和普通 dict 区别

普通字典：

```python
d = {}

print(d["x"])
```

结果：

```text
KeyError
```

而：

```python
d = defaultdict(int)

print(d["x"])
```

结果：

```text
0
```

因为 `defaultdict` 会自动创建默认值。

---

# 20. deque

首先导入：

```python
from collections import deque
```

`deque` 全称：

```text
double-ended queue
```

中文：

> 双端队列

它支持从：

```text
左边
右边
```

高效地添加和删除元素。

---

# 21. 创建 deque

例如：

```python
from collections import deque

queue = deque([10, 20, 30])
```

此时：

```text
左边            右边

10   20   30
```

---

# 22. append()

```python
queue.append(40)
```

作用：

> 从右边添加元素。

结果：

```python
deque([10, 20, 30, 40])
```

---

# 23. appendleft()

```python
queue.appendleft(0)
```

作用：

> 从左边添加元素。

结果：

```python
deque([0, 10, 20, 30, 40])
```

---

# 24. pop()

```python
queue.pop()
```

作用：

> 删除并返回最右边的元素。

例如：

```python
deque([0, 10, 20, 30, 40])
```

执行：

```python
queue.pop()
```

删除：

```text
40
```

剩下：

```python
deque([0, 10, 20, 30])
```

---

# 25. popleft()

```python
queue.popleft()
```

作用：

> 删除并返回最左边的元素。

例如：

```python
deque([0, 10, 20, 30])
```

执行：

```python
queue.popleft()
```

删除：

```text
0
```

剩下：

```python
deque([10, 20, 30])
```

---

# 26. deque 四个核心方法

```text
append()
↓
右边添加


appendleft()
↓
左边添加


pop()
↓
右边删除


popleft()
↓
左边删除
```

可以画成：

```text
appendleft()                     append()
      ↓                             ↓

   [ 10 | 20 | 30 ]

      ↑                             ↑
 popleft()                        pop()
```

---

# 27. deque 综合练习

初始：

```python
queue = deque([10, 20, 30])
```

右边加入：

```python
queue.append(40)
```

结果：

```python
deque([10, 20, 30, 40])
```

左边加入：

```python
queue.appendleft(0)
```

结果：

```python
deque([0, 10, 20, 30, 40])
```

删除右边：

```python
queue.pop()
```

结果：

```python
deque([0, 10, 20, 30])
```

删除左边：

```python
queue.popleft()
```

最终：

```python
deque([10, 20, 30])
```

---

# 28. deque 和 queue 思想

队列常见特点：

```text
先进先出
FIFO
First In First Out
```

例如：

```text
进入：

A → B → C
```

最先出来的是：

```text
A
```

Python 中以后做 BFS 经常：

```python
queue = deque()
```

添加：

```python
queue.append(node)
```

取出最前面的：

```python
node = queue.popleft()
```

---

# 29. BFS 常见模板预览

以后学习 BFS 时，经常会看到：

```python
from collections import deque

queue = deque()

queue.append(start)

while queue:

    node = queue.popleft()

    # 处理 node
```

现在暂时不用掌握 BFS。

只需要知道：

```text
deque
+
append()
+
popleft()
```

以后会非常常见。

---

# 30. 为什么不用 list 做队列

Python 的：

```python
list
```

很适合：

```python
append()
pop()
```

从右边操作。

但如果频繁：

```python
pop(0)
```

从最左边删除，就不够高效。

而：

```python
deque.popleft()
```

就是专门为这种场景设计的。

所以以后：

```text
栈
↓
list 常常可以


队列 / BFS
↓
优先考虑 deque
```

---

# 31. Counter / defaultdict / deque 对比

## Counter

```text
作用：
统计频率
```

典型：

```python
Counter(words)
```

---

## defaultdict

```text
作用：
不存在 key 时自动创建默认值
```

典型：

```python
defaultdict(list)
```

用于：

```text
分组
```

---

## deque

```text
作用：
双端队列
```

典型：

```python
queue.append()
queue.popleft()
```

用于：

```text
队列
BFS
```

---

# 32. 今日核心知识链

```text
collections
│
├── Counter
│   ├── 统计频率
│   ├── count[element]
│   └── most_common()
│
├── defaultdict
│   ├── 自动创建默认值
│   ├── defaultdict(list)
│   ├── defaultdict(int)
│   └── defaultdict(set)
│
└── deque
    ├── append()
    ├── appendleft()
    ├── pop()
    └── popleft()
```

---

# 33. 今日快速记忆

```text
Counter
↓
统计元素出现次数


most_common(n)
↓
出现次数最多的前 n 个


defaultdict(list)
↓
不存在 key 时自动创建 []


defaultdict(int)
↓
不存在 key 时自动创建 0


defaultdict(set)
↓
不存在 key 时自动创建 set()


deque
↓
双端队列


append()
↓
右加


appendleft()
↓
左加


pop()
↓
右删


popleft()
↓
左删
```

---

# 34. LeetCode 联系

以后看到：

```text
统计出现次数
```

可以想到：

```python
Counter
```

看到：

```text
按照某个 key 分组
```

可以想到：

```python
defaultdict(list)
```

看到：

```text
队列
BFS
层序遍历
```

可以想到：

```python
deque
```

---

# 35. Day10 完成情况

- [x] `collections`
- [x] `Counter`
- [x] Counter 统计频率
- [x] `count[element]`
- [x] `most_common()`
- [x] `most_common(n)`
- [x] `defaultdict`
- [x] `defaultdict(list)`
- [x] `defaultdict(int)`
- [x] `defaultdict(set)`
- [x] 使用 defaultdict 分组
- [x] `deque`
- [x] `append()`
- [x] `appendleft()`
- [x] `pop()`
- [x] `popleft()`
- [x] 队列基本思想
- [x] BFS 使用场景初步了解

# Day10 完成 ✅

---

## 知识关联

- 主题入口：[[maps/Python基础|Python基础]]
- 相关知识：[[notes/Day13-哈希表专题|Day13]] · [[notes/Day14-栈 Stack 与队列 Queue|Day14]]
