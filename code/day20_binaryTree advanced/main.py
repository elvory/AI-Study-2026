#leetcode 543
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        def dfs(node):
            if node is None:
                return 0

            # 这里计算左右高度
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # 这里更新直径
            self.diameter = max(
                self.diameter,
                left_height+right_height
            )

            # 这里返回当前节点高度
            return 1+max(left_height,right_height)

        dfs(root)

        return self.diameter



#leetcode 110
class Solution:
    def isBalanced(self, root):

        def dfs_(node):


            if node is None:
                return 0

            #记录高度
            left_height = dfs_(node.left)

            if left_height == -1:
                return -1

            right_height = dfs_(node.right)

            if right_height == -1:
                return -1


            if abs(left_height-right_height)>1:
                return -1

            elif abs(left_height-right_height)<=1:
                return 1+max(left_height,right_height)


        return dfs_(root) != -1
