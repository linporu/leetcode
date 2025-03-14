# 貪婪演算法技巧與 LeetCode 學習清單

## 基本解題技巧

### 1. 貪婪演算法的基本概念

- 貪婪算法是一種在每一步選擇中都採取當下最佳選擇的演算法策略，希望透過局部最佳解來達到全局最佳解。

- 使用時機：
  - 問題具有「最優子結構」特性
  - 局部最優解能導致全局最優解
  - 需要最大化或最小化某個目標函數
  - 問題可以分解成一系列決策
- 實作重點：
  - 設計合適的貪婪策略
  - 證明貪婪策略的正確性
  - 高效實現貪婪選擇
  - 處理邊界情況

### 2. 貪婪算法模板

貪婪演算法通常遵循以下步驟：

```python
def greedy_algorithm(problem_input):
    """貪婪演算法的通用模板

    Args:
        problem_input: 問題的輸入數據

    Returns:
        解決方案或最優值
    """
    # 1. 初始化結果或解決方案
    result = initial_value

    # 2. 根據貪婪策略對問題元素進行排序或處理
    sorted_items = sort_according_to_greedy_criteria(problem_input)

    # 3. 依次處理每個元素，做出貪婪選擇
    for item in sorted_items:
        if is_feasible(item, result):
            # 4. 將當前貪婪選擇納入解決方案
            result = update_solution(result, item)

    # 5. 返回最終解決方案
    return result
```

主要優點：

1. 實現簡單直觀
2. 時間複雜度通常較低
3. 不需要考慮所有可能的解
4. 在適用的問題上非常高效

使用時機：

1. 問題具有貪婪選擇性質
2. 問題具有最優子結構
3. 局部最優選擇不會影響後續選擇
4. 需要快速找到近似最優解

### 3. 貪婪演算法優化技巧

#### 排序策略

##### 1. 基於比值排序

- 概念：根據某種比值（如性價比）進行排序
- 實作範例：

```python
def fractional_knapsack(items, capacity):
    """分數背包問題的貪婪解法
    
    Args:
        items: 物品列表，每個物品為 (value, weight) 元組
        capacity: 背包容量
        
    Returns:
        float: 最大價值
    """
    # 計算每個物品的價值/重量比
    value_weight_ratio = [(v / w, v, w) for v, w in items]
    # 根據比值降序排序
    value_weight_ratio.sort(reverse=True)
    
    total_value = 0
    remaining_capacity = capacity
    
    for ratio, value, weight in value_weight_ratio:
        if remaining_capacity >= weight:
            # 可以完整放入物品
            total_value += value
            remaining_capacity -= weight
        else:
            # 只能放入物品的一部分
            total_value += ratio * remaining_capacity
            break
            
    return total_value
```

##### 2. 基於差值排序

- 概念：根據選擇與不選擇之間的差值進行排序
- 實作範例：

```python
def activity_selection(activities):
    """活動選擇問題的貪婪解法
    
    Args:
        activities: 活動列表，每個活動為 (start_time, end_time) 元組
        
    Returns:
        list: 選擇的活動列表
    """
    # 根據結束時間排序
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]  # 選擇第一個活動
    last_end_time = activities[0][1]
    
    for start, end in activities[1:]:
        if start >= last_end_time:  # 如果當前活動的開始時間不早於上一個選中活動的結束時間
            selected.append((start, end))
            last_end_time = end
            
    return selected
```

##### 3. 基於多重條件排序

- 概念：使用多個條件進行排序決策
- 實作範例：

```python
def job_scheduling(jobs):
    """工作排程問題的貪婪解法
    
    Args:
        jobs: 工作列表，每個工作為 (deadline, profit) 元組
        
    Returns:
        int: 最大利潤
    """
    # 根據利潤降序排序
    jobs.sort(key=lambda x: x[1], reverse=True)
    
    max_deadline = max(job[0] for job in jobs)
    slot = [-1] * (max_deadline + 1)  # 時間槽，0 不使用
    
    total_profit = 0
    
    for deadline, profit in jobs:
        # 尋找最晚的可用時間槽
        for t in range(deadline, 0, -1):
            if slot[t] == -1:
                slot[t] = 1  # 標記為已使用
                total_profit += profit
                break
                
    return total_profit
```

#### 貪婪策略選擇

##### 1. 最小化成本策略

- 概念：每次選擇成本最小的選項
- 實作範例：

```python
def minimum_spanning_tree_prim(graph, start_vertex):
    """Prim 算法求最小生成樹
    
    Args:
        graph: 圖的鄰接矩陣表示
        start_vertex: 起始頂點
        
    Returns:
        list: 最小生成樹的邊集合
    """
    n = len(graph)
    # 記錄頂點是否已加入MST
    in_mst = [False] * n
    # 記錄到達每個頂點的最小權重
    key = [float('inf')] * n
    # 記錄每個頂點的父節點
    parent = [-1] * n
    
    key[start_vertex] = 0
    
    for _ in range(n):
        # 找出未加入MST且權重最小的頂點
        min_key = float('inf')
        min_vertex = -1
        
        for v in range(n):
            if not in_mst[v] and key[v] < min_key:
                min_key = key[v]
                min_vertex = v
        
        # 將該頂點加入MST
        in_mst[min_vertex] = True
        
        # 更新相鄰頂點的權重
        for v in range(n):
            if (graph[min_vertex][v] > 0 and 
                not in_mst[v] and 
                graph[min_vertex][v] < key[v]):
                key[v] = graph[min_vertex][v]
                parent[v] = min_vertex
    
    # 構建MST的邊集合
    mst_edges = []
    for v in range(1, n):
        mst_edges.append((parent[v], v, graph[parent[v]][v]))
        
    return mst_edges
```

##### 2. 最大化收益策略

- 概念：每次選擇收益最大的選項
- 實作範例：

```python
def huffman_coding(frequencies):
    """霍夫曼編碼的貪婪解法
    
    Args:
        frequencies: 字符頻率字典
        
    Returns:
        dict: 字符編碼字典
    """
    import heapq
    from collections import defaultdict
    
    # 創建葉節點並構建最小堆
    heap = [[freq, [char, ""]] for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    # 當堆中至少有兩個節點時
    while len(heap) > 1:
        # 取出兩個頻率最小的節點
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        
        # 為這些節點分配編碼 (0 和 1)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        
        # 將這兩個節點合併，並放回堆中
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    # 構建編碼字典
    codes = defaultdict(str)
    for pair in heap[0][1:]:
        codes[pair[0]] = pair[1]
        
    return codes
```

##### 3. 平衡策略

- 概念：在多個目標之間尋找平衡
- 實作範例：

```python
def load_balancing(tasks, processors):
    """負載平衡問題的貪婪解法
    
    Args:
        tasks: 任務列表，每個任務為其處理時間
        processors: 處理器數量
        
    Returns:
        list: 每個處理器的任務分配
    """
    # 初始化每個處理器的負載
    loads = [0] * processors
    # 初始化每個處理器的任務分配
    assignments = [[] for _ in range(processors)]
    
    # 根據任務處理時間降序排序
    tasks.sort(reverse=True)
    
    # 為每個任務分配處理器
    for task in tasks:
        # 找出負載最小的處理器
        min_load_idx = loads.index(min(loads))
        # 分配任務
        assignments[min_load_idx].append(task)
        # 更新處理器負載
        loads[min_load_idx] += task
    
    return assignments
```

## 練習題目

### 1. 基礎貪婪練習（Easy）

1. [455. Assign Cookies](https://leetcode.com/problems/assign-cookies/) (Easy)

   - 核心技巧：排序與貪婪分配
   - 時間複雜度：O(n log n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 基本貪婪策略的應用
     - 排序後的貪婪選擇
     - 滿足條件的最小化分配

2. [860. Lemonade Change](https://leetcode.com/problems/lemonade-change/) (Easy)

   - 核心技巧：模擬與貪婪找零
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 貪婪找零策略
     - 資源管理與分配
     - 邊界情況處理

3. [1005. Maximize Sum Of Array After K Negations](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/) (Easy)
   - 核心技巧：排序與選擇性反轉
   - 時間複雜度：O(n log n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 貪婪選擇的優先順序
     - 多次操作的最優策略
     - 奇偶性質的利用

### 2. 進階貪婪練習（Medium）

1. [55. Jump Game](https://leetcode.com/problems/jump-game/) (Medium)

   - 核心技巧：前向貪婪
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 貪婪策略的正確性證明
     - 最遠可達位置的維護
     - 問題的貪婪特性分析

2. [134. Gas Station](https://leetcode.com/problems/gas-station/) (Medium)

   - 核心技巧：環形路徑與累積和
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 環形問題的貪婪解法
     - 起點選擇的貪婪策略
     - 問題轉化與簡化

3. [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) (Medium)

   - 核心技巧：區間調度
   - 時間複雜度：O(n log n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 區間問題的貪婪解法
     - 結束時間排序的重要性
     - 最小化移除數量的策略

4. [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) (Medium)

   - 核心技巧：區間合併
   - 時間複雜度：O(n log n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 區間重疊的處理
     - 貪婪選擇的正確性
     - 排序策略的選擇

5. [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/) (Medium)

   - 核心技巧：頻率排序與填充
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 任務調度的貪婪策略
     - 頻率分析與排序
     - 數學公式的推導

6. [1029. Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/) (Medium)

   - 核心技巧：差值排序
   - 時間複雜度：O(n log n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 基於差值的貪婪策略
     - 成本最小化的分配
     - 排序後的平衡分配

7. [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) (Medium)
   - 核心技巧：優先隊列
   - 時間複雜度：O(n log n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 堆（優先隊列）的使用
     - 貪婪選擇的實現
     - 模擬過程的優化

### 3. 高級貪婪練習（Hard）

1. [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/) (Hard)

   - 核心技巧：範圍貪婪
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 貪婪策略的設計
     - 最小跳躍次數的計算
     - 範圍更新的技巧

2. [135. Candy](https://leetcode.com/problems/candy/) (Hard)

   - 核心技巧：雙向遍歷
   - 時間複雜度：O(n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 多約束條件的處理
     - 雙向貪婪策略
     - 最小化總量的技巧

3. [502. IPO](https://leetcode.com/problems/ipo/) (Hard)

   - 核心技巧：雙優先隊列
   - 時間複雜度：O(n log n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 資本與利潤的平衡
     - 多輪貪婪選擇
     - 優先隊列的高級應用

4. [871. Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/) (Hard)
   - 核心技巧：優先隊列與貪婪選擇
   - 時間複雜度：O(n log n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 延遲選擇的貪婪策略
     - 最大堆的應用
     - 燃料管理的最優化

## 附錄

### 常見變體模版

#### 1. 區間調度問題模板

```python
def interval_scheduling(intervals):
    """區間調度問題的貪婪解法
    
    Args:
        intervals: 區間列表，每個區間為 (start, end) 元組
        
    Returns:
        list: 選擇的區間列表
    """
    if not intervals:
        return []
        
    # 根據結束時間排序
    intervals.sort(key=lambda x: x[1])
    
    result = [intervals[0]]
    last_end = intervals[0][1]
    
    for start, end in intervals[1:]:
        if start >= last_end:  # 無重疊
            result.append((start, end))
            last_end = end
            
    return result
```

#### 2. 分數背包問題模板

```python
def fractional_knapsack(items, capacity):
    """分數背包問題的貪婪解法
    
    Args:
        items: 物品列表，每個物品為 (value, weight) 元組
        capacity: 背包容量
        
    Returns:
        float: 最大價值
    """
    # 計算每個物品的價值/重量比
    items_with_ratio = [(v, w, v/w) for v, w in items]
    # 根據比值降序排序
    items_with_ratio.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0
    remaining_capacity = capacity
    
    for value, weight, ratio in items_with_ratio:
        if remaining_capacity >= weight:
            # 可以完整放入物品
            total_value += value
            remaining_capacity -= weight
        else:
            # 只能放入物品的一部分
            total_value += ratio * remaining_capacity
            break
            
    return total_value
```

#### 3. 霍夫曼編碼模板

```python
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''
        
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(data):
    """霍夫曼編碼的貪婪解法
    
    Args:
        data: 待編碼的字符串
        
    Returns:
        tuple: (編碼後的字符串, 編碼表)
    """
    from collections import Counter
    import heapq
    
    # 計算頻率
    frequency = Counter(data)
    
    # 創建節點並構建最小堆
    heap = [Node(freq, symbol) for symbol, freq in frequency.items()]
    heapq.heapify(heap)
    
    # 當堆中至少有兩個節點時
    while len(heap) > 1:
        # 取出兩個頻率最小的節點
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # 分配編碼 (0 和 1)
        left.code = '0'
        right.code = '1'
        
        # 創建新節點，頻率為兩個子節點的和
        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        
        # 將新節點放回堆中
        heapq.heappush(heap, new_node)
    
    # 構建編碼表
    root = heap[0]
    codes = {}
    
    def assign_codes(node, code=''):
        if node:
            node.code = code
            
            if node.left is None and node.right is None:  # 葉節點
                codes[node.symbol] = code
                
            assign_codes(node.left, code + '0')
            assign_codes(node.right, code + '1')
    
    assign_codes(root)
    
    # 編碼數據
    encoded_data = ''.join([codes[symbol] for symbol in data])
    
    return encoded_data, codes
```
