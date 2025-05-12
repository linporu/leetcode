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


# Iterative method
class Solution02:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result
