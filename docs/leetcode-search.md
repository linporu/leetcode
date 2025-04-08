# 搜尋演算法技巧與 LeetCode 學習清單

## 基本解題技巧

### 1. 搜尋演算法的基本概念

- 使用時機：
  - 需要在資料集中尋找特定元素
  - 需要找出符合特定條件的所有解
  - 需要在搜尋空間中找出最佳解
- 實作重點：
  - 選擇合適的搜尋策略
  - 設計有效的剪枝條件
  - 注意搜尋空間的大小
  - 考慮時間和空間的平衡

### 2. 常見搜尋策略

#### 二分搜尋（Binary Search）

- 特點：
  - 適用於已排序的資料
  - 每次將搜尋範圍減半
  - 時間複雜度為 O(log n)
- 實作模板：

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # 找不到目標值
```

#### 深度優先搜尋（DFS）

- 特點：
  - 優先探索到最深層
  - 使用堆疊（遞迴或顯式）實現
  - 適合樹狀結構和圖的搜尋
- 實作模板：

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

#### 廣度優先搜尋（BFS）

- 特點：
  - 逐層探索
  - 使用佇列實現
  - 找到的路徑為最短路徑
- 實作模板：

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

#### DFS 與 BFS 的比較與選擇

- 搜索空間的探索方式：

  - DFS：沿著一條路徑一直探索到底，如果發現不可行，則回退到上一步嘗試其他選擇
  - BFS：按照層級探索，先探索所有相鄰的可能性，再向下一層擴展

- 實現機制：

  - DFS：通常使用遞迴或堆疊實現，使用系統調用棧隱式記錄路徑
  - BFS：通常使用隊列實現，沒有回退操作，只有入隊和出隊

- 適用問題類型：

  - DFS 適合：

    - 需要列舉所有可能解的問題（如排列、組合、子集）
    - 需要找到所有解的問題
    - 搜索深度有限的問題
    - 記憶體空間有限的情況（因為只需存儲當前路徑）

  - BFS 適合：
    - 最短路徑問題
    - 層級遍歷問題
    - 需要找到最優解（在無權圖中）的問題
    - 搜索寬度有限的問題

- 空間複雜度比較：

  - DFS：O(h)，h 為搜索深度
  - BFS：O(w)，w 為搜索寬度（通常較大）

- 實際應用選擇：

  - 如果需要找到所有可能的解，選擇 DFS
  - 如果需要找到最短路徑或最優解，選擇 BFS
  - 如果搜索空間非常大且解在較深層，選擇 DFS
  - 如果解可能在較淺層，選擇 BFS

- 常見誤區：
  - 回溯法是 DFS 的一種應用，而非 BFS 的應用
  - BFS 不適合需要「選擇-探索-撤銷」模式的問題
  - DFS 不保證找到最短路徑

### 3. 搜尋優化技巧

#### 二分搜尋的變體

- 找出第一個符合條件的元素
- 找出最後一個符合條件的元素
- 找出最接近目標值的元素
- 實作模板：

```python
def binary_search_leftmost(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

def binary_search_rightmost(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left - 1
```

#### 搜尋剪枝技巧

- 使用時機：
  - 搜尋空間過大
  - 存在明顯無效的搜尋路徑
  - 可以提前判斷解的可行性
- 實作重點：
  - 設計有效的剪枝條件
  - 在適當的時機進行剪枝
  - 確保剪枝不會遺漏正確解

##### 1. 邊界剪枝（Boundary Pruning）

- 概念：在搜尋過程中，如果當前狀態超出問題的合理邊界，就停止繼續搜尋
- 適用場景：
  - 數值範圍限制
  - 陣列邊界檢查
  - 時間或空間限制
- 實作範例：

```python
def dfs_with_boundary_pruning(grid, x, y, target):
    # 邊界剪枝：檢查座標是否在網格範圍內
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return False

    # 數值範圍剪枝：如果當前值已經超過目標，停止搜尋
    if grid[x][y] > target:
        return False

    # 繼續搜尋...
```

##### 2. 可行性剪枝（Feasibility Pruning）

- 概念：根據問題的約束條件，提前判斷當前路徑是否可能達到有效解
- 適用場景：
  - 組合總和問題
  - 排列組合問題
  - 路徑規劃問題
- 實作範例：

```python
def combination_sum_with_pruning(candidates, target, path, start):
    # 可行性剪枝：如果當前和已經超過目標，停止搜尋
    current_sum = sum(path)
    if current_sum > target:
        return

    if current_sum == target:
        result.append(path[:])
        return

    for i in range(start, len(candidates)):
        # 可行性剪枝：如果加入當前數字必然超過目標，跳過
        if current_sum + candidates[i] > target:
            continue
        path.append(candidates[i])
        combination_sum_with_pruning(candidates, target, path, i)
        path.pop()
```

##### 3. 最優性剪枝（Optimality Pruning）

- 概念：在搜尋最優解時，如果當前路徑已經不可能優於已知的最優解，就停止搜尋
- 適用場景：
  - 最短路徑問題
  - 最小成本問題
  - 最優化問題
- 實作範例：

```python
def tsp_with_pruning(graph, path, current_cost, best_cost):
    n = len(graph)
    if len(path) == n:
        return min(best_cost, current_cost)

    for next_city in range(n):
        if next_city not in path:
            # 最優性剪枝：如果當前成本已經超過最佳解，停止搜尋
            if current_cost + graph[path[-1]][next_city] >= best_cost:
                continue
            path.append(next_city)
            best_cost = tsp_with_pruning(graph, path,
                                       current_cost + graph[path[-1]][next_city],
                                       best_cost)
            path.pop()

    return best_cost
```

##### 4. 重複狀態剪枝（Duplicate State Pruning）

- 概念：避免重複搜尋已經訪問過的狀態
- 適用場景：
  - 圖的搜尋
  - 狀態空間搜尋
  - 動態規劃優化
- 實作範例：

```python
def word_search_with_pruning(board, word):
    def dfs(x, y, index, visited):
        # 重複狀態剪枝：檢查是否已訪問
        if (x, y) in visited:
            return False

        if index == len(word):
            return True

        visited.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < len(board) and
                0 <= new_y < len(board[0]) and
                board[new_x][new_y] == word[index]):
                if dfs(new_x, new_y, index + 1, visited):
                    return True
        visited.remove((x, y))
        return False

    # 主搜尋邏輯...
```

##### 剪枝策略的選擇原則

1. 優先使用計算成本低的剪枝條件
2. 剪枝條件要確保不會誤剪掉可能的正確解
3. 根據問題特性組合使用多種剪枝策略
4. 在合適的搜尋階段進行剪枝，避免過早或過晚剪枝

##### 實際應用範例

以 N 皇后問題為例，結合多種剪枝策略：

```python
def solve_n_queens(n):
    def is_safe(board, row, col):
        # 邊界剪枝
        if row >= n or col >= n:
            return False

        # 可行性剪枝：檢查列衝突
        for i in range(row):
            if board[i] == col:
                return False

        # 可行性剪枝：檢查對角線衝突
        for i in range(row):
            if abs(board[i] - col) == abs(i - row):
                return False

        return True

    def place_queen(board, row):
        if row == n:
            return 1

        count = 0
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                count += place_queen(board, row + 1)
                board[row] = -1

        return count

    board = [-1] * n
    return place_queen(board, 0)
```

## 練習題目

### 1. 二分搜尋練習

#### Easy 題目

1. [704. Binary Search](https://leetcode.com/problems/binary-search/) (Easy)

   - 核心技巧：基本二分搜尋
   - 時間複雜度：O(log n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 二分搜尋的基本實現
     - 邊界條件的處理
     - 中間位置的計算

2. [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) (Easy)

   - 核心技巧：二分搜尋變體
   - 時間複雜度：O(log n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 插入位置的確定
     - 邊界情況的處理
     - 搜尋範圍的調整

3. [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/) (Easy)
   - 核心技巧：二分搜尋的實際應用
   - 時間複雜度：O(log n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 處理數值範圍
     - 避免整數溢出
     - 結果的取整處理

#### Medium 題目

1. [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) (Medium)

   - 核心技巧：二分搜尋邊界
   - 時間複雜度：O(log n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 尋找左右邊界
     - 二分搜尋的變體
     - 重複元素的處理

2. [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) (Medium)
   - 核心技巧：旋轉數組的二分搜尋
   - 時間複雜度：O(log n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 處理旋轉數組
     - 判斷有序區間
     - 分段搜尋策略

### 2. 深度優先搜尋練習

#### Easy 題目

1. [100. Same Tree](https://leetcode.com/problems/same-tree/) (Easy)

   - 核心技巧：基本樹狀 DFS
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)，h 為樹高
   - 學習重點：
     - 遞迴的基本概念
     - 樹的遍歷方式
     - 節點比較邏輯

2. [112. Path Sum](https://leetcode.com/problems/path-sum/) (Easy)

   - 核心技巧：路徑追蹤 DFS
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)，h 為樹高
   - 學習重點：
     - 路徑和的計算
     - 終止條件的判斷
     - 遞迴參數的傳遞

3. [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) (Easy)
   - 核心技巧：路徑記錄 DFS
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)，h 為樹高
   - 學習重點：
     - 路徑的字串表示
     - 回溯處理
     - 結果的收集方式

#### Medium 題目

1. [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) (Medium)

   - 核心技巧：網格 DFS
   - 時間複雜度：O(m \* n)
   - 空間複雜度：O(m \* n)
   - 學習重點：
     - 網格 DFS 的實現
     - 已訪問位置的標記
     - 連通區域的計數

2. [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) (Medium)
   - 核心技巧：邊界 DFS
   - 時間複雜度：O(m \* n)
   - 空間複雜度：O(m \* n)
   - 學習重點：
     - 從邊界開始的 DFS
     - 狀態的標記與更新
     - 條件判斷的處理

### 3. 廣度優先搜尋練習

#### Easy 題目

1. [111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) (Easy)

   - 核心技巧：層次遍歷 BFS
   - 時間複雜度：O(n)
   - 空間複雜度：O(w)，w 為樹的最大寬度
   - 學習重點：
     - 層次遍歷的實現
     - 最短路徑的尋找
     - 終止條件的判斷

2. [637. Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/) (Easy)

   - 核心技巧：層次統計 BFS
   - 時間複雜度：O(n)
   - 空間複雜度：O(w)，w 為樹的最大寬度
   - 學習重點：
     - 層次資料的收集
     - 平均值的計算
     - 數值溢出的處理

3. [993. Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/) (Easy)
   - 核心技巧：節點關係 BFS
   - 時間複雜度：O(n)
   - 空間複雜度：O(w)，w 為樹的最大寬度
   - 學習重點：
     - 節點深度的追蹤
     - 父節點的記錄
     - 表親關係的判斷

#### Medium 題目

1. [542. 01 Matrix](https://leetcode.com/problems/01-matrix/) (Medium)

   - 核心技巧：多源 BFS
   - 時間複雜度：O(m \* n)
   - 空間複雜度：O(m \* n)
   - 學習重點：
     - 多源點 BFS
     - 距離的更新
     - 佇列的使用技巧

2. [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) (Medium)
   - 核心技巧：時間推進 BFS
   - 時間複雜度：O(m \* n)
   - 空間複雜度：O(m \* n)
   - 學習重點：
     - 腐爛過程的模擬
     - 時間的計算
     - 終止條件的判斷
