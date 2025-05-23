from typing import List


# Iterative DFS
# 非常省記憶體，但時間不快
class Solution01:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        stack = [(0, [0])]  # (node, path)

        while stack:
            node, path = stack.pop()

            if node == len(graph) - 1:
                result.append(path.copy())

            if not graph[node]:
                continue

            for next_node in graph[node]:
                new_path = path.copy()
                new_path.append(next_node)
                stack.append((next_node, new_path))

        return result


# Recursive DFS
# 時間超快，因為不用一直 path.copy()
class Solution02:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(node, path):
            if node == len(graph) - 1:
                result.append(path.copy())
                return

            if not graph[node]:
                return

            for next_node in graph[node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()

        result = []
        backtrack(0, [0])
        return result


# Iterative BFS
# 慢，空間也沒比較省
class Solution03:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        from collections import deque

        result = []
        queue = deque([(0, [0])])  # (node, path)

        while queue:
            node, path = queue.popleft()

            if node == len(graph) - 1:
                result.append(path.copy())

            if not graph[node]:
                continue

            for next_node in graph[node]:
                new_path = path.copy()
                new_path.append(next_node)
                queue.append((next_node, new_path))

        return result
