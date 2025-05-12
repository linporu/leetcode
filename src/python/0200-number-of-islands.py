from typing import List


"""
LeetCode 200. Number of Islands

四種解法比較：

1. Solution01: 遞迴 DFS + visited 集合
   - 時間複雜度：O(M×N)，其中 M 是網格的行數，N 是網格的列數
   - 空間複雜度：O(M×N)，來自於 visited 集合和遞迴調用棧
   - 優點：實現簡單直觀，不修改原始輸入資料
   - 缺點：需要額外的記憶體來儲存 visited 集合，遞迴調用可能導致棧溢出

2. Solution02: 優化的遞迴 DFS + 原地標記
   - 時間複雜度：O(M×N)
   - 空間複雜度：O(max(M,N))，僅來自遞迴調用棧
   - 優點：不需要額外的 visited 集合，節省記憶體，邊界條件檢查更高效
   - 缺點：修改了原始輸入資料，仍然使用遞迴，可能有棧溢出風險

3. Solution03: 迭代式 BFS + 原地標記
   - 時間複雜度：O(M×N)
   - 空間複雜度：O(min(M,N))，來自於 BFS 隊列
   - 優點：避免了遞迴調用，不會有棧溢出風險，在島嶼較大時可能更高效
   - 缺點：同樣修改了原始輸入資料，實現稍微複雜一些

4. Solution04: Union-Find (並查集)
   - 時間複雜度：O(M×N×α(M×N))，其中 α 是阿克曼函數的反函數，實際上接近 O(M×N)
   - 空間複雜度：O(M×N)，用於存儲 parent 和 rank 映射
   - 優點：理論基礎扎實，適合動態問題（如果網格會變化）
   - 缺點：實現較複雜，初始化開銷大

選擇建議：
- 一般情況下：Solution02（優化的遞迴 DFS）通常是最佳選擇
- 對於非常大的網格：Solution03（迭代式 BFS）可能更適合，避免棧溢出
- 如果需要保持原始資料不變：使用 Solution01 或先複製網格
- 如果網格會動態變化：考慮使用 Solution04（Union-Find）
"""


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


# Union-Find
class Solution04:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        # 只為陸地的格子創建並查集
        parent = {}
        rank = {}

        # 初始化並查集，每個陸地格子一開始是自己的父節點
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    parent[(i, j)] = (i, j)
                    rank[(i, j)] = 0

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # 路徑壓縮
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            # 按秩合併，將秩較小的樹接到秩較大的樹上
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        # 方向數組：右、下
        directions = [(0, 1), (1, 0)]

        # 將相鄰的陸地合併
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # 檢查右和下方向的相鄰格子
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                            union((i, j), (ni, nj))

        # 計算不同的陸地（不同的根節點數量）
        islands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands.add(find((i, j)))

        return len(islands)
