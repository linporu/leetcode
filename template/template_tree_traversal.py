from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NaryTreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children else []


class TreeTraversal:
    """樹狀結構遍歷模板類"""

    @staticmethod
    def preorder_recursive(root: Optional[TreeNode]) -> List[int]:
        """前序遍歷（遞迴）- 根->左->右"""

        def dfs(node: Optional[TreeNode], result: List[int]) -> None:
            if not node:
                return
            result.append(node.val)  # 訪問根節點
            dfs(node.left, result)  # 遍歷左子樹
            dfs(node.right, result)  # 遍歷右子樹

        result = []
        dfs(root, result)
        return result

    @staticmethod
    def inorder_recursive(root: Optional[TreeNode]) -> List[int]:
        """中序遍歷（遞迴）- 左->根->右"""

        def dfs(node: Optional[TreeNode], result: List[int]) -> None:
            if not node:
                return
            dfs(node.left, result)  # 遍歷左子樹
            result.append(node.val)  # 訪問根節點
            dfs(node.right, result)  # 遍歷右子樹

        result = []
        dfs(root, result)
        return result

    @staticmethod
    def postorder_recursive(root: Optional[TreeNode]) -> List[int]:
        """後序遍歷（遞迴）- 左->右->根"""

        def dfs(node: Optional[TreeNode], result: List[int]) -> None:
            if not node:
                return
            dfs(node.left, result)  # 遍歷左子樹
            dfs(node.right, result)  # 遍歷右子樹
            result.append(node.val)  # 訪問根節點

        result = []
        dfs(root, result)
        return result

    @staticmethod
    def levelorder_recursive(root: Optional[TreeNode]) -> List[List[int]]:
        """層序遍歷（遞迴）"""

        def dfs(node: Optional[TreeNode], level: int, result: List[List[int]]) -> None:
            if not node:
                return
            # 如果當前層級還沒有對應的列表，就創建一個
            if len(result) == level:
                result.append([])
            # 將當前節點的值加入對應層級的列表
            result[level].append(node.val)
            # 遞迴處理左右子樹，層級加1
            dfs(node.left, level + 1, result)
            dfs(node.right, level + 1, result)

        result = []
        dfs(root, 0, result)
        return result

    @staticmethod
    def preorder_iterative(root: Optional[TreeNode]) -> List[int]:
        """前序遍歷（迭代）- 根->左->右"""
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)
            # 注意：因為是使用堆疊，所以要先將右子節點壓入堆疊
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    @staticmethod
    def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
        """中序遍歷（迭代）- 左->根->右"""
        result = []
        stack = []
        current = root

        while current or stack:
            # 一直往左走，將所有左子節點壓入堆疊
            while current:
                stack.append(current)
                current = current.left

            # 處理當前節點
            current = stack.pop()
            result.append(current.val)

            # 移動到右子節點
            current = current.right

        return result

    @staticmethod
    def postorder_iterative(root: Optional[TreeNode]) -> List[int]:
        """後序遍歷（迭代）- 左->右->根"""
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

    @staticmethod
    def levelorder_iterative(root: Optional[TreeNode]) -> List[List[int]]:
        """層序遍歷（迭代）"""
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result


class NaryTreeTraversal:
    """N叉樹遍歷模板類"""

    @staticmethod
    def preorder_recursive(root: Optional[NaryTreeNode]) -> List[int]:
        """前序遍歷（遞迴）- 根->子節點"""

        def dfs(node: Optional[NaryTreeNode], result: List[int]) -> None:
            if not node:
                return
            result.append(node.val)  # 訪問根節點
            for child in node.children:  # 遍歷所有子節點
                dfs(child, result)

        result = []
        dfs(root, result)
        return result

    @staticmethod
    def postorder_recursive(root: Optional[NaryTreeNode]) -> List[int]:
        """後序遍歷（遞迴）- 子節點->根"""

        def dfs(node: Optional[NaryTreeNode], result: List[int]) -> None:
            if not node:
                return
            for child in node.children:  # 先遍歷所有子節點
                dfs(child, result)
            result.append(node.val)  # 最後訪問根節點

        result = []
        dfs(root, result)
        return result

    @staticmethod
    def levelorder_recursive(root: Optional[NaryTreeNode]) -> List[List[int]]:
        """層序遍歷（遞迴）"""

        def dfs(node: Optional[NaryTreeNode], level: int, result: List[List[int]]) -> None:
            if not node:
                return
            # 如果當前層級還沒有對應的列表，就創建一個
            if len(result) == level:
                result.append([])
            # 將當前節點的值加入對應層級的列表
            result[level].append(node.val)
            # 遞迴處理所有子節點，層級加1
            for child in node.children:
                dfs(child, level + 1, result)

        result = []
        dfs(root, 0, result)
        return result

    @staticmethod
    def preorder_iterative(root: Optional[NaryTreeNode]) -> List[int]:
        """前序遍歷（迭代）- 根->子節點"""
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)
            # 注意：因為是使用堆疊，所以要從右到左將子節點壓入堆疊
            # 這樣出堆疊時就會從左到右處理子節點
            for child in reversed(node.children):
                stack.append(child)

        return result

    @staticmethod
    def postorder_iterative(root: Optional[NaryTreeNode]) -> List[int]:
        """後序遍歷（迭代）- 子節點->根"""
        if not root:
            return []

        result = []
        stack = [(root, False)]  # (節點, 是否已訪問過子節點)

        while stack:
            node, visited = stack.pop()

            if visited:
                result.append(node.val)
            else:
                # 重新壓入當前節點，標記為已訪問
                stack.append((node, True))
                # 從右到左將子節點壓入堆疊
                for child in reversed(node.children):
                    stack.append((child, False))

        return result

    @staticmethod
    def levelorder_iterative(root: Optional[NaryTreeNode]) -> List[List[int]]:
        """層序遍歷（迭代）"""
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                # 將所有子節點加入隊列
                for child in node.children:
                    queue.append(child)

            result.append(current_level)

        return result
