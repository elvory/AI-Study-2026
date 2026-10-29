---
tags:
  - 主题/算法
  - 类型/每日笔记
aliases:
  - "Day12"
---

# Day12 - 数组、字符串与常见算法思想

## 今日学习内容

- 数组基础
- 字符串基础
- 遍历 + 状态维护
- 前缀和 Prefix Sum
- 区间和
- 左右双指针
- 回文判断
- 有序数组 Two Sum
- 无序数组 Two Sum + 哈希
- 快慢指针

---

# 1. 数组基础

Python 中算法题通常使用：

```python
nums = [10, 20, 30, 40]
```

来表示数组。

索引：

```text
索引    0   1   2   3
数据   10  20  30  40
```

按索引访问：

```python
nums[2]
```

得到：

```text
30
```

时间复杂度：

```text
O(1)
```

---

# 2. 数组常见操作复杂度

```text
按索引访问 nums[i]
→ O(1)

修改 nums[i]
→ O(1)

查找 x in nums
→ O(n)

遍历整个数组
→ O(n)

append()
→ 平均 O(1)

头部 / 中间插入
→ O(n)
```

---

# 3. 字符串基础

例如：

```python
text = "hello"
```

可以理解成：

```text
索引    0   1   2   3   4
字符    h   e   l   l   o
```

访问：

```python
text[1]
```

结果：

```text
e
```

时间复杂度：

```text
O(1)
```

---

# 4. Python 字符串不可变

字符串是：

```text
immutable
```

不能：

```python
text[0] = "H"
```

如果需要修改，实际上要生成新的字符串。

---

# 5. 遍历 + 状态维护

很多数组问题的基础模式：

```text
遍历
+
维护当前状态
```

例如找最小值：

```text
nums = [7, 3, 9, 2, 8]

current_min = 7

看到 3 → current_min = 3
看到 9 → current_min = 3
看到 2 → current_min = 2
看到 8 → current_min = 2
```

最终：

```text
2
```

常见状态：

```text
当前最大值
当前最小值
累计和
当前次数
当前最优答案
```

---

# 6. 前缀和 Prefix Sum

例如：

```python
nums = [3, 5, 2, 6]
```

前缀和：

```python
prefix = [0, 3, 8, 10, 16]
```

含义：

```text
prefix[0] = 0
prefix[1] = 前1个元素和
prefix[2] = 前2个元素和
prefix[3] = 前3个元素和
prefix[4] = 前4个元素和
```

---

# 7. 构造前缀和

```python
nums = [3, 5, 2, 6]

prefix = [0]
current_sum = 0

for num in nums:
    current_sum += num
    prefix.append(current_sum)

print(prefix)
```

输出：

```python
[0, 3, 8, 10, 16]
```

---

# 8. 为什么 prefix 前面放 0

为了统一区间和公式。

区间：

```text
[L, R]
```

区间和：

```text
prefix[R + 1] - prefix[L]
```

例如：

```python
nums = [3, 5, 2, 6]
```

索引 `1` 到 `3`：

```text
5 + 2 + 6 = 13
```

使用：

```python
prefix[4] - prefix[1]
```

得到：

```text
16 - 3 = 13
```

---

# 9. 前缀和复杂度

构造：

```text
O(n)
```

单次区间查询：

```text
O(1)
```

如果有 `m` 次查询：

不用前缀和：

```text
O(mn)
```

使用前缀和：

```text
O(n + m)
```

---

# 10. 前缀和核心思想

```text
先预处理
↓
后续查询变快
```

类似：

```text
list → set
```

都是：

> 用额外空间 / 预处理换时间。

---

# 11. 左右双指针

两个指针：

```text
left
right
```

分别从两边开始。

典型：

```text
回文判断
反转
有序数组 Two Sum
```

---

# 12. 回文判断

例如：

```text
"abccba"
```

过程：

```text
a == a
b == b
c == c
```

左右指针不断向中间移动。

核心：

```text
left += 1
right -= 1
```

只要某次：

```text
左字符 != 右字符
```

就不是回文。

---

# 13. 回文复杂度

双指针：

```text
时间复杂度：O(n)
额外空间：O(1)
```

---

# 14. 有序数组 Two Sum

例如：

```python
nums = [1, 3, 4, 6, 8, 11]
target = 10
```

规则：

```text
当前和 == target
→ 找到

当前和 < target
→ left 右移

当前和 > target
→ right 左移
```

例如：

```text
1 + 11 = 12
→ 太大
→ right 左移

1 + 8 = 9
→ 太小
→ left 右移

3 + 8 = 11
→ 太大

3 + 6 = 9
→ 太小

4 + 6 = 10
→ 找到
```

---

# 15. 有序 Two Sum 复杂度

```text
时间：O(n)
空间：O(1)
```

前提：

> 数组有序。

---

# 16. 无序 Two Sum

例如：

```python
nums = [3, 8, 5, 12]
target = 13
```

无序数组不能直接使用左右双指针。

可以使用：

```text
dict 哈希
```

核心：

```text
need = target - num
```

每次检查：

```text
need 是否以前出现过
```

---

# 17. Two Sum 哈希模板

```python
seen = {}

for index, num in enumerate(nums):
    need = target - num

    if need in seen:
        print([seen[need], index])

    seen[num] = index
```

例如：

```text
nums = [3, 8, 5, 12]
```

当看到：

```text
num = 5
index = 2
```

得到：

```text
need = 13 - 5 = 8
```

而：

```text
seen[8] = 1
```

所以返回：

```text
[1, 2]
```

---

# 18. 为什么 Two Sum 使用 dict

因为不仅需要知道：

```text
某个数字出现过没有
```

还需要知道：

```text
这个数字出现在哪个索引
```

所以保存：

```text
数字 → 索引
```

例如：

```python
{
    3: 0,
    8: 1
}
```

---

# 19. set 和 dict 的选择

```text
只需要判断“出现过没有”
→ set

还需要保存索引 / 信息
→ dict
```

---

# 20. 快慢指针

快慢指针通常同方向移动。

可以理解：

```text
fast
→ 扫描 / 读数据

slow
→ 维护结果 / 写数据
```

---

# 21. 快慢指针典型场景

```text
数组去重
删除元素
原地修改数组
链表问题
```

例如：

```text
[1, 1, 2, 2, 3]
```

最终有效部分：

```text
[1, 2, 3]
```

---

# 22. 左右指针 vs 快慢指针

```text
左右指针

两边向中间
↓
回文
反转
有序 Two Sum
```

```text
快慢指针

同方向移动
↓
一个读
一个写
↓
去重
删除元素
链表
```

---

# 23. Day12 算法思维地图

```text
区间求和
→ 前缀和

有序 + 两数问题
→ 左右双指针

无序 + 快速查找
→ dict / set 哈希

回文
→ 左右双指针

原地删除 / 去重
→ 快慢指针

最大值 / 最小值
→ 遍历 + 状态维护
```

---

# 24. Day12 完成情况

- [x] 数组基础
- [x] 字符串基础
- [x] 遍历 + 状态维护
- [x] 前缀和
- [x] 前缀和构造
- [x] 区间求和
- [x] 左右双指针
- [x] 回文判断
- [x] 有序 Two Sum
- [x] 无序 Two Sum
- [x] dict 哈希解法
- [x] 快慢指针

# Day12 完成 ✅

---

## 知识关联

- 主题入口：[[maps/数据结构与算法|数据结构与算法]]
