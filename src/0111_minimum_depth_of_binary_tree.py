from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative BFS
class Solution01:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        if not root:
            return 0

        queue = deque([root])
        min_depth = 1

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                if not node.left and not node.right:
                    return min_depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            min_depth += 1

        return min_depth


# Dijkstra
class Solution02:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        import heapq

        # 使用字典而不是集合來追蹤已訪問的節點及其距離
        distances = {root: 0}
        # 使用計數器來避免比較 TreeNode 物件
        counter = 0
        # 優先隊列：(距離, 計數器, 節點)
        pq = [(0, counter, root)]

        while pq:
            curr_distance, _, curr_node = heapq.heappop(pq)

            # 如果找到葉子節點，返回其深度
            if not curr_node.left and not curr_node.right:
                return curr_distance + 1

            # 處理左子節點
            if curr_node.left and (
                curr_node.left not in distances or curr_distance + 1 < distances[curr_node.left]
            ):
                distances[curr_node.left] = curr_distance + 1
                counter += 1
                heapq.heappush(pq, (curr_distance + 1, counter, curr_node.left))

            # 處理右子節點
            if curr_node.right and (
                curr_node.right not in distances or curr_distance + 1 < distances[curr_node.right]
            ):
                distances[curr_node.right] = curr_distance + 1
                counter += 1
                heapq.heappush(pq, (curr_distance + 1, counter, curr_node.right))
