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


# Iterative DFS
class Solution02:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # 構建鄰接表
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        stack = [source]

        while stack:
            node = stack.pop()

            if node == destination:
                return True

            if node not in visited:
                visited.add(node)
                for next_node in adj[node]:
                    if next_node not in visited:
                        stack.append(next_node)

        return False


# Iterative BFS
class Solution03:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import deque

        # 構建鄰接表
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set([source])
        queue = deque([source])

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            for next_node in adj[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(next_node)

        return False


# Union-Find
# 很省記憶體，但速度比 DFS 和 BFS 略慢
class Solution04:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        parent = {i: i for i in range(n)}
        rank = {i: 0 for i in range(n)}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return

            if rank[root_x] < rank[root_y]:
                root_x, root_y = root_y, root_x
            parent[root_y] = root_x
            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1

        for u, v in edges:
            union(u, v)

        return find(source) == find(destination)
