# Day19 - DFS 与 BFS 巩固

## 今日目标

继续学习二叉树，重点掌握：

- BFS 层序遍历
- DFS 递归比较二叉树
- 理解递归返回值的使用

完成 LeetCode：

- [x] 102. 二叉树的层序遍历
- [x] 100. 相同的树


---

# 一、BFS（广度优先搜索）

## 1. BFS 思想

BFS（Breadth First Search）

中文：广度优先搜索。

特点：

> 一层一层访问节点。

例如：

```
        10
       /  \
      20   30
     / \   /
    40 50 60
```

访问顺序：

```
10
20 30
40 50 60
```

---

## 2. deque 双端队列

Python 中 BFS 常用：

```python
from collections import deque
```

deque：

double-ended queue（双端队列）

特点：

可以从两端快速添加和删除元素。

常用操作：

### 创建队列

```python
queue = deque([root])
```

### 入队

```python
queue.append(node)
```

### 出队

```python
queue.popleft()
```

为什么不用 list？

如果使用：

```python
list.pop(0)
```

删除第一个元素需要移动其他元素：

时间复杂度：

```
O(n)
```

而：

```python
deque.popleft()
```

时间复杂度：

```
O(1)
```

---

# 二、LeetCode 102. 二叉树的层序遍历

## 题目要求

普通 BFS：

```
10 20 30 40 50 60
```

但是题目要求：

```python
[
    [10],
    [20,30],
    [40,50,60]
]
```

所以需要记录每一层节点。

---

## 核心技巧

记录当前层节点数量：

```python
level_size = len(queue)
```

然后：

```python
for _ in range(level_size):
```

只处理当前层。

---

## BFS 模板

```python
while queue:

    level_size = len(queue)

    current_level = []

    for _ in range(level_size):

        node = queue.popleft()

        current_level.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    result.append(current_level)
```

---

## 易错点

### 错误

```python
if current_node.left is None:
```

含义：

左孩子不存在。

但是 BFS 需要判断：

左孩子存在时加入队列。


正确：

```python
if current_node.left is not None:
    queue.append(current_node.left)
```

---

# 三、LeetCode 100. 相同的树

## 题目

判断两个二叉树是否完全相同。


两个树相同需要满足：

1. 当前节点值相同
2. 左子树相同
3. 右子树相同


---

# DFS 递归思想

递归判断：

```
当前节点
    ↓
左子树
    ↓
右子树
```

---

## 三种情况


## 1. 两个节点都是空

例如：

```
p = None
q = None
```

返回：

```python
True
```

因为两个空节点相同。


---

## 2. 一个节点为空

例如：

```
p:

    1


q:

    1
   /
  2
```

结构不同。

返回：

```python
False
```


---

## 3. 两个节点都存在


比较：

```python
p.val == q.val
```

递归：

```python
left_same = self.isSameTree(
    p.left,
    q.left
)

right_same = self.isSameTree(
    p.right,
    q.right
)
```

最后：

```python
return (
    p.val == q.val
    and left_same
    and right_same
)
```

---

# 四、递归返回值的重要性

错误：

```python
self.isSameTree(p.left,q.left)
```

虽然执行了递归，但是返回结果没有保存。


例如：

```
False
 ↓
没有变量接收
 ↓
结果丢失
```


正确：

```python
left_same = self.isSameTree(
    p.left,
    q.left
)
```

或者：

直接使用：

```python
return self.isSameTree(...)
```


---

# 五、DFS 与 BFS 对比

| | DFS | BFS |
|-|-|-|
| 中文 | 深度优先搜索 | 广度优先搜索 |
| 实现 | 递归 / 栈 | 队列 |
| 特点 | 一条路走到底 | 一层层访问 |
| 二叉树应用 | 前中后序遍历 | 层序遍历 |
| 常见问题 | 路径、递归 | 最短距离、层数 |

---

# 六、复杂度分析


## LeetCode 102

### 时间复杂度

每个节点访问一次：

```
O(n)
```


### 空间复杂度

队列保存一层节点：

```
O(w)
```

w 为二叉树最大宽度。

最坏：

```
O(n)
```


---

## LeetCode 100

### 时间复杂度

每个节点比较一次：

```
O(n)
```


### 空间复杂度

递归调用栈：

```
O(h)
```

h 为树高度。

最坏：

```
O(n)
```

---

# 七、今日核心收获

## 1. BFS 分层关键

```python
level_size = len(queue)
```

利用队列长度区分每一层。


## 2. DFS 需要利用返回值

递归不是简单调用：

```python
dfs(child)
```

而是：

```python
result = dfs(child)
```

利用子问题结果。


## 3. 二叉树递归模板

```python
if node is None:
    return ...

left = dfs(node.left)

right = dfs(node.right)

return result
```

---

# 八、完成情况

- [x] 理解 deque
- [x] BFS 层序遍历
- [x] LeetCode 102 提交通过
- [x] DFS 判断两棵树
- [x] LeetCode 100 提交通过
- [x] 理解递归返回值


---

# Day19 总结

今天学习了二叉树中最重要的两种搜索方式：

## BFS

关注：

> 层

核心：

```
队列 + len(queue)
```


## DFS

关注：

> 子问题

核心：

```
递归 + 返回值
```


这两个思想会继续应用于：

- 图搜索
- 回溯
- 动态规划
- AI 算法中的搜索问题


Day19 完成 ✅