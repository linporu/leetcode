from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive method
class Solution01:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, depth):

            result = True

            if not node:
                return depth - 1, result

            depth_left, result_left = dfs(node.left, depth + 1)
            depth_right, result_right = dfs(node.right, depth + 1)

            if abs(depth_left - depth_right) > 1:
                result = False
            if not (result_left and result_right):
                result = False

            return max(depth_left, depth_right), result

        # Base case
        if not root:
            return True

        max_depth, result = dfs(root, 1)
        return result
