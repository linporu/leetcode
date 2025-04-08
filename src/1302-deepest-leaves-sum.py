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


# Recursive DFS
class Solution03:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """
        使用 DFS 配合遞迴，記錄目前深度和最大深度。
        當發現更深的葉子節點時，重置 sum。
        當深度等於最大深度時，累加節點值。
        """
        max_depth = 0
        deepest_sum = 0

        def dfs(node: TreeNode, depth: int) -> None:
            if not node:
                return

            nonlocal max_depth, deepest_sum

            # 更新最大深度和重置 sum
            if depth > max_depth:
                max_depth = depth
                deepest_sum = node.val
            # 在最大深度累加節點值
            elif depth == max_depth:
                deepest_sum += node.val

            # 遞迴處理左右子樹
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return deepest_sum
