# 回溯演算法技巧與 LeetCode 學習清單

## 基本解題技巧

### 1. 回溯演算法的基本概念

- 使用時機：
  - 需要列舉所有可能的解
  - 需要找出符合特定條件的組合
  - 需要在決策樹中尋找可行解
- 實作重點：
  - 定義清楚的結束條件
  - 設計有效的狀態記錄
  - 正確實作「選擇」與「撤銷」
  - 善用剪枝優化效能

### 2. 回溯算法模板

#### 基本模板

```python
def backtrack(選擇列表, 路徑):
    if 滿足結束條件:
        result.append(路徑.copy())  # 重要：要做深拷貝
        return

    for 選擇 in 選擇列表:
        if 不合法:
            continue

        做選擇
        路徑.append(選擇)
        backtrack(選擇列表, 路徑)
        路徑.pop()  # 撤銷選擇
```

#### 常見變體

##### 1. 組合問題模板

```python
def combination(n, k, start, path):
    if len(path) == k:
        result.append(path[:])
        return

    for i in range(start, n + 1):
        path.append(i)
        combination(n, k, i + 1, path)  # 從 i + 1 開始，避免重複
        path.pop()
```

##### 2. 排列問題模板

```python
def permutation(nums, path, used):
    if len(path) == len(nums):
        result.append(path[:])
        return

    for i in range(len(nums)):
        if used[i]:
            continue

        used[i] = True
        path.append(nums[i])
        permutation(nums, path, used)
        path.pop()
        used[i] = False
```

### 3. 回溯優化技巧

#### 剪枝策略

##### 1. 可行性剪枝

- 概念：提前判斷當前路徑是否可能產生有效解
- 實作範例：

```python
def subset_sum(nums, target, path, current_sum, start):
    if current_sum > target:  # 可行性剪枝
        return
    if current_sum == target:
        result.append(path[:])
        return

    for i in range(start, len(nums)):
        path.append(nums[i])
        subset_sum(nums, target, path, current_sum + nums[i], i + 1)
        path.pop()
```

##### 2. 重複元素剪枝

- 概念：避免產生重複的組合或排列
- 實作範例：

```python
def combination_with_duplicates(nums, start, path):
    result.append(path[:])

    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i-1]:  # 跳過重複元素
            continue

        path.append(nums[i])
        combination_with_duplicates(nums, i + 1, path)
        path.pop()
```

##### 3. 排序優化

- 概念：通過預先排序來優化剪枝效果
- 實作範例：

```python
def combination_sum(candidates, target, path, start):
    if target < 0:
        return
    if target == 0:
        result.append(path[:])
        return

    for i in range(start, len(candidates)):
        if candidates[i] > target:  # 因為已排序，後面的都不需要嘗試
            break

        path.append(candidates[i])
        combination_sum(candidates, target - candidates[i], path, i)
        path.pop()
```

## 練習題目

### 1. 基礎回溯練習（由易到難）

1. [77. Combinations](https://leetcode.com/problems/combinations/) (Medium)

   - 核心技巧：基本組合回溯
   - 時間複雜度：O(C(n,k))
   - 空間複雜度：O(k)
   - 學習重點：
     - 基本回溯框架的應用
     - 組合問題的處理
     - 避免重複組合的技巧

2. [46. Permutations](https://leetcode.com/problems/permutations/) (Medium)

   - 核心技巧：基本排列回溯
   - 時間複雜度：O(n!)
   - 空間複雜度：O(n)
   - 學習重點：
     - 排列問題的實現
     - 已使用元素的標記
     - 狀態恢復的處理

3. [78. Subsets](https://leetcode.com/problems/subsets/) (Medium)
   - 核心技巧：子集生成
   - 時間複雜度：O(2^n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 子集問題的思考
     - 選擇與不選擇的處理
     - 結果收集的時機

### 2. 進階回溯練習

1. [39. Combination Sum](https://leetcode.com/problems/combination-sum/) (Medium)

   - 核心技巧：無限重複選擇
   - 時間複雜度：O(n^(target/min))
   - 空間複雜度：O(target/min)
   - 學習重點：
     - 可重複選擇的處理
     - 和為目標值的組合
     - 剪枝優化

2. [51. N-Queens](https://leetcode.com/problems/n-queens/) (Hard)

   - 核心技巧：約束滿足問題
   - 時間複雜度：O(n!)
   - 空間複雜度：O(n)
   - 學習重點：
     - 棋盤狀態的表示
     - 有效性檢查
     - 解的表示方法

3. [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) (Hard)
   - 核心技巧：數獨求解
   - 時間複雜度：O(9^m)，m 為空格數
   - 空間複雜度：O(1)
   - 學習重點：
     - 狀態檢查的優化
     - 多重約束的處理
     - 提前剪枝的技巧

### 3. 特殊回溯練習

1. [93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/) (Medium)

   - 核心技巧：字符串分割
   - 時間複雜度：O(1)
   - 空間複雜度：O(1)
   - 學習重點：
     - IP 地址的驗證
     - 分段處理
     - 邊界條件的處理

2. [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) (Medium)

   - 核心技巧：字符串分割與回文判斷
   - 時間複雜度：O(n \* 2^n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 回文串的判斷
     - 動態規劃優化
     - 結果收集的處理

3. [47. Permutations II](https://leetcode.com/problems/permutations-ii/) (Medium)
   - 核心技巧：重複元素的排列
   - 時間複雜度：O(n!)
   - 空間複雜度：O(n)
   - 學習重點：
     - 重複元素的處理
     - 排序與剪枝
     - 去重技巧的應用
