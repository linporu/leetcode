from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative BFS
class Solution01:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        if not root:
            return 0

        queue = deque([root])
        min_depth = 1

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                if not node.left and not node.right:
                    return min_depth
                if node.left:

                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            min_depth += 1

        return min_depth
