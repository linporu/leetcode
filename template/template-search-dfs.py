from collections import defaultdict
from typing import Any, List, Optional


class TreeNode:
    """二元樹節點的基本結構"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Graph:
    """使用鄰接表實現的圖結構"""

    def __init__(self):
        # 使用 defaultdict 來建立鄰接表
        self.adj_list = defaultdict(list)

    def add_edge(self, u: Any, v: Any) -> None:
        """新增一條無向邊從 u 到 v

        Args:
            u: 起始頂點
            v: 終止頂點
        """
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # 如果是無向圖的話


def dfs_tree_recursive(root: Optional[TreeNode]) -> List[int]:
    """遞迴方式實現二元樹的 DFS（前序遍歷）

    時間複雜度: O(n), 其中 n 是節點數量
    空間複雜度: O(h), 其中 h 是樹高，最壞情況 O(n)

    Args:
        root: 二元樹的根節點

    Returns:
        包含遍歷順序的節點值列表
    """
    result = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            return

        # 前序遍歷 (Pre-order): 根 -> 左 -> 右
        result.append(node.val)  # 訪問節點
        dfs(node.left)  # 遞迴左子樹
        dfs(node.right)  # 遞迴右子樹

    dfs(root)
    return result


def dfs_tree_iterative(root: Optional[TreeNode]) -> List[int]:
    """迭代方式實現二元樹的 DFS（前序遍歷）

    時間複雜度: O(n), 其中 n 是節點數量
    空間複雜度: O(h), 其中 h 是樹高，最壞情況 O(n)

    Args:
        root: 二元樹的根節點

    Returns:
        包含遍歷順序的節點值列表
    """
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # 注意：因為使用 stack，所以要先將右子節點壓入堆疊
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def dfs_graph_recursive(graph: Graph, start: Any) -> List[Any]:
    """遞迴方式實現圖的 DFS

    時間複雜度: O(V + E), 其中 V 是頂點數，E 是邊數
    空間複雜度: O(V), 用於 visited 集合和遞迴調用棧

    Args:
        graph: 圖物件
        start: 起始頂點

    Returns:
        包含遍歷順序的頂點列表
    """
    visited = set()
    result = []

    def dfs(vertex: Any) -> None:
        visited.add(vertex)
        result.append(vertex)

        for neighbor in graph.adj_list[vertex]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return result


def dfs_graph_iterative(graph: Graph, start: Any) -> List[Any]:
    """迭代方式實現圖的 DFS

    時間複雜度: O(V + E), 其中 V 是頂點數，E 是邊數
    空間複雜度: O(V), 用於 visited 集合和堆疊

    Args:
        graph: 圖物件
        start: 起始頂點

    Returns:
        包含遍歷順序的頂點列表
    """
    visited = set()
    result = []
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)

            # 將所有未訪問的相鄰節點加入堆疊
            for neighbor in reversed(graph.adj_list[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


def test_tree_dfs():
    """測試二元樹的 DFS 實作"""
    # 建立測試用的二元樹
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Tree DFS Recursive:", dfs_tree_recursive(root))  # 預期: [1, 2, 4, 5, 3]
    print("Tree DFS Iterative:", dfs_tree_iterative(root))  # 預期: [1, 2, 4, 5, 3]


def test_graph_dfs():
    """測試圖的 DFS 實作"""
    # 建立測試用的圖
    # 0 -- 1 -- 2 -- 3 -- 4
    graph = Graph()
    edges = [(0, 1), (1, 2), (2, 3), (3, 4)]
    for u, v in edges:
        graph.add_edge(u, v)

    print("Graph DFS Recursive:", dfs_graph_recursive(graph, 0))  # 預期: [0, 1, 2, 3, 4]
    print("Graph DFS Iterative:", dfs_graph_iterative(graph, 0))  # 預期: [0, 1, 2, 3, 4]


if __name__ == "__main__":
    test_tree_dfs()
    test_graph_dfs()
