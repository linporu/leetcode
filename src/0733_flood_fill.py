from typing import List


# Recursive DFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def flood(r, c, starting_color, visited):
            if (r, c) in visited:
                return
            else:
                image[r][c] = color
                visited.add((r, c))

            m = len(image)
            n = len(image[0])

            if r + 1 < m and image[r + 1][c] == starting_color:
                flood(r + 1, c, starting_color, visited)
            if r - 1 >= 0 and image[r - 1][c] == starting_color:
                flood(r - 1, c, starting_color, visited)
            if c + 1 < n and image[r][c + 1] == starting_color:
                flood(r, c + 1, starting_color, visited)
            if c - 1 >= 0 and image[r][c - 1] == starting_color:
                flood(r, c - 1, starting_color, visited)

        starting_color = image[sr][sc]
        visited = set()
        flood(sr, sc, starting_color, visited)

        return image
