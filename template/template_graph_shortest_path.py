"""
圖論最短路徑模板 (Graph Shortest Path Template)

本模板包含：
1. BFS 最短路徑（無權圖或權重相同的圖）
2. Dijkstra 算法（帶權圖，無負權邊）
3. Bellman-Ford 算法（可處理負權邊）
4. Floyd-Warshall 算法（所有點對最短路徑）

適用於：
- 需要找出兩點間最短距離
- 需要計算最小成本路徑
- 需要處理加權圖的路徑問題

算法選擇依據：
- BFS 適用於無權圖或權重相同的圖（所有邊的權重都是 1）
- Dijkstra 適用於帶權圖，特別是權重不同的情況（無負權邊）
- Bellman-Ford 適用於可能存在負權邊的圖
- Floyd-Warshall 適用於需要計算所有點對最短路徑的情況
"""

from typing import List, Dict, Tuple, Optional, Any
from collections import deque
import heapq


class ShortestPath:
    """
    最短路徑算法
    """

    @staticmethod
    def bfs_shortest_path(
        graph: Dict[int, List[Any]], start: int, end: int
    ) -> Tuple[int, List[int]]:
        """
        使用 BFS 尋找無權圖中的最短路徑

        Args:
            graph: 鄰接列表表示的圖，格式為 {node: [neighbors]} 或 {node: [(neighbor, weight), ...]}
            start: 起始節點
            end: 目標節點

        Returns:
            Tuple[int, List[int]]: (最短距離, 最短路徑)，如果不存在路徑則返回 (-1, [])
        """
        if start == end:
            return 0, [start]

        visited = set([start])
        queue = deque([(start, 0, [start])])  # (節點, 距離, 路徑)

        while queue:
            node, distance, path = queue.popleft()

            for neighbor in graph.get(node, []):
                if isinstance(neighbor, tuple):  # 處理帶權重的情況
                    next_node = neighbor[0]
                else:
                    next_node = neighbor

                if next_node == end:
                    return distance + 1, path + [next_node]

                if next_node not in visited:
                    visited.add(next_node)
                    queue.append((next_node, distance + 1, path + [next_node]))

        return -1, []  # 不存在路徑

    @staticmethod
    def dijkstra(
        graph: Dict[int, List[Tuple[int, int]]], start: int, end: Optional[int] = None
    ) -> Dict[int, Tuple[int, List[int]]]:
        """
        Dijkstra 算法尋找帶權圖中的最短路徑

        Args:
            graph: 鄰接列表表示的圖，格式為 {node: [(neighbor, weight), ...]}
            start: 起始節點
            end: 目標節點，如果為 None 則計算從 start 到所有其他節點的最短路徑

        Returns:
            Dict[int, Tuple[int, List[int]]]: {目標節點: (最短距離, 最短路徑)}
        """
        # 初始化距離和路徑
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        paths = {node: [] for node in graph}
        paths[start] = [start]

        # 優先隊列，存儲 (距離, 節點)
        pq = [(0, start)]
        visited = set()

        while pq:
            dist, node = heapq.heappop(pq)

            # 如果已經找到目標節點，則返回結果
            if end is not None and node == end:
                return {end: (distances[end], paths[end])}

            # 如果節點已訪問過，則跳過
            if node in visited:
                continue

            visited.add(node)

            for neighbor, weight in graph.get(node, []):
                if neighbor in visited:
                    continue

                new_dist = dist + weight

                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    paths[neighbor] = paths[node] + [neighbor]
                    heapq.heappush(pq, (new_dist, neighbor))

        # 返回從 start 到所有節點的最短路徑
        return {
            node: (distances[node], paths[node])
            for node in graph
            if distances[node] != float('inf')
        }

    @staticmethod
    def bellman_ford(
        n: int, edges: List[Tuple[int, int, int]], start: int
    ) -> Tuple[Dict[int, int], Dict[int, List[int]], bool]:
        """
        Bellman-Ford 算法尋找帶權圖中的最短路徑，可處理負權邊

        Args:
            n: 節點數量（節點編號從 0 到 n-1）
            edges: 邊列表，格式為 [(u, v, weight), ...]
            start: 起始節點

        Returns:
            Tuple[Dict[int, int], Dict[int, List[int]], bool]:
            (距離字典, 路徑字典, 是否存在負權環)
        """
        # 初始化距離和路徑
        distances = {i: float('inf') for i in range(n)}
        distances[start] = 0
        paths = {i: [] for i in range(n)}
        paths[start] = [start]

        # 鬆弛操作
        for _ in range(n - 1):
            for u, v, weight in edges:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    paths[v] = paths[u] + [v]

        # 檢測負權環
        has_negative_cycle = False
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                has_negative_cycle = True
                break

        return distances, paths, has_negative_cycle

    @staticmethod
    def floyd_warshall(
        n: int, edges: List[Tuple[int, int, int]]
    ) -> Tuple[List[List[int]], List[List[List[int]]]]:
        """
        Floyd-Warshall 算法計算所有點對最短路徑

        Args:
            n: 節點數量（節點編號從 0 到 n-1）
            edges: 邊列表，格式為 [(u, v, weight), ...]

        Returns:
            Tuple[List[List[int]], List[List[List[int]]]]:
            (距離矩陣, 路徑矩陣)
        """
        # 初始化距離矩陣和路徑矩陣
        INF = float('inf')
        dist = [[INF] * n for _ in range(n)]
        path = [[[] for _ in range(n)] for _ in range(n)]

        # 設置對角線
        for i in range(n):
            dist[i][i] = 0
            path[i][i] = [i]

        # 初始化邊
        for u, v, weight in edges:
            dist[u][v] = weight
            path[u][v] = [u, v]

        # Floyd-Warshall 算法
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if (
                        dist[i][k] != INF
                        and dist[k][j] != INF
                        and dist[i][k] + dist[k][j] < dist[i][j]
                    ):
                        dist[i][j] = dist[i][k] + dist[k][j]
                        path[i][j] = path[i][k][:-1] + path[k][j]

        return dist, path


class GridShortestPath:
    """
    網格圖最短路徑算法
    """

    @staticmethod
    def bfs_grid_shortest_path(
        grid: List[List[int]],
        start: Tuple[int, int],
        end: Tuple[int, int],
        valid_cell: callable = lambda x: x == 0,
    ) -> Tuple[int, List[Tuple[int, int]]]:
        """
        使用 BFS 尋找網格圖中的最短路徑

        Args:
            grid: 二維網格
            start: 起始位置 (row, col)
            end: 目標位置 (row, col)
            valid_cell: 判斷單元格是否可通行的函數

        Returns:
            Tuple[int, List[Tuple[int, int]]]: (最短距離, 最短路徑)，如果不存在路徑則返回 (-1, [])
        """
        if not grid or not grid[0]:
            return -1, []

        rows, cols = len(grid), len(grid[0])

        # 檢查起點和終點是否有效
        if not (0 <= start[0] < rows and 0 <= start[1] < cols) or not valid_cell(
            grid[start[0]][start[1]]
        ):
            return -1, []
        if not (0 <= end[0] < rows and 0 <= end[1] < cols) or not valid_cell(grid[end[0]][end[1]]):
            return -1, []

        if start == end:
            return 0, [start]

        # 四個方向：上、右、下、左
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        visited = set([start])
        queue = deque([(start, 0, [start])])  # (位置, 距離, 路徑)

        while queue:
            (row, col), distance, path = queue.popleft()

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                new_pos = (new_row, new_col)

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and valid_cell(grid[new_row][new_col])
                    and new_pos not in visited
                ):

                    if new_pos == end:
                        return distance + 1, path + [new_pos]

                    visited.add(new_pos)
                    queue.append((new_pos, distance + 1, path + [new_pos]))

        return -1, []  # 不存在路徑

    @staticmethod
    def a_star_grid_shortest_path(
        grid: List[List[int]],
        start: Tuple[int, int],
        end: Tuple[int, int],
        valid_cell: callable = lambda x: x == 0,
    ) -> Tuple[int, List[Tuple[int, int]]]:
        """
        使用 A* 算法尋找網格圖中的最短路徑

        Args:
            grid: 二維網格
            start: 起始位置 (row, col)
            end: 目標位置 (row, col)
            valid_cell: 判斷單元格是否可通行的函數

        Returns:
            Tuple[int, List[Tuple[int, int]]]: (最短距離, 最短路徑)，如果不存在路徑則返回 (-1, [])
        """
        if not grid or not grid[0]:
            return -1, []

        rows, cols = len(grid), len(grid[0])

        # 檢查起點和終點是否有效
        if not (0 <= start[0] < rows and 0 <= start[1] < cols) or not valid_cell(
            grid[start[0]][start[1]]
        ):
            return -1, []
        if not (0 <= end[0] < rows and 0 <= end[1] < cols) or not valid_cell(grid[end[0]][end[1]]):
            return -1, []

        if start == end:
            return 0, [start]

        # 曼哈頓距離啟發函數
        def heuristic(pos):
            return abs(pos[0] - end[0]) + abs(pos[1] - end[1])

        # 四個方向：上、右、下、左
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # 開放列表和關閉列表
        open_set = []
        closed_set = set()

        # g_score[pos] 表示從起點到 pos 的實際距離
        g_score = {start: 0}

        # f_score[pos] = g_score[pos] + heuristic(pos)
        f_score = {start: heuristic(start)}

        # 路徑追踪
        came_from = {}

        # 將起點加入開放列表
        heapq.heappush(open_set, (f_score[start], start))

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == end:
                # 重建路徑
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                path.reverse()
                return g_score[end], path

            closed_set.add(current)

            for dr, dc in directions:
                row, col = current
                new_row, new_col = row + dr, col + dc
                neighbor = (new_row, new_col)

                if not (0 <= new_row < rows and 0 <= new_col < cols) or not valid_cell(
                    grid[new_row][new_col]
                ):
                    continue

                if neighbor in closed_set:
                    continue

                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor)

                    if neighbor not in [item[1] for item in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return -1, []  # 不存在路徑


def example_usage():
    """
    示範如何使用最短路徑算法模板
    """
    print("===== BFS 最短路徑示範 =====")

    # 創建無權圖
    unweighted_graph = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1], 4: [1, 5], 5: [2, 4]}

    # 使用 BFS 尋找最短路徑
    distance, path = ShortestPath.bfs_shortest_path(unweighted_graph, 0, 5)
    print(f"從節點 0 到節點 5 的最短距離: {distance}")
    print(f"從節點 0 到節點 5 的最短路徑: {path}")

    print("\n===== Dijkstra 算法示範 =====")

    # 創建帶權圖
    weighted_graph = {
        0: [(1, 4), (2, 2)],
        1: [(0, 4), (3, 5), (4, 1)],
        2: [(0, 2), (5, 3)],
        3: [(1, 5)],
        4: [(1, 1), (5, 6)],
        5: [(2, 3), (4, 6)],
    }

    # 使用 Dijkstra 算法尋找最短路徑
    result = ShortestPath.dijkstra(weighted_graph, 0, 5)
    distance, path = result[5]
    print(f"從節點 0 到節點 5 的最短距離: {distance}")
    print(f"從節點 0 到節點 5 的最短路徑: {path}")

    print("\n===== Bellman-Ford 算法示範 =====")

    # 創建邊列表
    edges = [(0, 1, 4), (0, 2, 2), (1, 3, 5), (1, 4, 1), (2, 5, 3), (4, 5, 6)]

    # 使用 Bellman-Ford 算法尋找最短路徑
    distances, paths, has_negative_cycle = ShortestPath.bellman_ford(6, edges, 0)
    print(f"從節點 0 到所有節點的最短距離: {distances}")
    print(f"從節點 0 到節點 5 的最短路徑: {paths[5]}")
    print(f"是否存在負權環: {has_negative_cycle}")

    print("\n===== Floyd-Warshall 算法示範 =====")

    # 使用 Floyd-Warshall 算法計算所有點對最短路徑
    dist_matrix, path_matrix = ShortestPath.floyd_warshall(6, edges)
    print(f"節點 0 到節點 5 的最短距離: {dist_matrix[0][5]}")
    print(f"節點 0 到節點 5 的最短路徑: {path_matrix[0][5]}")

    print("\n===== 網格最短路徑示範 =====")

    # 創建網格
    grid = [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]

    # 使用 BFS 尋找網格中的最短路徑
    start, end = (0, 0), (4, 4)
    distance, path = GridShortestPath.bfs_grid_shortest_path(grid, start, end)
    print(f"網格中從 {start} 到 {end} 的最短距離: {distance}")
    print(f"網格中從 {start} 到 {end} 的最短路徑: {path}")

    # 使用 A* 算法尋找網格中的最短路徑
    distance, path = GridShortestPath.a_star_grid_shortest_path(grid, start, end)
    print(f"使用 A* 算法，網格中從 {start} 到 {end} 的最短距離: {distance}")
    print(f"使用 A* 算法，網格中從 {start} 到 {end} 的最短路徑: {path}")


if __name__ == "__main__":
    example_usage()
