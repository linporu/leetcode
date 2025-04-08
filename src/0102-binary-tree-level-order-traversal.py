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


# Iterative method
class Solution02:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            current_level = []
            level_length = len(queue)

            for _ in range(level_length):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result
