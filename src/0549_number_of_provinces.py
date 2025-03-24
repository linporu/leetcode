from typing import List


# Recursive DFS
# 快
class Solution01:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        count = 0

        def dfs(i):
            if i in visited:
                return

            visited.add(i)

            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j)

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count


# Union-Find
# 較省記憶體
class Solution02:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1

        # 合併所有直接相連的城市
        for i in range(n):
            for j in range(i + 1, n):  # 只需要檢查上三角矩陣
                if isConnected[i][j]:
                    union(i, j)

        # 計算不同的根節點數量（即省份數量）
        return sum(parent[i] == i for i in range(n))
