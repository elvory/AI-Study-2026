---
tags:
  - 主题/算法
  - 类型/每日笔记
aliases:
  - "Day13"
---

# Day13 - 哈希表专题

## 今日学习内容

- 哈希思想
- `set`
- `dict`
- `Counter`
- `defaultdict`
- 判断重复元素
- Two Sum
- 异位词
- 第一个不重复字符
- 数组交集
- 异位词分组
- Top K 高频元素

---

# 1. 什么是哈希思想

核心：

> 利用哈希结构快速判断一个值是否存在，或者快速找到对应信息。

常见结构：

```text
set
dict
Counter
defaultdict
```

---

# 2. 为什么叫哈希

大致流程：

```text
key
↓
hash
↓
映射到某个位置
↓
快速查找
```

因此：

```text
dict / set 查找
平均 O(1)
```

---

# 3. list 和哈希结构区别

```text
list

按索引访问
→ O(1)

按值查找
→ O(n)
```

```text
set / dict

查 key / 判断存在
→ 平均 O(1)
```

---

# 4. 哈希结构选择

```text
判断是否出现
→ set

保存 key → 信息
→ dict

统计次数
→ Counter / dict

分组
→ defaultdict(list)
```

---

# 5. 判断重复元素

例如：

```python
nums = [5, 3, 8, 1, 3]
```

使用：

```python
seen = set()

for num in nums:
    if num in seen:
        print(f"有重复元素：{num}")

    seen.add(num)
```

输出：

```text
有重复元素：3
```

---

# 6. 判断重复元素思路

```text
从左到右
↓
当前 num 是否在 seen
↓
如果在
→ 重复

如果不在
→ 加入 seen
```

复杂度：

```text
时间：O(n)
空间：O(n)
```

---

# 7. Two Sum + dict

```python
nums = [3, 8, 5, 12]
target = 13
```

核心：

```text
need = target - num
```

保存：

```text
数字 → 索引
```

代码：

```python
seen = {}

for index, num in enumerate(nums):
    need = target - num

    if need in seen:
        print([seen[need], index])

    seen[num] = index
```

结果：

```text
[1, 2]
```

---

# 8. Two Sum 核心流程

```text
遍历 num
↓
need = target - num
↓
查 need 是否在 seen
↓
存在 → 找到
↓
不存在 → 保存 num:index
```

时间：

```text
O(n)
```

空间：

```text
O(n)
```

---

# 9. Counter

用于：

> 统计元素出现次数。

例如：

```python
from collections import Counter

s = "swiss"

count = Counter(s)
```

得到：

```text
s → 3
w → 1
i → 1
```

---

# 10. 异位词判断

例如：

```python
s = "listen"
t = "silent"
```

代码：

```python
if Counter(s) == Counter(t):
    print("是异位词")
else:
    print("不是异位词")
```

核心：

```text
两个字符串
↓
字符频率完全一样
↓
异位词
```

---

# 11. 第一个不重复字符

```python
s = "swiss"

count_s = Counter(s)

for char in s:
    if count_s[char] == 1:
        print(char)
        break
```

输出：

```text
w
```

---

# 12. 为什么需要二次遍历

第一次：

```text
统计频率
```

第二次：

```text
按原顺序找第一个 count == 1
```

所以：

```text
O(n) + O(n)
= O(n)
```

不是：

```text
O(n²)
```

---

# 13. 两个数组求交集

```python
nums1 = [2, 5, 7, 9]
nums2 = [1, 5, 8, 9]
```

代码：

```python
nums2_set = set(nums2)

result = []

for num in nums1:
    if num in nums2_set:
        result.append(num)

print(result)
```

输出：

```python
[5, 9]
```

---

# 14. 数组交集复杂度

假设：

```text
nums1 长度 = n
nums2 长度 = m
```

则：

```text
建立 set(nums2)
→ O(m)

遍历 nums1
→ O(n)

set 查找
→ 平均 O(1)
```

总时间：

```text
O(n + m)
```

空间：

```text
O(m)
```

---

# 15. defaultdict(list)

用于：

> 一个 key 对应多个 value 的分组问题。

例如：

```python
groups = defaultdict(list)
```

如果某个 key 不存在：

```python
groups[key]
```

会自动创建：

```python
[]
```

---

# 16. 异位词分组

例如：

```python
words = [
    "eat",
    "tea",
    "tan",
    "ate",
    "nat",
    "bat"
]
```

关键：

> 给每个单词提取一个统一特征 key。

---

# 17. 排序后的字符串作为 key

例如：

```text
eat → aet
tea → aet
ate → aet

tan → ant
nat → ant

bat → abt
```

代码：

```python
groups = defaultdict(list)

for word in words:
    key = "".join(sorted(word))
    groups[key].append(word)
```

结果：

```text
"aet"
→ ["eat", "tea", "ate"]

"ant"
→ ["tan", "nat"]

"abt"
→ ["bat"]
```

---

# 18. "".join(sorted(word))

例如：

```python
sorted("tea")
```

得到：

```python
['a', 'e', 't']
```

再：

```python
"".join(sorted("tea"))
```

得到：

```text
"aet"
```

这个写法要重点记住。

---

# 19. Top K 高频元素

例如：

```python
nums = [4, 4, 1, 1, 1, 2, 2, 3]
k = 2
```

统计：

```text
1 → 3
4 → 2
2 → 2
3 → 1
```

---

# 20. most_common(k)

```python
count = Counter(nums)

most_common = count.most_common(k)
```

可能得到：

```python
[(1, 3), (4, 2)]
```

每个元组：

```text
(元素, 出现次数)
```

---

# 21. 只取 Top K 元素

```python
result = [
    num
    for num, freq in most_common
]
```

结果：

```python
[1, 4]
```

这里：

```text
num
→ 元素

freq
→ 出现次数
```

---

# 22. set / dict / Counter / defaultdict 总结

```text
set
→ 判断是否存在

dict
→ 保存 key → value

Counter
→ 统计次数

defaultdict(list)
→ 分组
```

---

# 23. Day13 哈希思维地图

```text
有没有出现过？
→ set

在哪里？
→ dict

出现几次？
→ Counter

属于哪一组？
→ defaultdict(list)

找配对值？
→ dict / set

找重复？
→ set

字符频率？
→ Counter
```

---

# 24. 今日核心题型

```text
重复元素
→ set

Two Sum
→ dict

异位词
→ Counter

第一个不重复字符
→ Counter + 二次遍历

数组交集
→ set

异位词分组
→ defaultdict(list)

Top K 高频
→ Counter.most_common()
```

---

# 25. 今日易忘点

## 1. 空 set

正确：

```python
seen = set()
```

而：

```python
{}
```

是空字典。

---

## 2. enumerate()

```python
for index, num in enumerate(nums):
```

同时得到：

```text
index
num
```

---

## 3. dict 存索引

```python
seen[num] = index
```

表示：

```text
数字 → 索引
```

---

## 4. Counter 比较

```python
Counter(s) == Counter(t)
```

可以判断两个字符串字符频率是否一致。

---

## 5. defaultdict(list)

```python
groups[key].append(word)
```

第一次遇到 key 时，会自动创建空列表。

---

## 6. 异位词统一 key

```python
key = "".join(sorted(word))
```

这个写法重点记。

---

# 26. Day13 完成情况

- [x] 哈希思想
- [x] set
- [x] dict
- [x] Counter
- [x] defaultdict
- [x] 重复元素
- [x] Two Sum
- [x] 异位词
- [x] 第一个不重复字符
- [x] 两数组交集
- [x] 异位词分组
- [x] Top K 高频元素
- [x] 理论转代码实操

# Day13 完成 ✅

---

## 知识关联

- 主题入口：[[maps/数据结构与算法|数据结构与算法]]
- 相关知识：[[notes/Day10-Python collections 常用工具|Day10]]
