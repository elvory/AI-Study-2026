
#leetcode 101 对称二叉树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def check(left,right):
            if left==None and right==None:
                return True

            if left==None or right==None:
                return False

            if left.val!=right.val:
                return False

            return check(left.left,right.right) and check(left.right,right.left)

        return check(root,root)



#leetcode 572 另一棵树的子树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(a,b):
            if a==None and b==None:
                return True

            elif a==None or b==None:
                return False

            elif a.val !=b.val:
                return False

            else:
                return sameTree(a.left,b.left) and sameTree(a.right,b.right)

        if root == None:
            return False

        if sameTree(root,subRoot):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)



#leetcode 235 二叉搜索树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)

        else:
            return root
