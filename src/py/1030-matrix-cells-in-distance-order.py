from typing import List


# Iterative BFS
class Solution01:
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


# 計算並按照距離排序（字典儲存）
class Solution02:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:
        # 創建一個字典，key 是距離，value 是具有該距離的單元格列表
        distance_dict = {}

        # 遍歷所有單元格
        for r in range(rows):
            for c in range(cols):
                # 計算曼哈頓距離
                distance = abs(r - rCenter) + abs(c - cCenter)

                # 如果該距離不在字典中，初始化為空列表
                if distance not in distance_dict:
                    distance_dict[distance] = []

                # 將單元格加入對應距離的列表
                distance_dict[distance].append([r, c])

        # 創建結果列表
        result = []

        # 按照距離順序合併所有單元格列表
        for distance in sorted(distance_dict.keys()):
            result.extend(distance_dict[distance])

        return result


# 計算並按照距離排序（直接排序陣列內元素）
class Solution03:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:

        def distance(point):
            pi, pj = point
            return abs(pi - rCenter) + abs(pj - cCenter)

        points = [(i, j) for i in range(rows) for j in range(cols)]
        return sorted(points, key=distance)
