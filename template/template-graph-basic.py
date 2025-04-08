"""
圖論基礎模板 (Graph Basics Template)

本模板包含：
1. 圖的表示方法（鄰接矩陣、鄰接列表、邊列表）
2. 圖的基本遍歷算法（DFS、BFS）
3. 連通性檢測

適用於：
- 需要表示節點間的關係
- 需要遍歷圖中所有節點
- 需要找出特定路徑
- 需要檢查連通性
"""

from typing import List, Dict, Tuple, Any
from collections import defaultdict, deque


class GraphRepresentation:
    """
    圖的表示方法
    """

    @staticmethod
    def create_adjacency_matrix(
        n: int, edges: List[List[int]], directed: bool = False
    ) -> List[List[int]]:
        """
        創建鄰接矩陣

        Args:
            n: 節點數量（節點編號從 0 到 n-1）
            edges: 邊的列表，每個邊為 [u, v] 或 [u, v, weight]
            directed: 是否為有向圖

        Returns:
            List[List[int]]: 鄰接矩陣
        """
        # 初始化鄰接矩陣
        matrix = [[0] * n for _ in range(n)]

        for edge in edges:
            u, v = edge[0], edge[1]
            weight = edge[2] if len(edge) > 2 else 1

            matrix[u][v] = weight
            if not directed:  # 如果是無向圖，則雙向添加
                matrix[v][u] = weight

        return matrix

    @staticmethod
    def create_adjacency_list(
        n: int, edges: List[List[int]], directed: bool = False
    ) -> Dict[int, List[Tuple[int, int]]]:
        """
        創建鄰接列表

        Args:
            n: 節點數量（節點編號從 0 到 n-1）
            edges: 邊的列表，每個邊為 [u, v] 或 [u, v, weight]
            directed: 是否為有向圖

        Returns:
            Dict[int, List[Tuple[int, int]]]: 鄰接列表，格式為 {node: [(neighbor, weight), ...]}
        """
        # 初始化鄰接列表
        adj_list = defaultdict(list)

        for edge in edges:
            u, v = edge[0], edge[1]
            weight = edge[2] if len(edge) > 2 else 1

            adj_list[u].append((v, weight))
            if not directed:  # 如果是無向圖，則雙向添加
                adj_list[v].append((u, weight))

        return adj_list

    @staticmethod
    def create_edge_list(edges: List[List[int]]) -> List[Tuple[int, int, int]]:
        """
        創建邊列表

        Args:
            edges: 邊的列表，每個邊為 [u, v] 或 [u, v, weight]

        Returns:
            List[Tuple[int, int, int]]: 標準化的邊列表，格式為 [(u, v, weight), ...]
        """
        edge_list = []

        for edge in edges:
            u, v = edge[0], edge[1]
            weight = edge[2] if len(edge) > 2 else 1
            edge_list.append((u, v, weight))

        return edge_list


class GraphTraversal:
    """
    圖的遍歷算法
    """

    @staticmethod
    def dfs_recursive(graph: Dict[int, List[int]], start: int) -> List[int]:
        """
        深度優先搜索（遞迴實現）

        Args:
            graph: 鄰接列表表示的圖，格式為 {node: [neighbors]}
            start: 起始節點

        Returns:
            List[int]: 遍歷順序
        """
        visited = set()
        result = []

        def dfs(node: int):
            if node in visited:
                return

            visited.add(node)
            result.append(node)

            for neighbor in graph[node]:
                if isinstance(neighbor, tuple):  # 處理帶權重的情況
                    next_node = neighbor[0]
                else:
                    next_node = neighbor

                if next_node not in visited:
                    dfs(next_node)

        dfs(start)
        return result

    @staticmethod
    def dfs_iterative(graph: Dict[int, List[Any]], start: int) -> List[int]:
        """
        深度優先搜索（迭代實現）

        Args:
            graph: 鄰接列表表示的圖，格式為 {node: [neighbors]} 或 {node: [(neighbor, weight), ...]}
            start: 起始節點

        Returns:
            List[int]: 遍歷順序
        """
        if not graph:
            return []

        visited = set()
        result = []
        stack = [start]

        while stack:
            node = stack.pop()

            if node in visited:
                continue

            visited.add(node)
            result.append(node)

            # 將鄰居節點按照逆序加入棧中，以保持與遞迴 DFS 相同的遍歷順序
            neighbors = []
            for neighbor in graph[node]:
                if isinstance(neighbor, tuple):  # 處理帶權重的情況
                    next_node = neighbor[0]
                else:
                    next_node = neighbor
                neighbors.append(next_node)

            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)

        return result

    @staticmethod
    def bfs(graph: Dict[int, List[Any]], start: int) -> List[int]:
        """
        廣度優先搜索

        Args:
            graph: 鄰接列表表示的圖，格式為 {node: [neighbors]} 或 {node: [(neighbor, weight), ...]}
            start: 起始節點

        Returns:
            List[int]: 遍歷順序
        """
        if not graph:
            return []

        visited = set([start])
        result = [start]
        queue = deque([start])

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                if isinstance(neighbor, tuple):  # 處理帶權重的情況
                    next_node = neighbor[0]
                else:
                    next_node = neighbor

                if next_node not in visited:
                    visited.add(next_node)
                    result.append(next_node)
                    queue.append(next_node)

        return result


class ConnectivityChecker:
    """
    圖的連通性檢測
    """

    @staticmethod
    def is_path_exists(graph: Dict[int, List[Any]], source: int, destination: int) -> bool:
        """
        檢查兩點間是否存在路徑

        Args:
            graph: 鄰接列表表示的圖
            source: 起始節點
            destination: 目標節點

        Returns:
            bool: 是否存在路徑
        """
        if source == destination:
            return True

        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                if isinstance(neighbor, tuple):  # 處理帶權重的情況
                    next_node = neighbor[0]
                else:
                    next_node = neighbor

                if next_node == destination:
                    return True

                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(next_node)

        return False

    @staticmethod
    def count_connected_components(n: int, graph: Dict[int, List[Any]]) -> int:
        """
        計算無向圖中的連通分量數量

        Args:
            n: 節點數量（節點編號從 0 到 n-1）
            graph: 鄰接列表表示的圖

        Returns:
            int: 連通分量數量
        """
        visited = set()
        count = 0

        def dfs(node: int):
            visited.add(node)

            for neighbor in graph.get(node, []):
                if isinstance(neighbor, tuple):  # 處理帶權重的情況
                    next_node = neighbor[0]
                else:
                    next_node = neighbor

                if next_node not in visited:
                    dfs(next_node)

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count


def example_usage():
    """
    示範如何使用圖論基礎模板
    """
    print("===== 圖的表示方法示範 =====")

    # 創建測試數據
    n = 5  # 節點數量
    edges = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 4]]  # 邊列表

    # 創建鄰接矩陣
    adj_matrix = GraphRepresentation.create_adjacency_matrix(n, edges)
    print("鄰接矩陣:")
    for row in adj_matrix:
        print(row)

    # 創建鄰接列表
    adj_list = GraphRepresentation.create_adjacency_list(n, edges)
    print("\n鄰接列表:")
    for node, neighbors in adj_list.items():
        print(f"{node}: {neighbors}")

    print("\n===== 圖的遍歷示範 =====")

    # 遞迴 DFS
    dfs_result = GraphTraversal.dfs_recursive(adj_list, 0)
    print(f"遞迴 DFS 遍歷順序: {dfs_result}")

    # 迭代 DFS
    dfs_iter_result = GraphTraversal.dfs_iterative(adj_list, 0)
    print(f"迭代 DFS 遍歷順序: {dfs_iter_result}")

    # BFS
    bfs_result = GraphTraversal.bfs(adj_list, 0)
    print(f"BFS 遍歷順序: {bfs_result}")

    print("\n===== 連通性檢測示範 =====")

    # 檢查路徑存在性
    path_exists = ConnectivityChecker.is_path_exists(adj_list, 0, 4)
    print(f"節點 0 到節點 4 是否存在路徑: {path_exists}")

    # 計算連通分量
    components_count = ConnectivityChecker.count_connected_components(n, adj_list)
    print(f"連通分量數量: {components_count}")


if __name__ == "__main__":
    example_usage()
