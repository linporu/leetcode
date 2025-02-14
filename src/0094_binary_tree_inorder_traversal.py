from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive method
class Solution01:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, result):
            if node is None:
                return
            dfs(node.left, result)
            result.append(node.val)
            dfs(node.right, result)
            return result

        result = []
        dfs(root, result)
        return result
