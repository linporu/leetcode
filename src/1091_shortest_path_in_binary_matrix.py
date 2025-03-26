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


# Dijkstra
class Solution03:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        import heapq

        n = len(grid)

        # 檢查起點和終點是否可通行
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        if n == 1:
            return 1

        # 初始化距離矩陣
        distance = [[float("inf") for _ in range(n)] for _ in range(n)]
        distance[0][0] = 1

        # 初始化優先佇列和已訪問集合
        pq = [(1, 0, 0)]  # (距離, 行, 列)
        visited = set()

        # 定義8個方向的移動
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        while pq:
            curr_distance, r, c = heapq.heappop(pq)

            # 如果當前距離大於已知距離，跳過
            if curr_distance > distance[r][c]:
                continue

            # 如果到達終點，返回距離
            if r == n - 1 and c == n - 1:
                return curr_distance

            # 標記為已訪問
            visited.add((r, c))

            # 檢查所有鄰居
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # 檢查邊界和是否可訪問
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:

                    new_distance = curr_distance + 1

                    # 如果找到更短的路徑，更新距離並加入優先佇列
                    if new_distance < distance[nr][nc]:
                        distance[nr][nc] = new_distance
                        heapq.heappush(pq, (new_distance, nr, nc))

        return -1


# A* 算法
class Solution04:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        import heapq

        n = len(grid)

        # 檢查起點和終點是否可通行
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        if n == 1:
            return 1

        # 定義啟發函數：切比雪夫距離 (Chebyshev distance)
        def heuristic(r, c):
            # 計算到終點 (n-1, n-1) 的切比雪夫距離
            # 在八方向移動的網格中，切比雪夫距離更適合作為啟發函數
            return max(abs(r - (n - 1)), abs(c - (n - 1)))

        # 初始化距離矩陣
        g_score = [[float("inf") for _ in range(n)] for _ in range(n)]
        g_score[0][0] = 1  # 起點到起點的距離為 1（包含起點本身）

        # 初始化優先佇列：(f_score, g_score, row, col)
        # f_score = g_score + heuristic
        start_f_score = 1 + heuristic(0, 0)
        open_set = [(start_f_score, 1, 0, 0)]

        # 已訪問集合
        closed_set = set()

        # 定義8個方向的移動
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        while open_set:
            # 取出 f_score 最小的節點
            f_score, g, r, c = heapq.heappop(open_set)

            # 如果節點已經訪問過，跳過
            if (r, c) in closed_set:
                continue

            # 如果到達終點，返回距離
            if r == n - 1 and c == n - 1:
                return g

            # 標記為已訪問
            closed_set.add((r, c))

            # 檢查所有鄰居
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # 檢查邊界和是否可訪問
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in closed_set:

                    # 計算新的 g_score
                    new_g = g + 1

                    # 如果找到更短的路徑，更新 g_score 並加入開放集合
                    if new_g < g_score[nr][nc]:
                        g_score[nr][nc] = new_g
                        new_f = new_g + heuristic(nr, nc)
                        heapq.heappush(open_set, (new_f, new_g, nr, nc))

        # 如果沒有找到路徑
        return -1
