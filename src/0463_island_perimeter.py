from typing import List


# BFS
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        from collections import deque

        # Search the first land
        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                if col == 1:
                    start = (row_idx, col_idx)
                    break

        queue = deque([start])
        visited = set([start])
        curr_perimeter = 0

        while queue:
            curr_row, curr_col = queue.popleft()
            neighbors = [
                (curr_row + 1, curr_col),
                (curr_row - 1, curr_col),
                (curr_row, curr_col + 1),
                (curr_row, curr_col - 1),
            ]

            for neighbor in neighbors:
                neighbor_row, neighbor_col = neighbor

                # Check neighnor is valid
                if neighbor_row < 0 or neighbor_row >= len(grid):
                    curr_perimeter += 1
                    continue
                if neighbor_col < 0 or neighbor_col >= len(grid[0]):
                    curr_perimeter += 1
                    continue

                if grid[neighbor_row][neighbor_col] == 0:  # Water
                    curr_perimeter += 1
                else:  # Land
                    if (neighbor_row, neighbor_col) not in visited:
                        visited.add((neighbor_row, neighbor_col))
                        queue.append((neighbor_row, neighbor_col))

        return curr_perimeter
