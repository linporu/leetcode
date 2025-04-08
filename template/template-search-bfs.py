from collections import deque
from typing import Any, Dict, List, Optional, Set


class TreeNode:
    """二元樹節點的基本結構"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Graph:
    """圖的基本結構"""

    def __init__(self):
        self.graph: Dict[Any, List[Any]] = {}

    def add_edge(self, u: Any, v: Any) -> None:
        """新增一條邊從 u 到 v"""
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)


def bfs_iterative_tree(root: Optional[TreeNode]) -> List[int]:
    """
    迭代方式實現二元樹的 BFS
    時間複雜度: O(n), 其中 n 是節點數量
    空間複雜度: O(w), 其中 w 是樹的最大寬度
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        # 取得當前層級的節點數量
        level_size = len(queue)

        # 處理當前層級的所有節點
        for _ in range(level_size):
            node = queue.popleft()
            result.append(node.val)

            # 將子節點加入佇列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


def bfs_recursive_tree(root: Optional[TreeNode]) -> List[int]:
    """
    遞迴方式實現二元樹的 BFS
    時間複雜度: O(n), 其中 n 是節點數量
    空間複雜度: O(w), 其中 w 是樹的最大寬度
    """
    result = []

    def bfs_level(nodes: List[TreeNode]) -> None:
        if not nodes:
            return

        next_level = []
        for node in nodes:
            result.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        bfs_level(next_level)

    if root:
        bfs_level([root])
    return result


def bfs_iterative_graph(graph: Graph, start: Any) -> List[Any]:
    """
    迭代方式實現圖的 BFS
    時間複雜度: O(V + E), 其中 V 是頂點數，E 是邊數
    空間複雜度: O(V)
    """
    if start not in graph.graph:
        return []

    result = []
    visited = set([start])
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        # 訪問所有相鄰節點
        for neighbor in graph.graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def bfs_recursive_graph(graph: Graph, start: Any) -> List[Any]:
    """
    遞迴方式實現圖的 BFS
    時間複雜度: O(V + E), 其中 V 是頂點數，E 是邊數
    空間複雜度: O(V)
    """
    result = []
    visited = set()

    def bfs_level(queue: deque, visited: Set[Any]) -> None:
        if not queue:
            return

        # 處理當前層級的所有節點
        vertex = queue.popleft()
        result.append(vertex)

        # 訪問所有相鄰節點
        for neighbor in graph.graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

        bfs_level(queue, visited)

    if start in graph.graph:
        visited.add(start)
        queue = deque([start])
        bfs_level(queue, visited)

    return result


# 測試程式碼
def test_tree_bfs():
    """測試二元樹的 BFS 實作"""
    # 建立測試用的二元樹
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print("Tree BFS Iterative:", bfs_iterative_tree(root))  # 預期: [1, 2, 3, 4, 5, 6]
    print("Tree BFS Recursive:", bfs_recursive_tree(root))  # 預期: [1, 2, 3, 4, 5, 6]


def test_graph_bfs():
    """測試圖的 BFS 實作"""
    # 建立測試用的圖
    # 1 -> 2 -> 3
    # |    |
    # v    v
    # 4 -> 5
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(2, 5)
    graph.add_edge(4, 5)

    print("Graph BFS Iterative:", bfs_iterative_graph(graph, 1))  # 預期: [1, 2, 4, 3, 5]
    print("Graph BFS Recursive:", bfs_recursive_graph(graph, 1))  # 預期: [1, 2, 4, 3, 5]


if __name__ == "__main__":
    test_tree_bfs()
    test_graph_bfs()
