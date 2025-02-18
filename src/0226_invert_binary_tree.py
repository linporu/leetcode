from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution01:
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


# With helper function
class Solution02:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(node):
            if node is None:
                return None

            temp_left = node.left
            temp_right = node.right
            node.left = invert(temp_right)
            node.right = invert(temp_left)

            return node

        return invert(root)
