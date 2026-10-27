class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
#根节点
root = TreeNode(10)

#添加左孩子和右孩子
root.left = TreeNode(20)
root.right = TreeNode(30)

#+1
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.right.left = TreeNode(60)

#二叉树遍历

#第一种 前序遍历 Preorder Traversal
#根->左->右
#递归
def preorder(node):
    if node is None:
        return

    print(node.val)
    preorder(node.left)
    preorder(node.right)

preorder(root)
print()

#第二种 中序遍历 Inorder Traversal
#左->根->右
def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.val)
    inorder(node.right)

inorder(root)
print()


#第三种 后序遍历 Postorder Traversal Traversal
#左->右->根
def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.val)


#层序遍历 Level Order Traversal
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

level_order(root)
print()


#二叉树 深度
def max_depth(node):
    if node is None:
        return 0

    left_depth = max_depth(node.left)
    right_depth = max_depth(node.right)

    #返回最大深度
    return 1 + max(left_depth,right_depth)

#测试
print("原始深度：", max_depth(root))

root.left.left.left = TreeNode(70)

print("新增节点后：", max_depth(root))
