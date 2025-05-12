from typing import List


# BFS
class Solution01:
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


# Iterate all cells
class Solution02:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        land_count = 0
        neighbor_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    land_count += 1
                    # 檢查右邊和下方的鄰居
                    if r < rows - 1 and grid[r + 1][c] == 1:
                        neighbor_count += 1
                    if c < cols - 1 and grid[r][c + 1] == 1:
                        neighbor_count += 1

        # 周長 = 陸地數量*4 - 相鄰邊數*2
        return land_count * 4 - neighbor_count * 2
