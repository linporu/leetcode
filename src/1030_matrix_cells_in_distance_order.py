from typing import List


# Iterative BFS
class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:
        from collections import deque

        result = []
        start = (rCenter, cCenter)
        visited = set()
        queue = deque([start])

        while queue:
            r, c = queue.popleft()

            # Prune visited cell
            if (r, c) in visited:
                continue

            # Prune invalid cell
            if r < 0 or r >= rows or c < 0 or c >= cols:
                continue

            queue.extend([(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)])
            result.append([r, c])
            visited.add((r, c))

        return result
