---
tags:
  - 主题/算法
  - 类型/每日笔记
aliases:
  - "Day15"
---

# Day15 - 二分查找 Binary Search

## 今日学习内容

- 二分查找基本思想
- 闭区间 `[left, right]`
- `left <= right`
- 中点 `mid`
- 找到目标索引
- 未找到返回 `-1`
- 搜索插入位置
- 查找左边界
- 查找右边界
- 查找目标区间

---

# 1. 二分查找核心思想

二分查找适用于：

```text
有序数组
```

核心思想：

```text
每次比较中间元素
↓
排除一半搜索区间
```

所以时间复杂度：

```text
O(log n)
```

---

# 2. 基本例子

```python
nums = [2, 4, 6, 8, 10, 12, 14]
target = 12
```

第一次：

```text
left = 0
right = 6

mid = (0 + 6) // 2
mid = 3

nums[3] = 8
```

因为：

```text
12 > 8
```

所以去右半边：

```python
left = mid + 1
```

得到：

```text
left = 4
right = 6
```

第二次：

```text
mid = 5
nums[5] = 12
```

找到。

---

# 3. 为什么 right = len(nums) - 1

Python 索引从：

```text
0
```

开始。

例如：

```python
nums = [2, 4, 6, 8, 10, 12, 14]
```

长度：

```text
7
```

索引：

```text
0 1 2 3 4 5 6
```

所以最后一个索引：

```python
len(nums) - 1
```

---

# 4. 闭区间

本次使用：

```text
[left, right]
```

表示：

```text
left 和 right 都是有效索引
```

初始化：

```python
left = 0
right = len(nums) - 1
```

---

# 5. 为什么 while 使用 <=

使用：

```python
while left <= right:
```

因为当：

```text
left == right
```

时，区间中仍然剩下最后一个元素。

这个元素仍然需要检查。

只有：

```text
left > right
```

时，才说明搜索区间为空。

---

# 6. 中点计算

```python
mid = (left + right) // 2
```

例如：

```text
left = 0
right = 6
```

得到：

```text
mid = 3
```

---

# 7. 普通二分查找三种情况

## 情况 1：找到

```python
if nums[mid] == target:
    return mid
```

## 情况 2：目标更大

```python
elif target > nums[mid]:
    left = mid + 1
```

说明目标只能在右边。

## 情况 3：目标更小

```python
else:
    right = mid - 1
```

说明目标只能在左边。

---

# 8. 标准二分查找函数

```python
def binary_search_basic(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

测试：

```python
test_nums = [2, 4, 6, 8, 10, 12, 14]

print(binary_search_basic(test_nums, 12))
print(binary_search_basic(test_nums, 7))
```

输出：

```text
5
-1
```

---

# 9. 二分查找复杂度

时间复杂度：

```text
O(log n)
```

因为每次都缩小一半搜索范围。

空间复杂度：

```text
O(1)
```

因为只使用少量变量。

---

# 10. 搜索插入位置

例如：

```python
nums = [1, 3, 5, 6]
```

如果：

```text
target = 5
```

返回：

```text
2
```

如果：

```text
target = 2
```

应该插入：

```text
1 和 3 中间
```

返回：

```text
1
```

如果：

```text
target = 7
```

插到最后：

```text
4
```

---

# 11. 搜索插入位置关键规律

普通二分查找：

```text
没找到
→ return -1
```

搜索插入位置：

```text
没找到
→ return left
```

因为循环结束后：

```text
left
```

正好指向应该插入的位置。

---

# 12. 搜索插入位置函数

```python
def search_insert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid

        elif target < nums[mid]:
            right = mid - 1

        else:
            left = mid + 1

    return left
```

测试：

```python
print(search_insert([1, 3, 5, 6], 5))
print(search_insert([1, 3, 5, 6], 2))
print(search_insert([1, 3, 5, 6], 7))
print(search_insert([1, 3, 5, 6], 0))
```

输出：

```text
2
1
4
0
```

---

# 13. 左边界二分

例如：

```python
nums = [1, 2, 2, 2, 3, 4]
target = 2
```

目标：

```text
找到第一个 2
```

答案：

```text
索引 1
```

普通二分只要找到一个 `2` 就结束。

左边界二分：

```text
找到以后
→ 先记录当前位置
→ 继续往左找
```

---

# 14. 左边界核心

```python
if nums[first_mid] == target:
    first_answer = first_mid
    first_right = first_mid - 1
```

重点：

```text
找到不 return
继续向左
```

---

# 15. 左边界函数

```python
def find_first_position(nums, target):
    first_left = 0
    first_right = len(nums) - 1
    first_answer = -1

    while first_left <= first_right:
        first_mid = (first_left + first_right) // 2

        if target == nums[first_mid]:
            first_answer = first_mid
            first_right = first_mid - 1

        elif target > nums[first_mid]:
            first_left = first_mid + 1

        else:
            first_right = first_mid - 1

    return first_answer
```

---

# 16. 右边界二分

仍然：

```python
nums = [1, 2, 2, 2, 3, 4]
target = 2
```

目标：

```text
找到最后一个 2
```

答案：

```text
索引 3
```

---

# 17. 右边界核心

```python
if nums[last_mid] == target:
    last_answer = last_mid
    last_left = last_mid + 1
```

重点：

```text
找到不 return
继续向右
```

---

# 18. 右边界函数

```python
def find_last_position(nums, target):
    last_left = 0
    last_right = len(nums) - 1
    last_answer = -1

    while last_left <= last_right:
        last_mid = (last_left + last_right) // 2

        if target == nums[last_mid]:
            last_answer = last_mid
            last_left = last_mid + 1

        elif target < nums[last_mid]:
            last_right = last_mid - 1

        else:
            last_left = last_mid + 1

    return last_answer
```

---

# 19. 左边界 vs 右边界

```text
找第一次出现：

找到
→ 记录 mid
→ right = mid - 1
→ 继续往左
```

```text
找最后一次出现：

找到
→ 记录 mid
→ left = mid + 1
→ 继续往右
```

这是两者最关键的区别。

---

# 20. 查找目标区间

例如：

```python
nums = [1, 2, 2, 2, 3, 4]
target = 2
```

目标：

```python
[1, 3]
```

可以直接组合：

```python
def search_range(nums, target):
    first = find_first_position(nums, target)
    last = find_last_position(nums, target)

    return [first, last]
```

---

# 21. 二分查找思维地图

```text
有序数组 + 查找
→ 考虑二分
```

```text
找到任意一个 target
→ 普通二分
```

```text
找插入位置
→ 没找到时 return left
```

```text
找第一次出现
→ 找到后继续往左
```

```text
找最后一次出现
→ 找到后继续往右
```

```text
找 target 区间
→ 左边界 + 右边界
```

---

# 22. 今日容易出错的地方

## 1. right 初始化

正确：

```python
right = len(nums) - 1
```

因为索引从 `0` 开始。

---

## 2. 闭区间循环条件

正确：

```python
while left <= right:
```

不是：

```python
while left < right:
```

否则可能漏掉最后一个元素。

---

## 3. 向右搜索

```python
left = mid + 1
```

---

## 4. 向左搜索

```python
right = mid - 1
```

---

## 5. 左边界

找到以后：

```python
answer = mid
right = mid - 1
```

---

## 6. 右边界

找到以后：

```python
answer = mid
left = mid + 1
```

---

# 23. Day15 完成情况

- [x] 二分查找思想
- [x] 有序数组前提
- [x] 闭区间
- [x] `left <= right`
- [x] 中点计算
- [x] 普通二分
- [x] 返回索引
- [x] 未找到返回 `-1`
- [x] 搜索插入位置
- [x] 左边界
- [x] 右边界
- [x] 查找目标区间
- [x] 时间复杂度 `O(log n)`
- [x] 空间复杂度 `O(1)`

# Day15 完成 ✅

---

## 知识关联

- 主题入口：[[maps/数据结构与算法|数据结构与算法]]
