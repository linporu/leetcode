from typing import List


# Recursive DFS
class Solution01:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def flood(r, c, starting_color, visited):
            # 如果已經訪問過或超出邊界或顏色不符合，直接返回
            if (r, c) in visited:
                return
            if r < 0 or r >= len(image):
                return
            if c < 0 or c >= len(image[0]):
                return
            if image[r][c] != starting_color:
                return

            # 執行填色並標記為已訪問
            image[r][c] = color
            visited.add((r, c))

            # 遞迴訪問四個方向
            flood(r + 1, c, starting_color, visited)
            flood(r - 1, c, starting_color, visited)
            flood(r, c + 1, starting_color, visited)
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
