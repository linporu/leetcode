from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive method
class Solution01:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check(node_left, node_right):
            if not node_left and not node_right:
                return True
            elif not node_left or not node_right:
                return False
            else:
                return (
                    node_left.val == node_right.val
                    and check(node_left.left, node_right.right)
                    and check(node_left.right, node_right.left)
                )

        return check(root.left, root.right)


# Iterative method
class Solution02:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Base cases
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False

        stack = [(root.left, root.right)]

        while stack:
            node_left, node_right = stack.pop()
            if not node_left and not node_right:
                continue
            if not node_left or not node_right:
                return False
            if node_left.val != node_right.val:
                return False

            stack.append([node_left.left, node_right.right])
            stack.append([node_left.right, node_right.left])

        return True
