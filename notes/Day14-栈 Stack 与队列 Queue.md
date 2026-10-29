---
tags:
  - 主题/算法
  - 类型/每日笔记
aliases:
  - "Day14"
---

# Day14 - 栈 Stack 与队列 Queue

## 今日学习内容

- 栈 Stack
- 后进先出 LIFO
- 栈的入栈、出栈、查看栈顶
- 栈解决括号匹配
- 队列 Queue
- 先进先出 FIFO
- `deque`
- 队列入队、出队、查看队头
- 栈与队列对比

---

# 1. 栈 Stack

栈的核心特点：

```text
后进先出
Last In, First Out
LIFO
```

例如：

```text
依次进入：

10
20
30
```

栈：

```text
顶部
30
20
10
底部
```

出栈顺序：

```text
30 → 20 → 10
```

---

# 2. Python 使用 list 实现栈

创建：

```python
stack = []
```

入栈：

```python
stack.append(10)
stack.append(20)
stack.append(30)
```

得到：

```python
[10, 20, 30]
```

其中：

```text
最右边 = 栈顶
```

所以当前栈顶：

```text
30
```

---

# 3. 出栈 pop()

```python
value = stack.pop()
```

会：

```text
返回栈顶元素
+
删除栈顶元素
```

例如：

```python
stack = [10, 20, 30]

value = stack.pop()
```

得到：

```text
value = 30
stack = [10, 20]
```

---

# 4. 查看栈顶

如果只想看栈顶，不删除：

```python
stack[-1]
```

例如：

```python
stack = [10, 20]

print(stack[-1])
```

输出：

```text
20
```

但是：

```python
stack
```

仍然是：

```python
[10, 20]
```

---

# 5. 栈基本操作总结

```text
入栈
→ append()

出栈
→ pop()

查看栈顶
→ stack[-1]

判断是否为空
→ if stack:
```

---

# 6. 栈为什么适合括号匹配

例如：

```text
{[()]}
```

括号具有：

```text
最后打开
最先关闭
```

例如：

```text
{
    [
        (
        )
    ]
}
```

最后进入的是：

```text
(
```

最先关闭的是：

```text
)
```

符合：

```text
后进先出
```

所以可以使用栈。

---

# 7. 括号匹配对应关系

使用字典：

```python
bracket_pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}
```

含义：

```text
) → (
] → [
} → {
```

---

# 8. 左括号入栈

例如：

```python
s = "{[()]}"

bracket_stack = []
```

遍历：

```python
for char in s:
    if char in ['(', '[', '{']:
        bracket_stack.append(char)
```

遇到：

```text
{
[
(
```

栈逐渐变成：

```text
['{']
['{', '[']
['{', '[', '(']
```

最右边：

```text
(
```

是当前栈顶。

---

# 9. 遇到右括号

遇到：

```text
)
```

通过：

```python
bracket_pairs[char]
```

得到：

```text
(
```

然后和：

```python
bracket_stack[-1]
```

比较。

如果一样：

```python
bracket_stack.pop()
```

表示当前括号匹配完成。

---

# 10. 为什么匹配后必须 pop()

例如：

```text
{[()]}
```

遇到 `)`：

```text
栈：
['{', '[', '(']
```

匹配：

```text
( 和 )
```

然后：

```python
bracket_stack.pop()
```

栈变成：

```text
['{', '[']
```

接下来：

```text
]
```

才能和当前栈顶：

```text
[
```

进行匹配。

---

# 11. 遇到不匹配

例如：

```text
{[(])}
```

当遇到：

```text
]
```

当前栈顶：

```text
(
```

但：

```text
]
```

应该匹配：

```text
[
```

所以：

```text
不合法
```

可以：

```python
brackets_valid = False
break
```

直接停止。

---

# 12. 空栈边界情况

例如：

```text
]
```

一开始就是右括号。

此时：

```python
bracket_stack[-1]
```

会报错，因为栈为空。

所以必须先：

```python
if not bracket_stack:
    brackets_valid = False
    break
```

意思：

```text
出现右括号
但前面没有任何左括号
→ 不合法
```

---

# 13. 最终为什么还要判断栈是否为空

例如：

```text
(((
```

整个过程中没有出现错误的右括号。

所以：

```python
brackets_valid
```

仍然可能是：

```python
True
```

但是最后：

```python
bracket_stack
```

是：

```python
['(', '(', '(']
```

说明还有左括号没有匹配。

所以最终合法条件必须同时满足：

```python
if brackets_valid and not bracket_stack:
    print("括号合法")
else:
    print("括号不合法")
```

---

# 14. 有效括号完整思路

```text
遍历字符
↓
如果是左括号
→ 入栈

如果是右括号
↓
先检查栈是否为空
↓
检查右括号和栈顶是否匹配
↓
匹配
→ pop()

不匹配
→ False + break

遍历结束
↓
中途没有错误
+
最终栈为空
↓
括号合法
```

---

# 15. 队列 Queue

队列的核心特点：

```text
先进先出
First In, First Out
FIFO
```

例如：

```text
A 先进入
B 第二
C 第三
```

出队顺序：

```text
A → B → C
```

类似：

```text
排队买饭
```

先来的人先处理。

---

# 16. Python 使用 deque 实现队列

导入：

```python
from collections import deque
```

创建：

```python
queue_data = deque()
```

入队：

```python
queue_data.append(10)
queue_data.append(20)
queue_data.append(30)
```

得到：

```python
deque([10, 20, 30])
```

其中：

```text
左边 = 队头
右边 = 队尾
```

---

# 17. 队列出队

队列应该从队头出队。

使用：

```python
queue_data.popleft()
```

例如：

```python
queue_data = deque([10, 20, 30])

value = queue_data.popleft()
```

得到：

```text
value = 10
```

剩下：

```python
deque([20, 30])
```

---

# 18. 查看队头

如果只想查看：

```python
queue_data[0]
```

例如：

```python
queue_data = deque([20, 30])

print(queue_data[0])
```

得到：

```text
20
```

队列仍然：

```python
deque([20, 30])
```

---

# 19. 为什么不用 list.pop(0)

普通列表：

```python
list.pop(0)
```

需要移动后面的元素。

时间复杂度：

```text
O(n)
```

而：

```python
deque.popleft()
```

时间复杂度：

```text
O(1)
```

所以算法中做队列时：

```text
优先 deque
```

---

# 20. while queue

可以：

```python
while task_queue:
```

表示：

```text
只要队列不为空
就继续处理
```

例如：

```python
task_queue = deque(["任务A", "任务B", "任务C"])

while task_queue:
    print(f"处理：{task_queue.popleft()}")
```

输出：

```text
处理：任务A
处理：任务B
处理：任务C
```

---

# 21. 栈 vs 队列

同时放入：

```text
A
B
C
```

## 栈

```python
compare_stack.pop()
```

得到：

```text
C
```

因为：

```text
后进先出
```

## 队列

```python
compare_queue.popleft()
```

得到：

```text
A
```

因为：

```text
先进先出
```

---

# 22. 栈和队列核心对比

```text
栈 Stack

入：
append()

出：
pop()

特点：
后进先出 LIFO

典型应用：
括号匹配
DFS
撤销操作
表达式处理
```

```text
队列 Queue

入：
append()

出：
popleft()

特点：
先进先出 FIFO

典型应用：
任务队列
BFS
层序遍历
消息处理
```

---

# 23. 今日重点记忆

```text
stack.append(x)
→ 入栈

stack.pop()
→ 出栈

stack[-1]
→ 查看栈顶
```

```text
queue.append(x)
→ 入队

queue.popleft()
→ 出队

queue[0]
→ 查看队头
```

最核心区别：

```text
栈
→ 后进先出

队列
→ 先进先出
```

---

# 24. Day14 完成情况

- [x] 栈 Stack
- [x] LIFO
- [x] append()
- [x] pop()
- [x] stack[-1]
- [x] 有效括号
- [x] 括号映射字典
- [x] 空栈边界处理
- [x] 最终合法性判断
- [x] 队列 Queue
- [x] FIFO
- [x] deque
- [x] popleft()
- [x] queue[0]
- [x] while queue
- [x] 栈 vs 队列对比

# Day14 完成 ✅

---

## 知识关联

- 主题入口：[[maps/数据结构与算法|数据结构与算法]]
