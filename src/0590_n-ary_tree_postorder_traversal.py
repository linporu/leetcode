from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


# Recursive method
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            if not node:
                return

            for child in node.children:
                dfs(child)

            result.append(node.val)

        result = []
        dfs(root)
        return result
