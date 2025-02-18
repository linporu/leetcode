from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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
