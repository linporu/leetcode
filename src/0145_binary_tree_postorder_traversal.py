from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive method
class Solution01:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, result):
            if node is None:
                return

            dfs(node.left, result)
            dfs(node.right, result)
            result.append(node.val)
            return result

        result = []
        dfs(root, result)
        return result


# Iterative method
class Solution02:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = [(root, False)]  # (節點, 是否已訪問過右子樹)

        while stack:
            node, visited = stack.pop()
            # 如果是葉節點或已經訪問過右子樹
            if not node.left and not node.right or visited:
                result.append(node.val)
            else:
                # 重新壓入當前節點，標記為已訪問
                stack.append((node, True))
                # 先壓入右子節點（因為後序遍歷是左->右->根）
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

        return result
