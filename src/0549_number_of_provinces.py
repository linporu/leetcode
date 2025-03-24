from typing import List


# Recursive DFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = {i: False for i in range(n)}
        count = 0

        def dfs(i):
            if visited[i]:
                return

            visited[i] = True

            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j)

        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)

        return count
