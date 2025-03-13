from typing import List


# Recursive DFS
class Solution01:
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


# Iterative DFS
class Solution02:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return [[]]

        starting_color = image[sr][sc]
        visited = set()
        stack = [(sr, sc)]

        while stack:
            r, c = stack.pop()

            if r < 0 or r >= len(image):
                continue
            if c < 0 or c >= len(image[0]):
                continue
            if (r, c) in visited:
                continue
            if image[r][c] != starting_color:
                continue

            image[r][c] = color
            visited.add((r, c))

            stack.append((r + 1, c))
            stack.append((r - 1, c))
            stack.append((r, c + 1))
            stack.append((r, c - 1))

        return image
