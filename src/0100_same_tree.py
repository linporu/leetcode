from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution01:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def check(node_1, node_2):
            result = True
            if node_1 and node_2:
                if node_1.val != node_2.val:
                    result = False
                if not check(node_1.left, node_2.left) or not check(node_1.right, node_2.right):
                    return False
            elif not node_1 and not node_2:
                result = True
            else:
                result = False
            return result

        return check(p, q)
