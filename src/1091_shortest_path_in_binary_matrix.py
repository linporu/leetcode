from typing import List


# BFS
class Solution01:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque

        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        result = []
        visited = set()
        distance = 1
        queue = deque([(0, 0, 1)])

        while queue:
            r, c, distance = queue.popleft()

            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] == 1 or (r, c) in visited:
                continue

            if r == n - 1 and c == n - 1:
                result.append(distance)

            visited.add((r, c))

            neighbors = [
                (r - 1, c - 1),
                (r - 1, c),
                (r - 1, c + 1),
                (r, c - 1),
                (r, c + 1),
                (r + 1, c - 1),
                (r + 1, c),
                (r + 1, c + 1),
            ]

            for neighbor in neighbors:
                if neighbor not in visited:
                    new_distance = distance + 1
                    new_tuple = neighbor + (new_distance,)
                    queue.append(new_tuple)

        return min(result) if result else -1


# BFS (Optmized)
class Solution02:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque

        n = len(grid)

        # 檢查起點和終點是否可通行
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        # 如果只有一個格子的情況
        if n == 1:
            return 1

        # 定義8個方向的移動
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # 初始化訪問集合和隊列
        visited = {(0, 0)}
        queue = deque([(0, 0, 1)])  # (row, col, distance)

        while queue:
            r, c, distance = queue.popleft()

            # 檢查所有鄰居
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # 檢查邊界和是否可訪問
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:

                    # 如果到達終點，直接返回距離
                    if nr == n - 1 and nc == n - 1:
                        return distance + 1

                    # 標記為已訪問並加入隊列
                    visited.add((nr, nc))
                    queue.append((nr, nc, distance + 1))

        # 如果沒有找到路徑
        return -1
