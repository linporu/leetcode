from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive method
class Solution01:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(node, level, result):
            if not node:
                return
            if len(result) == level:
                result.append([])

            result[level].append(node.val)
            dfs(node.left, level + 1, result)
            dfs(node.right, level + 1, result)
            return result

        result = []
        dfs(root, 0, result)
        return result
