# Graph 圖論解題技巧與 LeetCode 學習清單

## 基本解題技巧

### 1. 圖的表示方法 (Graph Representation)

- 使用時機：
  - 需要表示節點間的關係
  - 需要處理有向或無向圖
  - 需要處理加權圖
- 實作重點：
  - 鄰接矩陣（Adjacency Matrix）
  - 鄰接列表（Adjacency List）
  - 邊列表（Edge List）
  - 選擇合適的表示方法考慮空間效率

### 2. 圖的遍歷 (Graph Traversal)

- 使用時機：
  - 需要訪問圖中所有節點
  - 需要找出特定路徑
  - 需要檢查連通性
- 實作重點：
  - 深度優先搜索（DFS）
  - 廣度優先搜索（BFS）
  - 訪問標記的管理
  - 處理環和重複訪問

### 3. 最短路徑 (Shortest Path)

- 使用時機：
  - 需要找出兩點間最短距離
  - 需要計算最小成本路徑
  - 需要處理加權圖的路徑問題
- 實作重點：
  - Dijkstra 算法
  - Floyd-Warshall 算法
  - Bellman-Ford 算法
  - 選擇合適的算法根據圖的特性

### 4. 拓撲排序 (Topological Sort)

- 使用時機：
  - 需要處理依賴關係
  - 需要安排任務順序
  - 需要檢測環的存在
- 實作重點：
  - 入度計算
  - 環的檢測
  - 排序結果的生成
  - BFS 或 DFS 的選擇

### 5. 並查集 (Union Find)

- 使用時機：
  - 需要處理圖的連通性
  - 需要合併集合
  - 需要檢測環
- 實作重點：
  - 路徑壓縮
  - 按秩合併
  - 集合的維護
  - 效率優化

## 練習題目

### 1. 圖的遍歷練習（由易到難）

1. [733. Flood Fill](https://leetcode.com/problems/flood-fill/) (Easy)

   - 核心技巧：DFS/BFS 基礎應用
   - 時間複雜度：O(n×m)
   - 空間複雜度：O(n×m)
   - 學習重點：
     - 基本的 DFS/BFS 實現
     - 格子圖的遍歷
     - 訪問標記的處理

2. [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) (Medium)

   - 核心技巧：連通分量計數
   - 時間複雜度：O(n×m)
   - 空間複雜度：O(n×m)
   - 學習重點：
     - DFS/BFS 的應用
     - 連通分量的識別
     - 訪問標記的優化

3. [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/) (Medium)

   - 核心技巧：圖的連通性
   - 時間複雜度：O(n²)
   - 空間複雜度：O(n)
   - 學習重點：
     - 鄰接矩陣的處理
     - DFS/BFS vs 並查集
     - 不同解法的比較

4. [797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/) (Medium)
   - 核心技巧：路徑搜索
   - 時間複雜度：O(2^n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 路徑記錄
     - 回溯處理
     - 有向無環圖特性

### 2. 最短路徑練習（由易到難）

1. [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) (Medium)

   - 核心技巧：BFS 最短路徑
   - 時間複雜度：O(n×m)
   - 空間複雜度：O(n×m)
   - 學習重點：
     - BFS 層次遍歷
     - 距離計算
     - 多方向移動處理

2. [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) (Medium)

   - 核心技巧：Dijkstra 算法
   - 時間複雜度：O(E log V)
   - 空間複雜度：O(V + E)
   - 學習重點：
     - Dijkstra 實現
     - 優先隊列使用
     - 加權圖處理

3. [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) (Medium)
   - 核心技巧：修改版 Bellman-Ford
   - 時間複雜度：O(K×E)
   - 空間複雜度：O(V)
   - 學習重點：
     - 限制條件下的最短路
     - 動態規劃思想
     - 狀態轉移設計

### 3. 拓撲排序練習

1. [207. Course Schedule](https://leetcode.com/problems/course-schedule/) (Medium)

   - 核心技巧：環檢測
   - 時間複雜度：O(V + E)
   - 空間複雜度：O(V + E)
   - 學習重點：
     - 圖中環的檢測
     - DFS/BFS 實現選擇
     - 狀態標記技巧

2. [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) (Medium)
   - 核心技巧：拓撲排序實現
   - 時間複雜度：O(V + E)
   - 空間複雜度：O(V + E)
   - 學習重點：
     - 完整拓撲序列生成
     - 入度統計與更新
     - 隊列使用技巧

### 4. 並查集練習

1. [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) (Medium)

   - 核心技巧：基礎並查集
   - 時間複雜度：O(N×α(N))
   - 空間複雜度：O(N)
   - 學習重點：
     - 並查集基本操作
     - 環的檢測
     - 路徑壓縮實現

2. [1319. Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) (Medium)
   - 核心技巧：連通分量計數
   - 時間複雜度：O(N×α(N))
   - 空間複雜度：O(N)
   - 學習重點：
     - 並查集的應用
     - 連通性判斷
     - 冗餘連接計數

## Python 解題模板

### 1. 圖的表示模板

```python
# 鄰接列表
def create_adj_list(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # 無向圖需要這行
    return graph

# 鄰接矩陣
def create_adj_matrix(n, edges):
    matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1  # 無向圖需要這行
    return matrix
```

### 2. DFS 模板

```python
# 遞迴 DFS
def dfs(graph, node, visited):
    if node in visited:
        return
    visited.add(node)
    for next_node in graph[node]:
        dfs(graph, next_node, visited)

# 迭代 DFS
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for next_node in graph[node]:
                if next_node not in visited:
                    stack.append(next_node)
```

### 3. BFS 模板

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
```

### 4. Dijkstra 模板

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances
```

### 5. 並查集模板

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True
```

## 學習建議

### 1. 學習順序

1. 第一週：圖的基本表示和遍歷 (733, 200)
2. 第二週：DFS 和 BFS 的應用 (547, 797)
3. 第三週：最短路徑算法 (1091, 743)
4. 第四週：拓撲排序應用 (207, 210)
5. 第五週：並查集和進階應用 (684, 1319)

### 2. 學習方法

1. 先熟悉圖的基本概念和表示方法
2. 從簡單的 DFS/BFS 題目開始
3. 理解並實作各種圖算法的基本模板
4. 練習識別問題與算法的對應關係

### 3. 進階建議

1. 注意不同表示方法的優缺點
2. 關注空間和時間複雜度的優化
3. 練習處理特殊情況和邊界條件
4. 嘗試結合多種圖算法解決複雜問題
