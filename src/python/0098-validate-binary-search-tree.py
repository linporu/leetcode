from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive DFS
class Solution01:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        所有左子樹必須小於根節點, 所有右子樹必須大於根節點
        """

        def dfs(node, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        return dfs(root, float("-inf"), float("inf"))


# Iterative DFS
class Solution02:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        使用中序遍歷（Inorder Traversal）驗證二元搜尋樹
        原理：BST 的中序遍歷結果必須是嚴格遞增的序列
        時間複雜度：O(n)，其中 n 是節點數
        空間複雜度：O(h)，其中 h 是樹高，最差情況下為 O(n)
        """
        # 空樹也是有效的 BST
        if not root:
            return True

        stack = []
        curr = root
        prev_val = float("-inf")  # 用於追蹤前一個節點的值

        while stack or curr:
            # 遍歷到最左邊的節點
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # 檢查當前值是否大於前一個值
            if curr.val <= prev_val:
                return False

            prev_val = curr.val
            curr = curr.right

        return True
