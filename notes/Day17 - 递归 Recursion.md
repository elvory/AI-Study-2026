---
tags:
  - 主题/算法
  - 类型/每日笔记
aliases:
  - "Day17"
---

# Day17 - 递归 Recursion

## 今日学习内容

- 什么是递归
- 终止条件
- 递归调用
- 递归“进入”和“返回”
- 递归求和
- 阶乘
- 调用栈 Call Stack
- 递归遍历链表
- 递归 vs 循环
- 递归常见错误

---

# 1. 什么是递归

递归：

> 一个函数在执行过程中调用自己。

例如：

```python
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)
```

调用：

```python
countdown(4)
```

输出：

```text
4
3
2
1
```

---

# 2. 递归两个核心组成

递归必须包含：

```text
1. 终止条件
2. 递归调用
```

例如：

```python
def countdown(n):
    if n == 0:
        return

    countdown(n - 1)
```

其中：

```python
if n == 0:
```

是终止条件。

```python
countdown(n - 1)
```

是递归调用。

---

# 3. 为什么必须有终止条件

如果没有终止条件：

```python
def test(n):
    test(n - 1)
```

就会：

```text
test(5)
→ test(4)
→ test(3)
→ ...
```

一直调用下去。

最终通常报：

```text
RecursionError
```

---

# 4. 参数必须靠近终止条件

例如：

```python
def bad_recursion(n):
    if n == 0:
        return

    bad_recursion(n + 1)
```

如果：

```text
n = 3
```

会：

```text
3 → 4 → 5 → 6 → ...
```

离终止条件 `0` 越来越远。

所以递归时要检查：

> 参数有没有越来越接近终止条件？

---

# 5. 递归进入过程

例如：

```python
def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)
```

执行：

```python
countdown(3)
```

过程：

```text
countdown(3)
↓
countdown(2)
↓
countdown(1)
↓
countdown(0)
```

这是：

```text
递归进入
```

---

# 6. 递归返回过程

如果：

```python
def countdown_reverse(n):
    if n == 0:
        return

    countdown_reverse(n - 1)
    print(n)
```

执行：

```python
countdown_reverse(3)
```

会先：

```text
3 → 2 → 1 → 0
```

然后返回：

```text
1 → 2 → 3
```

输出：

```text
1
2
3
```

---

# 7. print 放前面和后面的区别

## 放在递归调用前

```python
print(n)
func(n - 1)
```

执行顺序：

```text
3
2
1
```

## 放在递归调用后

```python
func(n - 1)
print(n)
```

执行顺序：

```text
1
2
3
```

重点：

```text
递归调用前
→ 顺着进入执行

递归调用后
→ 顺着返回执行
```

---

# 8. 递归求和

目标：

```text
1 + 2 + 3 + ... + n
```

例如：

```text
recursive_sum(4)
= 4 + 3 + 2 + 1
= 10
```

递归关系：

```text
recursive_sum(4)
= 4 + recursive_sum(3)

recursive_sum(3)
= 3 + recursive_sum(2)

recursive_sum(2)
= 2 + recursive_sum(1)

recursive_sum(1)
= 1
```

---

# 9. 递归求和代码

```python
def recursive_sum(n):
    if n == 1:
        return 1

    return n + recursive_sum(n - 1)
```

测试：

```python
print(recursive_sum(5))
```

输出：

```text
15
```

---

# 10. 阶乘 factorial

例如：

```text
4!
= 4 × 3 × 2 × 1
= 24
```

递归关系：

```text
factorial(4)
= 4 × factorial(3)

factorial(3)
= 3 × factorial(2)

factorial(2)
= 2 × factorial(1)

factorial(1)
= 1
```

---

# 11. 阶乘代码

```python
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)
```

例如：

```python
print(factorial(5))
```

输出：

```text
120
```

---

# 12. 调用栈 Call Stack

执行：

```python
factorial(4)
```

不会直接得到结果。

先进入：

```text
factorial(4)
factorial(3)
factorial(2)
factorial(1)
```

这相当于不断压入调用栈。

然后开始返回：

```text
factorial(1) = 1
factorial(2) = 2
factorial(3) = 6
factorial(4) = 24
```

---

# 13. 调用栈理解

可以理解成：

```text
进入：

4
↓
3
↓
2
↓
1
```

然后：

```text
返回：

1
↑
2
↑
3
↑
4
```

这也是为什么递归会消耗额外空间。

---

# 14. 递归遍历链表

假设：

```text
10 → 20 → 30 → None
```

递归遍历：

```python
def recursive_traverse(node):
    if node is None:
        return

    print(node.val)
    recursive_traverse(node.next)
```

输出：

```text
10
20
30
```

---

# 15. 递归逆序输出链表

如果把 `print()` 放在递归后面：

```python
def recursive_traverse_reverse(node):
    if node is None:
        return

    recursive_traverse_reverse(node.next)
    print(node.val)
```

对于：

```text
10 → 20 → 30
```

输出：

```text
30
20
10
```

---

# 16. 链表 + 递归思维

递归遍历链表可以理解成：

```text
处理当前节点
+
处理剩下的链表
```

即：

```python
recursive_traverse(node.next)
```

就是把剩余链表交给同一个函数继续处理。

---

# 17. 递归 vs 循环

## 循环

```python
total = 0

for i in range(1, n + 1):
    total += i
```

特点：

```text
通常空间更省
适合简单重复操作
```

---

## 递归

```python
def recursive_sum(n):
    if n == 1:
        return 1

    return n + recursive_sum(n - 1)
```

特点：

```text
代码有时更符合问题结构

常见于：
树
DFS
分治
回溯
```

---

# 18. 递归的空间开销

递归每调用一层，都需要保存当前函数状态。

例如：

```text
recursive_sum(4)
recursive_sum(3)
recursive_sum(2)
recursive_sum(1)
```

都会暂时保存在调用栈中。

因此递归通常会有额外的：

```text
O(n)
```

调用栈空间。

---

# 19. 常见递归错误

## 错误 1：没有终止条件

```python
def func(n):
    func(n - 1)
```

会无限递归。

---

## 错误 2：参数远离终止条件

```python
def func(n):
    if n == 0:
        return

    func(n + 1)
```

如果从正数开始：

```text
3 → 4 → 5 → ...
```

永远到不了 `0`。

---

## 错误 3：终止条件可能被跳过

例如：

```python
def test_recursion(n):
    if n == 1:
        return 1

    return n + test_recursion(n - 2)
```

如果：

```text
n = 4
```

过程：

```text
4 → 2 → 0 → -2 → ...
```

永远不会等于 `1`。

所以终止条件设计必须和递归步长匹配。

---

# 20. 更稳妥的终止条件

有些情况下：

```python
if n <= 1:
```

比：

```python
if n == 1:
```

更安全。

具体要根据问题定义判断。

---

# 21. Day17 核心思维

递归可以总结成：

```text
大问题
↓
拆成更小的同类问题
↓
直到最简单情况
↓
再逐层返回结果
```

每次写递归都检查：

```text
1. 最小问题是什么？
2. 终止条件是什么？
3. 怎么把问题缩小？
4. 参数是否一定会到终止条件？
5. 返回阶段要做什么？
```

---

# 22. Day17 完成情况

- [x] 递归基本概念
- [x] 终止条件
- [x] 递归调用
- [x] 进入过程
- [x] 返回过程
- [x] 递归求和
- [x] 阶乘
- [x] 调用栈
- [x] 递归遍历链表
- [x] 逆序递归输出
- [x] 递归 vs 循环
- [x] RecursionError
- [x] 递归常见错误

# Day17 完成 ✅

---

## 知识关联

- 主题入口：[[maps/数据结构与算法|数据结构与算法]]
