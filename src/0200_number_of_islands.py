from typing import List


# Recursive DFS with visited set
class Solution01:
    def numIslands(self, grid: List[List[str]]) -> int:
        component_count = 0
        visited = set()

        def dfs(node):
            if node in visited:
                return

            row, col = node
            if row < 0 or row >= len(grid):
                return
            if col < 0 or col >= len(grid[0]):
                return
            if grid[row][col] == "0":
                return

            visited.add(node)
            dfs((row + 1, col))
            dfs((row - 1, col))
            dfs((row, col + 1))
            dfs((row, col - 1))

        for row_idx, row in enumerate(grid):
            for col_idx, val in enumerate(row):
                node = (row_idx, col_idx)
                if val == "1" and node not in visited:
                    component_count += 1
                    dfs(node)

        return component_count


# Optimized DFS with in-place marking
class Solution02:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            # 檢查邊界條件和是否為陸地
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return

            # 將已訪問的陸地標記為已訪問（直接修改原網格）
            grid[i][j] = "#"  # 使用特殊標記避免與水（"0"）混淆

            # 訪問四個方向
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # 遍歷網格
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count


# Iterative BFS with in-place marking
class Solution03:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque

        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右、下、左、上

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    grid[i][j] = "#"  # 標記為已訪問

                    # 使用 BFS 訪問鄰近的陸地
                    queue = deque([(i, j)])
                    while queue:
                        curr_i, curr_j = queue.popleft()

                        # 檢查四個方向
                        for di, dj in directions:
                            ni, nj = curr_i + di, curr_j + dj

                            # 檢查邊界和是否為陸地
                            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                                grid[ni][nj] = "#"  # 標記為已訪問
                                queue.append((ni, nj))

        return count
