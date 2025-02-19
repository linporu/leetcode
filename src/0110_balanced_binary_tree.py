from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive method
class Solution01:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, depth):

            result = True

            if not node:
                return depth - 1, result

            depth_left, result_left = dfs(node.left, depth + 1)
            depth_right, result_right = dfs(node.right, depth + 1)

            if abs(depth_left - depth_right) > 1:
                result = False
            if not (result_left and result_right):
                result = False

            return max(depth_left, depth_right), result

        # Base case
        if not root:
            return True

        max_depth, result = dfs(root, 1)
        return result


# Recursive method (refactored)
class Solution02:
    """
    Optimized recursive solution using height-based approach.

    Key optimizations:
    1. Early termination: Uses -1 as a special value to indicate an unbalanced subtree
       and propagates it up immediately, avoiding unnecessary computations
    2. Single return value: Returns only height instead of (height, result) tuple,
       reducing memory usage and computation overhead
    3. Simplified logic: Combines balance checking and height calculation in one value,
       making the code more concise and efficient

    Time Complexity: O(n) where n is number of nodes
    Space Complexity: O(h) where h is height of tree, due to recursion stack
    """

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            # Base case
            if not node:
                return 0

            # Check left tree
            depth_left = dfs(node.left)
            if depth_left == -1:
                return -1

            # Check right tree
            depth_right = dfs(node.right)
            if depth_right == -1:
                return -1

            # Check balance
            if abs(depth_left - depth_right) > 1:
                return -1

            return max(depth_left, depth_right) + 1

        return False if dfs(root) == -1 else True
