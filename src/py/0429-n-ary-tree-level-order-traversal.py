from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        from collections import deque

        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            current_level = []
            level_length = len(queue)

            for _ in range(level_length):
                node = queue.popleft()
                current_level.append(node.val)

                for child in node.children:
                    queue.append(child)

            result.append(current_level)

        return result
