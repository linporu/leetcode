from typing import List


# Iterative BFS
class Solution:
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
