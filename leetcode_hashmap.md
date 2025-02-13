# HashMap 解題技巧與 LeetCode 學習清單

## 基本解題技巧

### 1. 計數統計 (Counting)

- 使用時機：
  - 需要統計元素出現頻率
  - 判斷字串組成是否相同
  - 找出眾數或超過特定次數的元素
- 實作重點：
  - 選擇合適的計數工具（Counter vs dict）
  - 注意計數的更新和刪除操作
  - 考慮空間使用效率

### 2. 快速查找 (Quick Lookup)

- 使用時機：
  - 需要 O(1) 時間判斷元素存在性
  - 需要儲存元素的額外資訊
  - 配對問題（如 Two Sum）
- 實作重點：
  - 選擇合適的資料結構（set vs dict）
  - 考慮鍵值對的設計
  - 注意更新時機

### 3. 分組管理 (Grouping)

- 使用時機：
  - 需要按特定規則分類元素
  - 需要維護多個類別的元素
  - 需要快速查找同組元素
- 實作重點：
  - 設計分組的 key
  - 選擇合適的值容器（list vs set）
  - 注意分組的維護成本

### 4. 滑動視窗 + HashMap

- 使用時機：
  - 需要追蹤視窗內元素頻率
  - 需要維護動態範圍內的元素統計
  - 子字串或子陣列的模式匹配
- 實作重點：
  - 視窗大小的控制
  - 元素進出視窗的更新策略
  - 優化空間使用

### 5. 前綴和 + HashMap

- 使用時機：
  - 需要快速查找累積和
  - 尋找特定和的子陣列
  - 需要追蹤路徑和
- 實作重點：
  - 前綴和的計算與儲存
  - 差值的查找策略
  - 處理負數和零的情況

## 練習題目

### 1. 計數統計練習（由易到難）

1. [383. Ransom Note](https://leetcode.com/problems/ransom-note/) (Easy)

   - 核心技巧：字符頻率比較
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 如何處理頻率比較
     - 提前終止的條件
     - 空間優化技巧

2. [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) (Easy)

   - 核心技巧：字符頻率統計
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)，因為字符集大小固定
   - 學習重點：
     - Counter 的基本使用
     - 如何優化空間複雜度
     - 不同計數方法的比較

3. [169. Majority Element](https://leetcode.com/problems/majority-element/) (Easy)

   - 核心技巧：元素計數
   - 時間複雜度：O(n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 計數統計的應用
     - 不同解法的比較（HashMap vs 摩爾投票算法）
     - 空間優化的思考

4. [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) (Medium)
   - 核心技巧：字符頻率作為鍵值
   - 時間複雜度：O(n \* k)，k 為字串平均長度
   - 空間複雜度：O(n)
   - 學習重點：
     - 如何設計有效的分組 key
     - 字符排序 vs 頻率統計
     - 大量數據的處理策略

### 2. 快速查找練習（由易到難）

1. [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) (Easy)

   - 核心技巧：集合特性
   - 時間複雜度：O(n)
   - 空間複雜度：O(n)
   - 學習重點：
     - Set 的使用場景
     - 時空複雜度權衡
     - 與排序解法的比較

2. [1. Two Sum](https://leetcode.com/problems/two-sum/) (Easy)

   - 核心技巧：一遍哈希表
   - 時間複雜度：O(n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 哈希表的建立時機
     - 配對元素的查找
     - 與雙指針解法的比較

3. [454. 4Sum II](https://leetcode.com/problems/4sum-ii/) (Medium)

   - 核心技巧：分組 + 哈希表
   - 時間複雜度：O(n²)
   - 空間複雜度：O(n²)
   - 學習重點：
     - 如何分組降低複雜度
     - 空間與時間的權衡
     - 處理多個數組的策略

4. [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) (Medium)
   - 核心技巧：集合查找
   - 時間複雜度：O(n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 如何優化連續序列查找
     - 避免重複計算
     - 邊界條件處理

### 3. 滑動視窗 + HashMap 練習

1. [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (Medium)

   - 核心技巧：滑動視窗 + 字符位置記錄
   - 時間複雜度：O(n)
   - 空間複雜度：O(min(m,n))，m 為字符集大小
   - 學習重點：
     - 視窗邊界的移動策略
     - 重複字符的處理
     - 最優解的實現

2. [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) (Medium)
   - 核心技巧：固定大小滑動視窗
   - 時間複雜度：O(n)
   - 空間複雜度：O(k)，k 為字符集大小
   - 學習重點：
     - 視窗大小的維護
     - 字符頻率的比較
     - 優化比較過程

### 4. 前綴和 + HashMap 練習

1. [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) (Medium)
   - 核心技巧：前綴和 + 累積和統計
   - 時間複雜度：O(n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 前綴和的應用
     - 如何處理負數
     - 優化查找過程

### 5. 進階應用練習

1. [146. LRU Cache](https://leetcode.com/problems/lru-cache/) (Medium)

   - 核心技巧：HashMap + 雙向鏈結串列
   - 時間複雜度：O(1) 所有操作
   - 空間複雜度：O(capacity)
   - 學習重點：
     - 資料結構的選擇與組合
     - 快速訪問與更新的實現
     - 容量限制的處理

2. [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) (Medium)
   - 核心技巧：HashMap + 動態陣列
   - 時間複雜度：O(1) 平均
   - 空間複雜度：O(n)
   - 學習重點：
     - 隨機訪問的實現
     - 高效刪除的處理
     - 資料結構的協同使用

## Python 解題模板

### 1. 計數統計模板

```python
# 使用 Counter
from collections import Counter
def count_elements(nums):
    # 方法一：直接使用 Counter
    count = Counter(nums)

    # 方法二：手動計數
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    return count

# 字符頻率比較
def compare_frequencies(s1, s2):
    return Counter(s1) == Counter(s2)
```

### 2. 快速查找模板

```python
# Two Sum 模式
def find_pair(nums, target):
    seen = {}  # val -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# 重複元素檢查
def has_duplicate(nums):
    return len(set(nums)) < len(nums)
```

### 3. 滑動視窗模板

```python
# 一般滑動視窗
def sliding_window(s):
    window = {}
    left = right = 0
    result = 0

    while right < len(s):
        # 擴展視窗
        c = s[right]
        window[c] = window.get(c, 0) + 1
        right += 1

        # 收縮視窗
        while (need_shrink):
            d = s[left]
            window[d] -= 1
            if window[d] == 0:
                del window[d]
            left += 1

        # 更新結果
        result = max(result, right - left)
    return result

# 固定大小視窗
def fixed_window(s, k):
    window = {}
    for i in range(k):
        window[s[i]] = window.get(s[i], 0) + 1

    result = []
    for i in range(k, len(s)):
        # 檢查當前視窗
        if is_valid(window):
            result.append(i - k)

        # 滑動視窗
        window[s[i]] = window.get(s[i], 0) + 1
        window[s[i-k]] -= 1
        if window[s[i-k]] == 0:
            del window[s[i-k]]
    return result
```

### 4. 前綴和模板

```python
# 子陣列和
def subarray_sum(nums, k):
    prefix_sum = 0
    sum_count = {0: 1}  # 前綴和 -> 出現次數
    count = 0

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    return count
```

## 學習建議

### 1. 學習順序

1. 第一週：計數統計基礎 (242, 383)
2. 第二週：快速查找應用 (1, 217)
3. 第三週：滑動視窗基礎 (3)
4. 第四週：滑動視窗進階 (438)
5. 第五週：前綴和應用 (560)

### 2. 學習方法

1. 先理解基本概念和使用場景
2. 從簡單題目開始，掌握基本模板
3. 練習不同變體，理解使用條件
4. 注意效能優化和邊界處理

### 3. 進階建議

1. 嘗試結合多種技巧解題
2. 關注空間複雜度的優化
3. 練習處理特殊情況和邊界條件
