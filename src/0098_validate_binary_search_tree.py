from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive DFS
class Solution01:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        所有左子樹必須小於根節點, 所有右子樹必須大於根節點
        """

        def dfs(node, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        return dfs(root, float('-inf'), float('inf'))
