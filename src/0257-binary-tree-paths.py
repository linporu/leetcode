from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive DFS
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path, result):
            if not node:
                return result
            path += str(node.val)
            if not node.left and not node.right:
                path.rstrip("->")
                result.append(path)
            if node.left:
                dfs(node.left, path + "->", result)
            if node.right:
                dfs(node.right, path + "->", result)
            return result

        return dfs(root, "", [])
