from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        from collections import deque

        queue = deque([root])
        prev = {}
        prev[root] = 0
        targets = {x, y}
        parents = []
        depth = 0

        while queue:
            level_size = len(queue)
            depth += 1
            for _ in range(level_size):
                node = queue.popleft()
                if node.val in targets:
                    targets.remove(node.val)
                    parents.append([prev[node], depth])
                    if len(targets) == 0:
                        return (
                            len(parents) == 2
                            and (parents[0][1] == parents[1][1])
                            and (parents[0][0] != parents[1][0])
                        )
                if node.left:
                    queue.append(node.left)
                    prev[node.left] = node
                if node.right:
                    queue.append(node.right)
                    prev[node.right] = node
        return False
