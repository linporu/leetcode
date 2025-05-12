from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# First take
class Solution01:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        from collections import deque

        queue = deque([root])
        prev = {}
        prev[root] = 0
        targets = {x, y}
        parents = []
        depth = 0

        while queue:
            level_size = len(queue)
            depth += 1
            for _ in range(level_size):
                node = queue.popleft()
                if node.val in targets:
                    targets.remove(node.val)
                    parents.append([prev[node], depth])
                    # TODO: refactor and prune
                    if len(targets) == 0:
                        return (
                            len(parents) == 2
                            and (parents[0][1] == parents[1][1])
                            and (parents[0][0] != parents[1][0])
                        )
                if node.left:
                    queue.append(node.left)
                    prev[node.left] = node
                if node.right:
                    queue.append(node.right)
                    prev[node.right] = node
        return False


# Refactored by me, time efficiency beat 100%
class Solution02:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        from collections import deque

        queue = deque([root])
        prev = {root: 0}
        targets = {x: 0, y: 0}
        parents = set()
        depth = 0

        while queue:
            level_size = len(queue)
            depth += 1
            for _ in range(level_size):
                node = queue.popleft()
                if node.val in targets:
                    targets[node.val] = depth
                    parents.add(prev[node])

                if node.left:
                    queue.append(node.left)
                    prev[node.left] = node
                if node.right:
                    queue.append(node.right)
                    prev[node.right] = node
            # Prune when cousins are not at same depth
            if not (targets[x] == targets[y]):
                return False
            if targets[x] > 0 and len(parents) == 2:
                return True
        return False


# AI refactored, DFS-based and memory-optimized solution
class Solution03:
    """
    記憶體優化版解法，專注於最小化記憶體使用

    優化重點：
    1. 極簡數據結構：
       - 使用最少的變數追蹤必要信息
       - 避免使用複雜的數據結構和巢狀循環
       - 不存儲不必要的節點信息

    2. 遞迴方法：
       - 使用遞迴而非 BFS，減少隊列開銷
       - 遞迴過程中只追蹤必要的信息
       - 提前返回不必要的遞迴路徑

    3. 記憶體效率：
       - 只存儲目標節點的深度和父節點值
       - 使用基本數據類型而非複雜對象
       - 避免創建不必要的臨時對象
    """

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # 存儲目標節點的信息：[深度, 父節點值]
        x_info = [-1, -1]
        y_info = [-1, -1]

        def dfs(node, parent_val, depth):
            if not node:
                return

            # 找到目標節點，記錄信息
            if node.val == x:
                x_info[0] = depth
                x_info[1] = parent_val
            elif node.val == y:
                y_info[0] = depth
                y_info[1] = parent_val

            # 如果兩個目標都找到了，停止遞迴
            if x_info[0] != -1 and y_info[0] != -1:
                return

            # 繼續遞迴搜索
            dfs(node.left, node.val, depth + 1)

            # 如果兩個目標都找到了，停止遞迴
            if x_info[0] != -1 and y_info[0] != -1:
                return

            dfs(node.right, node.val, depth + 1)

        # 從根節點開始遞迴
        dfs(root, -1, 0)

        # 檢查是否為表兄弟：深度相同但父節點不同
        return x_info[0] == y_info[0] and x_info[0] != -1 and x_info[1] != y_info[1]
