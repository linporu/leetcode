from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative DFS
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        path_sum = {root: root.val}
        prev = {root: None}
        stack = [root]
        result = []

        while stack:
            node = stack.pop()

            if not node.left and not node.right and (path_sum[node] == targetSum):
                path = []
                curr_node = node
                while curr_node:
                    path.append(curr_node.val)
                    curr_node = prev[curr_node]
                path.reverse()
                result.append(path)
            if node.left:
                stack.append(node.left)
                prev[node.left] = node
                path_sum[node.left] = path_sum[node] + node.left.val
            if node.right:
                stack.append(node.right)
                prev[node.right] = node
                path_sum[node.right] = path_sum[node] + node.right.val

        return result
