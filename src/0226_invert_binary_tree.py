from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case
        if not root:
            return None

        # Save the reference of child node
        temp_left = root.left
        temp_right = root.right

        # Recursively invert the child nodes
        root.left = self.invertTree(temp_right)
        root.right = self.invertTree(temp_left)

        return root
