from typing import List


# Iterative DFS by AI
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        # 構建圖
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)

        # 初始化結果
        ancestors = [set() for _ in range(n)]

        # 對每個節點進行DFS
        for i in range(n):
            stack = [i]
            visited = set()
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        # i是neighbor的祖先
                        ancestors[neighbor].add(i)
                        stack.append(neighbor)
                        visited.add(neighbor)

        # 將集合轉換為有序列表
        return [sorted(list(ancestor)) for ancestor in ancestors]
