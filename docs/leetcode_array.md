# Array 資料結構 LeetCode 學習清單

## 基本解題技巧

### 1. 雙指標技巧 (Two Pointers)

雙指標是一種常用的陣列處理技巧，主要有以下幾種應用方式：

#### 1.1 頭尾指標 (Head & Tail Pointers)

- 使用時機：
  - 搜尋成對的元素（如 Two Sum）
  - 陣列反轉
  - 已排序陣列的搜尋
- 實作重點：
  - 通常一個指標從頭開始，一個從尾開始
  - 根據條件向中間移動
  - 需要注意指標相遇的條件

#### 1.2 同向雙指標 (Same Direction Pointers)

- 使用時機：
  - 移除重複元素
  - 陣列重組
  - 快慢指標應用
- 實作重點：
  - 一個指標通常作為讀取位置
  - 另一個指標作為寫入位置
  - 需要維護不變量（invariant）

#### 1.3 滑動視窗 (Sliding Window)

- 使用時機：
  - 連續子陣列問題
  - 字串子串問題
  - 固定或可變大小的區間處理
- 實作重點：
  - 維護視窗大小
  - 更新視窗時的狀態管理
  - 最佳化條件的判斷

### 2. 原地修改陣列 (In-place Modification)

這是一種空間複雜度優化技巧，主要用於：

#### 2.1 交換元素 (Swapping Elements)

- 使用時機：
  - 排序問題
  - 分組問題
  - 重組陣列
- 實作技巧：
  - 使用 XOR 或臨時變數進行交換
  - 注意元素的順序維護
  - 避免不必要的交換操作

#### 2.2 覆寫元素 (Overwriting Elements)

- 使用時機：
  - 移除元素
  - 合併陣列
  - 壓縮陣列
- 實作技巧：
  - 從前往後或從後往前覆寫
  - 使用額外指標追蹤寫入位置
  - 保持原有順序或特定條件

### 3. 雜湊表輔助 (HashMap Helper)

雜湊表是解決陣列問題的強大工具：

#### 3.1 計數應用

- 使用時機：
  - 元素頻率統計
  - 重複元素檢測
  - 配對問題
- 實作技巧：
  - 使用 HashMap 儲存頻率
  - 使用 HashSet 檢查唯一性
  - 注意空間使用效率

#### 3.2 索引映射

- 使用時機：
  - 快速查找元素位置
  - 建立元素關聯
  - 空間換時間的優化
- 實作技巧：
  - 鍵值對的選擇
  - 碰撞處理
  - 更新策略

### 4. 前綴和技巧 (Prefix Sum)

前綴和是處理區間查詢的有效工具：

#### 4.1 基本概念

- 定義：第 i 個前綴和為前 i 個元素的總和
- 特性：
  - 可 O(1) 時間查詢任意區間和
  - 需要 O(n) 預處理時間
  - 適合頻繁的區間查詢

#### 4.2 應用場景

- 區間和查詢
- 連續子陣列問題
- 差分數組應用

### 5. 分治法 (Divide and Conquer)

將大問題分解為小問題的策略：

#### 5.1 基本步驟

- 分解：將問題分解為子問題
- 解決：遞迴解決子問題
- 合併：將子問題的解合併

#### 5.2 應用場景

- 排序算法
- 搜尋問題
- 區間處理

## 練習題目

### 1. 雙指標技巧練習

#### 1.1 同向雙指標題目

1. [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) (Easy)

   - 核心技巧：非零元素前移
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 如何維護兩個指標的關係
     - 如何確保元素相對順序不變
     - 原地修改的實現方式

2. [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) (Easy)
   - 核心技巧：快慢指標
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 利用陣列已排序的特性
     - 如何處理重複元素
     - 返回新長度的處理

#### 1.2 頭尾指標題目

1. [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) (Easy)

   - 核心技巧：收斂搜尋
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 如何利用排序特性優化搜尋
     - 指標移動的條件判斷
     - 與一般 Two Sum 的區別

2. [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) (Medium)
   - 核心技巧：貪婪策略
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 面積計算的理解
     - 指標移動的選擇策略
     - 最優解的證明思路

### 2. 雜湊表應用練習

1. [1. Two Sum](https://leetcode.com/problems/two-sum/) (Easy)

   - 核心技巧：一遍雜湊表
   - 時間複雜度：O(n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 雜湊表的建立時機
     - 如何處理配對元素
     - 與排序解法的比較

2. [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) (Easy)
   - 核心技巧：集合特性應用
   - 時間複雜度：O(n)
   - 空間複雜度：O(n)
   - 學習重點：
     - Set 的使用時機
     - 空間與時間的權衡
     - 與排序解法的比較

### 3. 前綴和技巧練習

1. [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/) (Easy)

   - 核心技巧：原地前綴和
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 前綴和的基本概念
     - 原地修改的實現
     - 應用場景理解

2. [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) (Medium)
   - 核心技巧：前綴和 + 雜湊表
   - 時間複雜度：O(n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 前綴和與子數組和的關係
     - 雜湊表優化查詢
     - 處理負數和零的情況

### 4. 分治法練習

1. [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (Medium)
   - 核心技巧：分治或動態規劃
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 分治解法的思路
     - 與動態規劃解法的比較
     - Kadane 算法的應用

## 學習建議

### 1. 學習順序

1. 第一週：雙指標基礎 (283, 26)
2. 第二週：雜湊表應用 (1, 217)
3. 第三週：前綴和入門 (1480)
4. 第四週：進階雙指標 (11, 167)
5. 第五週：綜合應用 (560, 53)

### 2. 學習方法

1. 每個題目先自己思考 15-20 分鐘
2. 卡住時參考提示，而不是直接看解答
3. 解出後，思考：
   - 時間複雜度是否最優？
   - 空間複雜度是否可以優化？
   - 是否有其他解法？
4. 一週後回顧，重新做一遍

### 3. 進階建議

1. 嘗試在不同題目中結合多種技巧
2. 練習解題時間的控制
3. 建立自己的解題模板
4. 整理常見的錯誤和陷阱

## Python 解題模板

### 1. 雙指標模板

#### 1.1 同向雙指標基本模板

```python
def two_pointers(arr: List[int]) -> List[int]:
    # 初始化雙指標
    slow = fast = 0
    n = len(arr)

    while fast < n:
        # 根據條件移動快指標
        if condition(arr[fast]):
            # 可能需要交換或處理元素
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1
        fast += 1

    return arr[:slow]  # 或其他需要的返回值
```

#### 1.2 頭尾指標基本模板

```python
def head_tail_pointers(arr: List[int]) -> List[int]:
    left, right = 0, len(arr) - 1

    while left < right:
        # 根據條件移動指標
        if condition_left(arr[left]):
            left += 1
            continue
        if condition_right(arr[right]):
            right -= 1
            continue

        # 處理找到的元素
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr
```

#### 1.3 滑動視窗基本模板

```python
def sliding_window(arr: List[int], k: int) -> List[int]:
    # 初始化視窗和結果
    window = {}  # 或使用其他資料結構
    result = []
    left = right = 0

    while right < len(arr):
        # 擴展視窗
        window[arr[right]] = window.get(arr[right], 0) + 1
        right += 1

        # 縮小視窗
        while condition(window):
            window[arr[left]] -= 1
            if window[arr[left]] == 0:
                del window[arr[left]]
            left += 1

        # 記錄結果
        if right - left == k:
            result.append(some_calculation)

    return result
```

### 2. 前綴和模板

#### 2.1 一維前綴和

```python
def prefix_sum(arr: List[int]) -> List[int]:
    n = len(arr)
    prefix = [0] * (n + 1)  # 多一個位置方便計算

    # 建立前綴和陣列
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    # 查詢區間 [left, right] 的和
    def query(left: int, right: int) -> int:
        return prefix[right + 1] - prefix[left]

    return prefix
```

#### 2.2 二維前綴和

```python
def matrix_prefix_sum(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix or not matrix[0]:
        return []

    m, n = len(matrix), len(matrix[0])
    prefix = [[0] * (n + 1) for _ in range(m + 1)]

    # 建立二維前綴和
    for i in range(m):
        for j in range(n):
            prefix[i + 1][j + 1] = (
                prefix[i + 1][j] +
                prefix[i][j + 1] -
                prefix[i][j] +
                matrix[i][j]
            )

    # 查詢子矩陣和 [(x1,y1), (x2,y2)]
    def query(x1: int, y1: int, x2: int, y2: int) -> int:
        return (
            prefix[x2 + 1][y2 + 1] -
            prefix[x2 + 1][y1] -
            prefix[x1][y2 + 1] +
            prefix[x1][y1]
        )

    return prefix
```

### 3. 雜湊表模板

#### 3.1 計數器模板

```python
from collections import Counter, defaultdict

def counter_template(arr: List[int]) -> bool:
    # 使用 Counter
    count = Counter(arr)

    # 或使用 defaultdict
    freq = defaultdict(int)
    for num in arr:
        freq[num] += 1

    # 處理計數結果
    for num, freq in count.items():
        if condition(num, freq):
            return True

    return False
```

#### 3.2 索引映射模板

```python
def index_mapping(arr: List[int]) -> dict:
    # 值到索引的映射
    value_to_index = {}

    for i, num in enumerate(arr):
        # 根據需求保存單個索引或多個索引
        if num not in value_to_index:
            value_to_index[num] = i
        # 或保存所有索引
        value_to_index[num] = value_to_index.get(num, []) + [i]

    return value_to_index
```

### 4. 二分搜尋模板

#### 4.1 基本二分搜尋

```python
def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # 或 left（用於插入位置）
```

#### 4.2 尋找左邊界

```python
def binary_search_left(arr: List[int], target: int) -> int:
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
```

#### 4.3 尋找右邊界

```python
def binary_search_right(arr: List[int], target: int) -> int:
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left - 1
```

### 5. 常用的輔助函數

```python
# 交換陣列中的兩個元素
def swap(arr: List[int], i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]

# 反轉陣列的一部分
def reverse(arr: List[int], start: int, end: int) -> None:
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# 檢查是否為回文
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# 找出最大公因數
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# 找出最小公倍數
def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)
```

這些模板提供了基本的框架，在實際解題時需要根據具體問題進行調整。建議：

1. 理解每個模板的核心邏輯
2. 練習修改模板以適應不同的問題需求
3. 注意邊界條件的處理
4. 根據實際需求選擇合適的資料結構
5. 在解題時注意時間和空間複雜度的優化
