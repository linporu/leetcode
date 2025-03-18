from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        component_count = 0
        visited = set()

        def dfs(node):
            if node in visited:
                return

            row, col = node
            if row < 0 or row >= len(grid):
                return
            if col < 0 or col >= len(grid[0]):
                return
            if grid[row][col] == "0":
                return

            visited.add(node)
            dfs((row + 1, col))
            dfs((row - 1, col))
            dfs((row, col + 1))
            dfs((row, col - 1))

        for row_idx, row in enumerate(grid):
            for col_idx, val in enumerate(row):
                node = (row_idx, col_idx)
                if val == "1" and node not in visited:
                    component_count += 1
                    dfs(node)

        return component_count
