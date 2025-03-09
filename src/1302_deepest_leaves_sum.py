from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative BFS
class Solution01:
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


# Iterative BFS refactored
class Solution02:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """
        利用 BFS 特性，實現一次遍歷即得結果。
        每層累加該層 node.val，進入下一層時歸零。
        """
        from collections import deque

        # Base case
        if not root:
            return 0

        queue = deque([root])
        curr_depth = 0

        while queue:
            curr_depth += 1
            level_size = len(queue)
            deepest_leaves_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                deepest_leaves_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return deepest_leaves_sum
