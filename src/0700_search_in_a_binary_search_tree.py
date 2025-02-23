from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def bst(node):
            if not node:
                return None
            if node.val == val:
                return node
            elif node.val > val:
                return bst(node.left)
            else:
                return bst(node.right)

        return bst(root)
