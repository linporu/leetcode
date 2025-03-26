"""
圖論拓撲排序模板 (Graph Topological Sort Template)

本模板包含：
1. 基於 BFS 的拓撲排序（Kahn 算法）
2. 基於 DFS 的拓撲排序
3. 環檢測

適用於：
- 需要處理依賴關係
- 需要安排任務順序
- 需要檢測環的存在

實作重點：
- 入度計算
- 環的檢測
- 排序結果的生成
- BFS 或 DFS 的選擇
"""

from typing import List, Dict, Set, Tuple, Optional
from collections import defaultdict, deque


class TopologicalSort:
    """
    拓撲排序算法
    """
    
    @staticmethod
    def kahn_algorithm(n: int, edges: List[List[int]]) -> Tuple[List[int], bool]:
        """
        基於 BFS 的拓撲排序（Kahn 算法）

        Args:
            n: 節點數量（節點編號從 0 到 n-1）
            edges: 邊列表，格式為 [[u, v], ...]，表示從 u 到 v 的有向邊

        Returns:
            Tuple[List[int], bool]: (拓撲排序結果, 是否存在有效的拓撲排序)
            如果存在環，則無法進行拓撲排序，返回 ([], False)
        """
        # 構建鄰接列表和計算入度
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # 將所有入度為 0 的節點加入隊列
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        # 拓撲排序結果
        topo_order = []
        
        # BFS
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 檢查是否存在環
        if len(topo_order) != n:
            return [], False
        
        return topo_order, True
    
    @staticmethod
    def dfs_topological_sort(n: int, edges: List[List[int]]) -> Tuple[List[int], bool]:
        """
        基於 DFS 的拓撲排序

        Args:
            n: 節點數量（節點編號從 0 到 n-1）
            edges: 邊列表，格式為 [[u, v], ...]，表示從 u 到 v 的有向邊

        Returns:
            Tuple[List[int], bool]: (拓撲排序結果, 是否存在有效的拓撲排序)
            如果存在環，則無法進行拓撲排序，返回 ([], False)
        """
        # 構建鄰接列表
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        # 訪問狀態：0 = 未訪問，1 = 正在訪問，2 = 已訪問
        visited = [0] * n
        topo_order = []
        has_cycle = [False]  # 使用列表以便在遞迴中修改
        
        def dfs(node):
            if visited[node] == 1:  # 檢測到環
                has_cycle[0] = True
                return
            if visited[node] == 2:  # 已訪問過，跳過
                return
            
            visited[node] = 1  # 標記為正在訪問
            
            for neighbor in graph[node]:
                dfs(neighbor)
                if has_cycle[0]:
                    return
            
            visited[node] = 2  # 標記為已訪問
            topo_order.append(node)
        
        # 對每個未訪問的節點進行 DFS
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                if has_cycle[0]:
                    return [], False
        
        # DFS 產生的順序是反向的，需要翻轉
        topo_order.reverse()
        
        return topo_order, True
    
    @staticmethod
    def all_topological_sorts(n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        生成所有可能的拓撲排序結果

        Args:
            n: 節點數量（節點編號從 0 到 n-1）
            edges: 邊列表，格式為 [[u, v], ...]，表示從 u 到 v 的有向邊

        Returns:
            List[List[int]]: 所有可能的拓撲排序結果列表
        """
        # 構建鄰接列表和計算入度
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # 存儲所有可能的拓撲排序
        all_topo_sorts = []
        
        def backtrack(current_path, in_degree_copy):
            # 如果當前路徑包含所有節點，則找到一個有效的拓撲排序
            if len(current_path) == n:
                all_topo_sorts.append(current_path.copy())
                return
            
            for i in range(n):
                # 如果入度為 0 且未訪問過
                if in_degree_copy[i] == 0 and i not in current_path:
                    # 將節點加入當前路徑
                    current_path.append(i)
                    
                    # 減少相鄰節點的入度
                    for neighbor in graph[i]:
                        in_degree_copy[neighbor] -= 1
                    
                    # 遞迴
                    backtrack(current_path, in_degree_copy)
                    
                    # 回溯
                    current_path.pop()
                    for neighbor in graph[i]:
                        in_degree_copy[neighbor] += 1
        
        backtrack([], in_degree.copy())
        
        return all_topo_sorts


class CycleDetection:
    """
    環檢測算法
    """
    
    @staticmethod
    def has_cycle_directed_dfs(n: int, edges: List[List[int]]) -> Tuple[bool, List[int]]:
        """
        使用 DFS 檢測有向圖中是否存在環

        Args:
            n: 節點數量（節點編號從 0 到 n-1）
            edges: 邊列表，格式為 [[u, v], ...]，表示從 u 到 v 的有向邊

        Returns:
            Tuple[bool, List[int]]: (是否存在環, 環中的節點列表)
        """
        # 構建鄰接列表
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        # 訪問狀態：0 = 未訪問，1 = 正在訪問，2 = 已訪問
        visited = [0] * n
        cycle = []
        
        def dfs(node, path):
            if visited[node] == 1:  # 檢測到環
                # 找到環的起點
                cycle_start = path.index(node)
                cycle.extend(path[cycle_start:])
                return True
            if visited[node] == 2:  # 已訪問過，跳過
                return False
            
            visited[node] = 1  # 標記為正在訪問
            path.append(node)
            
            for neighbor in graph[node]:
                if dfs(neighbor, path):
                    return True
            
            visited[node] = 2  # 標記為已訪問
            path.pop()
            
            return False
        
        # 對每個未訪問的節點進行 DFS
        for i in range(n):
            if visited[i] == 0:
                if dfs(i, []):
                    return True, cycle
        
        return False, []
    
    @staticmethod
    def has_cycle_undirected_dfs(n: int, edges: List[List[int]]) -> Tuple[bool, List[int]]:
        """
        使用 DFS 檢測無向圖中是否存在環

        Args:
            n: 節點數量（節點編號從 0 到 n-1）
            edges: 邊列表，格式為 [[u, v], ...]，表示 u 和 v 之間的無向邊

        Returns:
            Tuple[bool, List[int]]: (是否存在環, 環中的節點列表)
        """
        # 構建鄰接列表
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        cycle = []
        
        def dfs(node, parent, path):
            visited[node] = True
            path.append(node)
            
            for neighbor in graph[node]:
                if neighbor == parent:  # 跳過父節點
                    continue
                
                if visited[neighbor]:  # 檢測到環
                    # 找到環的起點
                    cycle_start = path.index(neighbor)
                    cycle.extend(path[cycle_start:])
                    return True
                
                if dfs(neighbor, node, path):
                    return True
            
            path.pop()
            return False
        
        # 對每個未訪問的節點進行 DFS
        for i in range(n):
            if not visited[i]:
                if dfs(i, -1, []):
                    return True, cycle
        
        return False, []


class DependencyResolver:
    """
    依賴關係解析
    """
    
    @staticmethod
    def resolve_dependencies(tasks: List[str], dependencies: List[Tuple[str, str]]) -> Tuple[List[str], bool]:
        """
        解析任務依賴關係，生成任務執行順序

        Args:
            tasks: 任務列表
            dependencies: 依賴關係列表，格式為 [(a, b), ...]，表示任務 a 依賴於任務 b（b 必須在 a 之前完成）

        Returns:
            Tuple[List[str], bool]: (任務執行順序, 是否可以解析所有依賴)
        """
        # 構建任務索引映射
        task_to_idx = {task: i for i, task in enumerate(tasks)}
        idx_to_task = {i: task for i, task in enumerate(tasks)}
        
        # 轉換依賴關係為邊列表
        edges = []
        for a, b in dependencies:
            edges.append([task_to_idx[b], task_to_idx[a]])  # b -> a 表示 a 依賴於 b
        
        # 使用拓撲排序解析依賴
        topo_order, is_valid = TopologicalSort.kahn_algorithm(len(tasks), edges)
        
        if not is_valid:
            return [], False
        
        # 將索引轉換回任務名稱
        result = [idx_to_task[idx] for idx in topo_order]
        
        return result, True


def example_usage():
    """
    示範如何使用拓撲排序模板
    """
    print("===== 拓撲排序示範 =====")
    
    # 創建有向無環圖
    n = 6
    edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 4], [3, 5], [4, 5]]
    
    # 使用 Kahn 算法進行拓撲排序
    topo_order, is_valid = TopologicalSort.kahn_algorithm(n, edges)
    print(f"Kahn 算法拓撲排序結果: {topo_order}")
    print(f"是否存在有效的拓撲排序: {is_valid}")
    
    # 使用 DFS 進行拓撲排序
    topo_order, is_valid = TopologicalSort.dfs_topological_sort(n, edges)
    print(f"DFS 拓撲排序結果: {topo_order}")
    print(f"是否存在有效的拓撲排序: {is_valid}")
    
    print("\n===== 環檢測示範 =====")
    
    # 創建有環的有向圖
    n = 4
    edges_with_cycle = [[0, 1], [1, 2], [2, 3], [3, 1]]
    
    # 檢測有向圖中的環
    has_cycle, cycle = CycleDetection.has_cycle_directed_dfs(n, edges_with_cycle)
    print(f"有向圖是否存在環: {has_cycle}")
    print(f"環中的節點: {cycle}")
    
    # 創建有環的無向圖
    n = 5
    undirected_edges_with_cycle = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 1]]
    
    # 檢測無向圖中的環
    has_cycle, cycle = CycleDetection.has_cycle_undirected_dfs(n, undirected_edges_with_cycle)
    print(f"無向圖是否存在環: {has_cycle}")
    print(f"環中的節點: {cycle}")
    
    print("\n===== 依賴關係解析示範 =====")
    
    # 創建任務和依賴關係
    tasks = ["編譯", "測試", "部署", "文檔", "設計", "開發"]
    dependencies = [
        ("測試", "編譯"),  # 測試依賴於編譯
        ("部署", "測試"),  # 部署依賴於測試
        ("開發", "設計"),  # 開發依賴於設計
        ("編譯", "開發"),  # 編譯依賴於開發
        ("文檔", "設計")   # 文檔依賴於設計
    ]
    
    # 解析依賴關係
    execution_order, is_resolvable = DependencyResolver.resolve_dependencies(tasks, dependencies)
    print(f"任務執行順序: {execution_order}")
    print(f"是否可以解析所有依賴: {is_resolvable}")


if __name__ == "__main__":
    example_usage()
