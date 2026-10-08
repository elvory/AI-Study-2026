# Day18 - 二叉树 Binary Tree

## 一、二叉树基础

二叉树是一种树形数据结构，每个节点最多有两个孩子：

- `left`：左孩子
    
- `right`：右孩子
    

Python 节点定义：

```
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

构造示例：

```
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)

root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.right.left = TreeNode(60)
```

得到：

```
        10
       /  \
      20   30
     / \   /
    40 50 60
```

**注意：** `left` 和 `right` 保存的是节点对象，不是单纯的整数。

## 二、二叉树的四种遍历

### 1. 前序遍历 Preorder

规则：根 → 左 → 右

```
def preorder(node):
    if node is None:
        return

    print(node.val)
    preorder(node.left)
    preorder(node.right)
```

输出：`10, 20, 40, 50, 30, 60`

### 2. 中序遍历 Inorder

规则：左 → 根 → 右

```
def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.val)
    inorder(node.right)
```

输出：`40, 20, 50, 10, 60, 30`

### 3. 后序遍历 Postorder

规则：左 → 右 → 根

```
def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.val)
```

输出：`40, 50, 20, 60, 30, 10`

**核心规律：** 三种 DFS 递归遍历的区别，在于处理当前节点的代码放在哪里。

### 4. 层序遍历 Level Order（BFS）

规则：从上到下，每层从左到右。

使用 `deque` 队列：

```
from collections import deque

def level_order(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        current = queue.popleft()
        print(current.val)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)
```

输出：`10, 20, 30, 40, 50, 60`

BFS 的核心过程：

- 左边出队：`popleft()`
    
- 处理当前节点
    
- 左孩子入队：`append()`
    
- 右孩子入队：`append()`
    

注意不能使用 `if ... elif ...` 判断左右孩子，因为两个孩子可能同时存在。

## 三、LeetCode 104 - 二叉树的最大深度 ✅

题目：返回从根节点到最远叶子节点的最大层数。

递归公式：

[  
depth(node)=1+\max(depth(left),depth(right))  
]

提交代码：

```
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
```

**关键理解：**

- 空节点的深度为 `0`
    
- 叶子节点的深度为 `1`
    
- `max()` 选择左右子树中更深的一边
    
- `+1` 代表当前节点自身这一层
    

复杂度：

- 时间：`O(n)`，每个节点访问一次
    
- 空间：`O(h)`，递归调用栈与树高有关
    
- 最坏空间：`O(n)`
    

## 四、LeetCode 226 - 翻转二叉树 ✅

题目：交换整棵二叉树中每个节点的左右孩子。

提交代码：

```
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```

**关键理解：**

当前节点只负责交换自己的左右孩子，剩余节点交给递归处理。

`return root` 是因为翻转后根节点对象本身没有改变。

复杂度：

- 时间：`O(n)`
    
- 空间：`O(h)`
    
- 平衡二叉树：空间 `O(log n)`
    
- 极度倾斜的二叉树：空间 `O(n)`
    

## 五、DFS 与 BFS 对比

|特征|DFS|BFS|
|---|---|---|
|核心思想|沿分支深入|按层访问|
|常用实现|递归、栈|队列|
|典型应用|前中后序遍历|层序遍历|
|时间复杂度|O(n)|O(n)|
|辅助空间|O(h)|O(w)|

其中 `h` 是树高，`w` 是树的最大宽度；两者最坏都可能达到 `O(n)`。

## 六、今日重要知识点

1. 遇到树结构，优先思考递归是否适用。
    
2. 递归必须有终止条件。
    
3. 深度计算通常需要先得到左右子树的结果，再合并。
    
4. 前序、中序、后序遍历都属于 DFS。
    
5. 层序遍历通常使用 BFS + 队列。
    
6. 递归空间复杂度取决于调用栈的最大深度，而不是总调用次数。
    
7. LeetCode 类方法中递归调用使用 `self.方法名()`。
    

## 七、完成情况

- 二叉树节点定义
    
- 手动构造二叉树
    
- 前序遍历
    
- 中序遍历
    
- 后序遍历
    
- 层序遍历 BFS
    
- LeetCode 104 提交通过
    
- LeetCode 226 提交通过
    
- 时间复杂度分析
    
- 空间复杂度分析
    

**Day18 核心学习完成 ✅**