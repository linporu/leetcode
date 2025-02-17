from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive method
class Solution01:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node, result):
            if node is None:
                return
            result.append(node.val)
            dfs(node.left, result)
            dfs(node.right, result)
            return result

        result = []
        dfs(root, result)
        return result


# Iterative method
class Solution02:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            current = stack.pop()
            result.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return result
