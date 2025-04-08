from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive method
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


# Recursive method refactored
class Solution02:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """重構改進說明：
        1. 先處理基本情況（base cases）：
           - 兩個節點都是 None
           - 其中一個節點是 None
        2. 使用 and 運算子串接所有條件，使邏輯更清晰
        3. 移除了多餘的 result 變數和巢狀的 if 判斷

        時間複雜度：O(n)，其中 n 是節點總數，需要遍歷每個節點
        空間複雜度：O(h)，其中 h 是樹的高度，這是由於遞迴調用堆疊的深度
        """

        def check(node_1, node_2):
            # 兩個節點都是 None，代表相同
            if not node_1 and not node_2:
                return True
            # 其中一個是 None，另一個不是，代表不同
            if not node_1 or not node_2:
                return False
            # 檢查當前節點值是否相同，以及左右子樹是否相同
            return (
                node_1.val == node_2.val
                and check(node_1.left, node_2.left)
                and check(node_1.right, node_2.right)
            )

        return check(p, q)


# Iterative method
class Solution03:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Base cases
        if not p and not q:
            return True
        if not p or not q:
            return False

        stack = [(p, q)]

        while stack:
            node_1, node_2 = stack.pop()

            if not node_1 and not node_2:
                continue
            if not node_1 or not node_2:
                return False
            if node_1.val != node_2.val:
                return False

            stack.append((node_1.right, node_2.right))
            stack.append((node_1.left, node_2.left))

        return True
