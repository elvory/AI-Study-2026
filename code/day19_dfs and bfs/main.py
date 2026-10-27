from collections import deque

#leetcode 102 题解 二叉树层序遍历
def level_order(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for i in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.val)

            if current_node.left is not None:
                queue.append(current_node.left)

            if current_node.right is not None:
                queue.append(current_node.right)

        result.append(current_level)

    return result

#TreeNode，有了这个类，才能创建真正的二叉树节点。
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(10)

root.left = TreeNode(20)
root.right = TreeNode(30)

root.left.left = TreeNode(40)
root.left.right = TreeNode(50)
root.right.left = TreeNode(60)

print(level_order(root))







#leetcode 100 DFS 递归
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        elif (p is None and q is not None) or (p is not None and q is None):
            return False

        else:
            return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
