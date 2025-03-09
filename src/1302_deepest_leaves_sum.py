from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative BFS
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        # Base case
        if not root:
            return 0

        queue = deque([root])
        max_depth = 0
        deepest_leaves_sum = 0

        # First traversal to find max depth
        while queue:
            max_depth += 1
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        # Second traversal to count the deepest leaves sum
        queue.append(root)
        curr_depth = 0
        while queue:
            curr_depth += 1
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                if curr_depth == max_depth:
                    deepest_leaves_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return deepest_leaves_sum
