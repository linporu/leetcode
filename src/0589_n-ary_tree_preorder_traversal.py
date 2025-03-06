from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []


# Recursice method
class Solution01:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            if not node:
                return

            result.append(node.val)

            for child in node.children:
                dfs(child)

        result = []
        dfs(root)
        return result


# Iterative method
class Solution02:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            for child in reversed(node.children):
                stack.append(child)

        return result


# Optimized iterative method
class Solution03:
    def preorder(self, root: 'Node') -> List[int]:
        """
        用 range(len(node.children) - 1, -1, -1) 代替 reversed()
        此方法時間效能最佳！
        """
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            # 避免使用 reversed() 函數，直接從後往前遍歷
            for i in range(len(node.children) - 1, -1, -1):
                stack.append(node.children[i])

        return result


# Generator method for memory efficiency
class Solution04:
    def preorder(self, root: 'Node') -> List[int]:
        # 使用生成器函數來產生前序遍歷結果
        def preorder_generator(node):
            if not node:
                return

            yield node.val

            for child in node.children:
                yield from preorder_generator(child)

        # 將生成器結果轉換為列表
        return list(preorder_generator(root))
