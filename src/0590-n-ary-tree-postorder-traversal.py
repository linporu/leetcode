from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


# Recursive method
class Solution01:
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


# Iterative method
class Solution02:
    def postorder(self, root: 'Node') -> List[int]:
        # Base case
        if not root:
            return []

        result = []
        stack = [(root, False)]

        while stack:
            node, is_visited = stack.pop()

            if not is_visited:
                stack.append((node, True))

                for i in range(len(node.children) - 1, -1, -1):
                    stack.append((node.children[i], False))

            else:
                result.append(node.val)

        return result
