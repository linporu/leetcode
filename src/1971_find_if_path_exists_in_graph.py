from typing import List


# Recursive DFS
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node, visited):
            if node == destination:
                return True

            visited.add(node)

            for neighbor in adj[node]:
                if neighbor in visited:
                    continue
                if dfs(neighbor, visited):
                    return True

            return False

        # 構建鄰接表
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        return dfs(source, visited)
