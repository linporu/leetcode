from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node):
            # Base case
            if not node:
                return 0
            if not node.children:
                return 1

            max_depth = 0
            for child in node.children:
                max_depth = max(dfs(child), max_depth)

            return max_depth + 1

        return dfs(root)
