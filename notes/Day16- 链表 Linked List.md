---
tags:
  - 主题/算法
  - 类型/每日笔记
aliases:
  - "Day16"
---

# Day16 - 链表 Linked List

## 今日学习内容

- 单链表基本结构
- ListNode 节点
- `next` 指针
- 链表遍历
- 头部插入
- 尾部插入
- 删除节点
- 删除头节点
- 反转链表
- 快慢指针找中点
- 快慢指针判断链表是否有环

---

# 1. 链表是什么

普通数组：

```text
10 | 20 | 30
```

链表：

```text
10 → 20 → 30 → None
```

每个节点通常包含：

```text
数据 val
+
下一个节点 next
```

可以理解为：

```text
[val | next]
```

---

# 2. ListNode

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
```

其中：

```text
self.val
→ 当前节点的数据

self.next
→ 下一个节点
```

---

# 3. 创建并连接链表

```python
node_a = ListNode(10)
node_b = ListNode(20)
node_c = ListNode(30)

node_a.next = node_b
node_b.next = node_c
```

得到：

```text
10 → 20 → 30 → None
```

---

# 4. 链表遍历

```python
current_node = node_a

while current_node:
    print(current_node.val)
    current_node = current_node.next
```

核心：

```text
当前节点
↓
处理当前节点
↓
current = current.next
↓
移动到下一个节点
```

---

# 5. 数组移动 vs 链表移动

数组：

```python
index += 1
```

链表：

```python
current = current.next
```

链表很多题的核心就是：

```text
让指针沿着 next 移动
```

---

# 6. 头部插入

原链表：

```text
10 → 20 → 30
```

插入 `5`：

```text
5 → 10 → 20 → 30
```

代码：

```python
new_node = ListNode(5)

new_node.next = head_node
head_node = new_node
```

记忆：

```text
1. 新节点指向旧头节点
2. head 指向新节点
```

---

# 7. 尾部插入

原链表：

```text
5 → 10 → 20 → 30 → None
```

找到尾节点：

```python
tail_node = head_node

while tail_node.next:
    tail_node = tail_node.next
```

尾节点满足：

```python
tail_node.next is None
```

然后：

```python
new_tail = ListNode(40)
tail_node.next = new_tail
```

得到：

```text
5 → 10 → 20 → 30 → 40 → None
```

---

# 8. 为什么不能移动 head_node

错误思路：

```python
while head_node.next:
    head_node = head_node.next
```

这样会把真正的头节点丢掉。

正确：

```python
tail_node = head_node
```

让临时指针移动：

```python
tail_node = tail_node.next
```

而：

```text
head_node
```

始终保留链表入口。

---

# 9. 删除中间节点

例如：

```text
5 → 10 → 20 → 30
```

删除：

```text
20
```

目标：

```text
5 → 10 → 30
```

关键：

```text
让 10 直接指向 30
```

代码：

```python
delete_current.next = delete_current.next.next
```

本质：

```text
跳过目标节点
```

---

# 10. 为什么检查 current.next

如果：

```text
current → 10
current.next → 20
```

发现：

```python
current.next.val == target
```

就可以直接修改：

```python
current.next = current.next.next
```

这样不用额外保存前驱节点。

---

# 11. 删除头节点

删除：

```text
5 → 10 → 30 → 40
```

中的 `5`。

因为头节点前面没有节点，所以需要单独处理：

```python
if head.val == target:
    return head.next
```

结果：

```text
10 → 30 → 40
```

---

# 12. 删除节点函数

```python
def delete_value(head, target):
    if head is None:
        return None

    if head.val == target:
        return head.next

    current_delete = head

    while current_delete.next:
        if current_delete.next.val == target:
            current_delete.next = current_delete.next.next
            break

        current_delete = current_delete.next

    return head
```

调用：

```python
head_node = delete_value(head_node, target)
```

为什么必须重新赋值？

因为：

```text
删除头节点以后
head 可能发生变化
```

---

# 13. 反转链表

原链表：

```text
10 → 20 → 30 → 40 → None
```

目标：

```text
40 → 30 → 20 → 10 → None
```

需要三个指针：

```text
prev
current
next_node
```

含义：

```text
prev
→ 前一个节点

current
→ 当前处理节点

next_node
→ 提前保存后面的节点
```

---

# 14. 为什么先保存 next_node

如果直接：

```python
current.next = prev
```

原来的：

```text
current → 后面的链表
```

会被修改。

所以必须先：

```python
next_node = current.next
```

把后面的链表保存下来。

---

# 15. 反转链表四步

```text
1. 保存后面
2. 反转箭头
3. prev 前进
4. current 前进
```

对应：

```python
next_node = current.next
current.next = prev
prev = current
current = next_node
```

---

# 16. 反转链表函数

```python
def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev
```

循环结束：

```text
current = None
prev = 新头节点
```

所以：

```python
return prev
```

---

# 17. 反转链表易错点

`return prev` 必须放在：

```text
while 循环外面
```

错误：

```python
while current:
    ...
    return prev
```

这样只会执行一轮。

正确：

```python
while current:
    ...

return prev
```

---

# 18. 快慢指针

两个指针：

```text
slow
→ 每次走 1 步

fast
→ 每次走 2 步
```

代码：

```python
slow = slow.next
fast = fast.next.next
```

---

# 19. 快慢指针找中点

例如：

```text
10 → 20 → 30 → 40 → 50
```

初始：

```text
slow = 10
fast = 10
```

移动：

```text
slow = 20
fast = 30
```

再次：

```text
slow = 30
fast = 50
```

最终：

```text
slow = 中点
```

---

# 20. 找中点函数

```python
def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

偶数长度：

```text
10 → 20 → 30 → 40
```

这种写法返回：

```text
30
```

即偏右中点。

---

# 21. 判断链表是否有环

正常链表：

```text
10 → 20 → 30 → 40 → None
```

有环链表：

```text
10 → 20 → 30 → 40
     ↑         ↓
     ← ← ← ← ←
```

如果有环：

```text
fast 最终会追上 slow
```

如果无环：

```text
fast 最终会走到 None
```

---

# 22. 判断有环函数

```python
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
```

---

# 23. 为什么比较 slow == fast

必须比较：

```python
slow == fast
```

也就是：

```text
是否指向同一个节点
```

不能比较：

```python
slow.val == fast.val
```

因为不同节点可能拥有相同的值。

---

# 24. 构造有环链表

```python
cycle_a = ListNode(10)
cycle_b = ListNode(20)
cycle_c = ListNode(30)
cycle_d = ListNode(40)

cycle_a.next = cycle_b
cycle_b.next = cycle_c
cycle_c.next = cycle_d

cycle_d.next = cycle_b
```

得到：

```text
10 → 20 → 30 → 40
     ↑         ↓
     ← ← ← ← ←
```

注意：

> 有环链表不能再直接使用普通 `while current:` 遍历，否则会无限循环。

---

# 25. Day16 文件结构

```text
day16_linked_list/
├── list_node.py
├── operations.py
└── main.py
```

## list_node.py

负责：

```text
ListNode 类
```

## operations.py

负责：

```text
delete_value()
reverse_list()
find_middle()
has_cycle()
```

## main.py

负责：

```text
创建测试链表
调用函数
输出测试结果
```

---

# 26. Day16 核心思维

链表题最重要的不是背代码，而是理解：

```text
节点
↓
next
↓
指针移动
↓
修改 next
```

常见指针：

```text
current
prev
slow
fast
```

它们本质上都是：

> 指向某个节点的变量。

---

# 27. 今日易错点

## 1. 节点和节点值不要混

```python
prev = current
```

不是：

```python
prev = current.val
```

---

## 2. 链表移动

正确：

```python
current = current.next
```

不是：

```python
current += 1
```

---

## 3. 不要随便移动 head

尽量：

```python
current = head
```

使用临时指针移动。

---

## 4. 修改链表后重新测试

删除、反转等操作会直接修改原链表。

测试不同算法时，可以重新创建一条干净链表。

---

## 5. 环判断比较节点本身

```python
slow == fast
```

不是：

```python
slow.val == fast.val
```

---

# 28. Day16 完成情况

- [x] ListNode
- [x] next
- [x] 节点连接
- [x] 链表遍历
- [x] 头部插入
- [x] 尾部插入
- [x] 删除中间节点
- [x] 删除头节点
- [x] delete_value
- [x] 反转链表
- [x] 快慢指针
- [x] 查找中点
- [x] 判断链表有环
- [x] 文件拆分

# Day16 完成 ✅

---

## 知识关联

- 主题入口：[[maps/数据结构与算法|数据结构与算法]]
- 相关知识：[[notes/Day07-Python 面向对象 OOP|Day07]]
