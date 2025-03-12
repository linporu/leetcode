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

#### Easy 題目

1. [733. Flood Fill](https://leetcode.com/problems/flood-fill/) (Easy)

   - 核心技巧：DFS/BFS 基礎應用
   - 時間複雜度：O(n×m)
   - 空間複雜度：O(n×m)
   - 學習重點：
     - 基本的 DFS/BFS 實現
     - 格子圖的遍歷
     - 訪問標記的處理

2. [1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) (Easy)

   - 核心技巧：基本圖遍歷
   - 時間複雜度：O(V+E)
   - 空間複雜度：O(V)
   - 學習重點：
     - 圖的連通性判斷
     - DFS/BFS 的選擇
     - 基本圖結構操作

3. [463. Island Perimeter](https://leetcode.com/problems/island-perimeter/) (Easy)
   - 核心技巧：網格遍歷
   - 時間複雜度：O(n×m)
   - 空間複雜度：O(1)
   - 學習重點：
     - 邊界判斷
     - 相鄰關係處理
     - 網格特性應用

#### Medium 題目

1. [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) (Medium)

   - 核心技巧：連通分量計數
   - 時間複雜度：O(n×m)
   - 空間複雜度：O(n×m)
   - 學習重點：
     - DFS/BFS 的應用
     - 連通分量的識別
     - 訪問標記的優化

2. [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/) (Medium)

   - 核心技巧：圖的連通性
   - 時間複雜度：O(n²)
   - 空間複雜度：O(n)
   - 學習重點：
     - 鄰接矩陣的處理
     - DFS/BFS vs 並查集
     - 不同解法的比較

3. [797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/) (Medium)
   - 核心技巧：路徑搜索
   - 時間複雜度：O(2^n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 路徑記錄
     - 回溯處理
     - 有向無環圖特性

### 2. 最短路徑練習（由易到難）

#### Easy 題目

1. [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) (Easy)

   - 核心技巧：BFS 最短路徑
   - 時間複雜度：O(n)
   - 空間複雜度：O(w)，w 為樹的最大寬度
   - 學習重點：
     - BFS 找最短路徑
     - 層次遍歷
     - 終止條件判斷

2. [1030. Matrix Cells in Distance Order](https://leetcode.com/problems/matrix-cells-in-distance-order/) (Easy)
   - 核心技巧：距離排序
   - 時間複雜度：O(n×m×log(n×m))
   - 空間複雜度：O(n×m)
   - 學習重點：
     - 曼哈頓距離
     - BFS 應用
     - 矩陣座標處理

#### Medium 題目

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

### 3. 拓撲排序練習（由易到難）

#### Easy 題目

1. [2192. All Ancestors of a Node in a Directed Acyclic Graph](https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/) (Easy)
   - 核心技巧：有向圖遍歷
   - 時間複雜度：O(V×(V+E))
   - 空間複雜度：O(V×V)
   - 學習重點：
     - 有向無環圖概念
     - 祖先節點的尋找
     - 依賴關係的處理

#### Medium 題目

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

### 4. 並查集練習（由易到難）

#### Easy 題目

1. [1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) (Easy)

   - 核心技巧：並查集基礎
   - 時間複雜度：O(V+E)
   - 空間複雜度：O(V)
   - 學習重點：
     - 並查集基本操作
     - 連通性判斷
     - 路徑存在性檢查

2. [2421. Number of Good Paths](https://leetcode.com/problems/number-of-good-paths/) (Easy)
   - 核心技巧：並查集應用
   - 時間複雜度：O(n×α(n))
   - 空間複雜度：O(n)
   - 學習重點：
     - 並查集進階應用
     - 連通分量處理
     - 路徑計數技巧

#### Medium 題目

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

### 3.1 DFS 與 BFS 訪問標記時機的差異

在圖的遍歷中，DFS 和 BFS 在訪問標記（visited 標記）的時機上有重要差異：

#### DFS 訪問標記特點
- 處理節點時標記：在 DFS 中，我們在實際處理節點時才將其標記為已訪問 `if node not in visited: visited.add(node)`
- 原因：因為同一個節點可能被多次加入堆疊（stack），所以需要在處理時檢查以避免重複處理
- 特性：允許節點多次進入堆疊，但只處理一次

#### BFS 訪問標記特點
- 入佇列時標記：在 BFS 中，我們在將節點加入佇列（queue）的同時就將其標記為已訪問 `visited.add(next_node)`
- 原因：這樣可以確保每個節點只會被加入佇列一次，從佇列中取出的節點一定是已訪問過的
- 特性：每個節點最多只會進入佇列一次，提高了空間效率

#### 實作差異的影響
- BFS 不需要在 `node = queue.popleft()` 後檢查 `if node not in visited`
- BFS 的這種實作方式可以減少佇列中的元素數量，提高效率
- 兩種方法在功能上等價，但在特定場景下可能有效率差異

#### 為什麼 BFS 不會出現同一節點多次入佇列的情況

在 BFS 實作中，我們採用「先標記再加入」的順序：

```python
if next_node not in visited:
    visited.add(next_node)  # 立即標記為已訪問
    queue.append(next_node)  # 然後加入佇列
```

這種機制確保了同一節點不會被多次加入佇列：

1. 即時標記：發現未訪問的相鄰節點時，立即標記為已訪問，然後才加入佇列
   
2. 層次遍歷特性：BFS 按層次遍歷，處理第 n 層節點時，所有第 n-1 層節點都已被標記為已訪問

3. 多路徑保護：若節點 A 有多個鄰居都指向節點 B：
   - 當第一個鄰居發現 B 時，B 被標記為已訪問並加入佇列
   - 當後續鄰居再次發現 B 時，因為 B 已被標記為已訪問，不會再次加入佇列

相比之下，DFS 允許同一節點多次入堆疊：

```python
node = stack.pop()
if node not in visited:  # 取出後才檢查
    visited.add(node)
    for next_node in graph[node]:
        if next_node not in visited:
            stack.append(next_node)  # 只檢查但不標記
```

DFS 中同一節點可多次入堆疊的原因：

1. 延遲標記：DFS 在實際處理節點時才標記為已訪問，而不是在加入堆疊時
   
2. 深度優先特性：DFS 可能通過不同路徑多次「發現」同一節點，在發現時只檢查但不標記
   
3. 堆疊後進先出：由於堆疊的特性，將一個節點的所有鄰居加入後，會先處理最後加入的節點

#### 實際例子

考慮簡單圖：A → B → C，且 A 也直接連接到 C (A → C)

在 BFS 中：
1. 訪問 A，將 B 和 C 標記為已訪問並加入佇列
2. 訪問 B，檢查 C，但 C 已被標記為已訪問，不會再次加入佇列
3. 訪問 C

在 DFS 中：
1. 訪問 A，將 C 和 B 加入堆疊（假設先加入 C 再加入 B）
2. 取出並訪問 B，將 C 加入堆疊（此時 C 在堆疊中出現兩次）
3. 取出並訪問 C
4. 取出第二個 C，發現已訪問，跳過

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
