from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive DFS
class Solution01:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, sum, targetSum):
            if not node:
                return

            sum += node.val

            if not node.left and not node.right:
                return sum == targetSum

            result_left = dfs(node.left, sum, targetSum) if node.left else False
            result_right = dfs(node.right, sum, targetSum) if node.right else False

            return True if result_left or result_right else False

        if not root:
            return False

        return dfs(root, 0, targetSum)


class Solution02:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """Find if there exists a root-to-leaf path that sums to targetSum.
        - 用 if not node return False 來處理 root is None
        - 用 curr_sum 取代 sum 以免函數名稱和 sum() 衝突
        - 利用 Python 閉包（closure）特性，不用在 dfs() 傳遞 targetSum
        - 簡化成 return result_left or result_right
        """

        def dfs(node: Optional[TreeNode], curr_sum: int) -> bool:
            if not node:
                return False

            curr_sum += node.val

            if not node.left and not node.right:
                return curr_sum == targetSum

            result_left = dfs(node.left, curr_sum) if node.left else False
            result_right = dfs(node.right, curr_sum) if node.right else False
            return result_left or result_right

        return dfs(root, 0)
