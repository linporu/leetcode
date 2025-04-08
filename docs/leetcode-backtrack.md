# 回溯演算法技巧與 LeetCode 學習清單

## 基本解題技巧

### 1. 回溯演算法的基本概念

- 回溯算法本質上是在一棵多叉樹 (N-ary Tree) 上進行 DFS，在窮舉過程中透過 pruning 加速效率的問題解決方式。

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

#### 遞迴式模板

```python
def backtrack_recursive(choices, path=None):
    """遞迴式回溯算法的通用模板

    Args:
        choices: 當前可用的選擇集合
        path: 當前路徑，預設為 None（初始呼叫時為空列表）

    Returns:
        list: 所有可能的解的列表
    """
    # 初始化路徑
    if path is None:
        path = []

    # 檢查是否達到目標
    if 滿足結束條件:
        result.append(path.copy())  # 重要：要做深拷貝
        return

    # 遍歷所有可能的選擇
    remaining = set(choices)  # 創建選擇的副本
    for choice in remaining:
        if 不合法:
            continue

        # 做選擇
        path.append(choice)
        new_choices = remaining - {choice}  # 創建新的選擇集合

        # 遞迴
        backtrack_recursive(new_choices, path)

        # 撤銷選擇（回溯）
        path.pop()
```

#### 迭代式模板

迭代式回溯使用堆疊（stack）來模擬遞迴呼叫，可以避免遞迴深度過大時的堆疊溢出問題。

```python
def backtrack_iterative(choices):
    """迭代式回溯算法的通用模板

    Args:
        choices: 初始的選擇集合，可以是任何可迭代的集合類型

    Returns:
        list: 所有可能的解的列表（注意：解的順序可能與遞迴版本不同）
    """
    if not choices:
        return []

    result = []
    # 堆疊項目格式：(current_path, remaining_choices)
    # - current_path: 當前已選擇的路徑
    # - remaining_choices: 剩餘可用的選擇
    stack = [([], set(choices))]

    while stack:
        path, remaining = stack.pop()

        # 檢查是否達到目標
        if 滿足結束條件:
            result.append(path.copy())  # 重要：要做深拷貝
            continue

        # 直接遍歷剩餘的選擇集合
        for choice in remaining:
            # 創建新的路徑和剩餘選擇集合，不要修改原路徑，以免後面壓入堆疊時重置 reference
            new_path = path + [choice]
            new_remaining = remaining - {choice}

            # 將新狀態壓入堆疊
            stack.append((new_path, new_remaining))

    return result
```

主要優點：

1. 避免遞迴調用的開銷
2. 不會有堆疊溢出的風險
3. 在某些情況下執行效率更高
4. 更容易進行狀態的觀察和除錯

使用時機：

1. 當遞迴深度可能很大時
2. 需要更好的狀態控制和觀察時
3. 需要避免堆疊溢出的風險時
4. 問題的狀態轉換較為直觀時

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

迭代式實現：

```python
def subset_sum_iterative(nums, target):
    result = []
    # 堆疊項目：(current_path, current_sum, start)
    stack = [([], 0, 0)]

    while stack:
        path, curr_sum, start = stack.pop()

        # 可行性剪枝
        if curr_sum > target:
            continue

        # 找到目標和
        if curr_sum == target:
            result.append(path[:])
            continue

        # 反向遍歷以保持與遞迴版本相同的順序
        for i in range(len(nums) - 1, start - 1, -1):
            new_sum = curr_sum + nums[i]
            if new_sum <= target:  # 額外的可行性檢查
                stack.append((path + [nums[i]], new_sum, i + 1))

    return result
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

迭代式實現：

```python
def combination_with_duplicates_iterative(nums):
    nums.sort()  # 先排序，以便處理重複元素
    result = []
    # 堆疊項目：(current_path, start)
    stack = [([], 0)]

    while stack:
        path, start = stack.pop()
        result.append(path[:])

        # 反向遍歷以保持與遞迴版本相同的順序
        for i in range(len(nums) - 1, start - 1, -1):
            # 跳過重複元素
            if i > start and nums[i] == nums[i-1]:
                continue

            stack.append((path + [nums[i]], i + 1))

    return result
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

迭代式實現：

```python
def combination_sum_iterative(candidates, target):
    candidates.sort()  # 先排序以便優化
    result = []
    # 堆疊項目：(current_path, remaining_target, start)
    stack = [([], target, 0)]

    while stack:
        path, remain, start = stack.pop()

        # 找到目標和
        if remain == 0:
            result.append(path[:])
            continue

        for i in range(start, len(candidates)):
            if candidates[i] > remain:  # 剪枝：當前數字太大
                break

            new_remain = remain - candidates[i]
            if new_remain >= 0:  # 可行性檢查
                stack.append((path + [candidates[i]], new_remain, i))  # 注意：這裡是 i 而不是 i+1，因為可以重複使用

    return result
```

## 練習題目

### 1. 基礎回溯練習（Easy）

1. [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) (Easy)

   - 核心技巧：樹的前序遍歷
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)，h 為樹高
   - 學習重點：
     - 基本回溯框架的應用
     - 遞迴與迭代的實現
     - 理解回溯的基本概念

2. [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) (Easy)

   - 核心技巧：路徑收集
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - 路徑的追蹤與收集
     - 字串處理技巧
     - 回溯時的狀態維護

3. [112. Path Sum](https://leetcode.com/problems/path-sum/) (Easy)
   - 核心技巧：路徑和檢查
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - 目標值的追蹤
     - 葉節點的判斷
     - 路徑完整性驗證

### 2. 進階回溯練習（Medium）

1. [78. Subsets](https://leetcode.com/problems/subsets/) (Medium)

   - 核心技巧：子集生成
   - 時間複雜度：O(2^n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 子集問題的思考
     - 選擇與不選擇的處理
     - 結果收集的時機

2. [46. Permutations](https://leetcode.com/problems/permutations/) (Medium)

   - 核心技巧：排列生成
   - 時間複雜度：O(n!)
   - 空間複雜度：O(n)
   - 學習重點：
     - 排列問題的實現
     - 已使用元素的標記
     - 狀態恢復的處理

3. [77. Combinations](https://leetcode.com/problems/combinations/) (Medium)

   - 核心技巧：組合生成
   - 時間複雜度：O(C(n,k))
   - 空間複雜度：O(k)
   - 學習重點：
     - 組合問題的處理
     - 避免重複組合的技巧
     - 剪枝優化

4. [39. Combination Sum](https://leetcode.com/problems/combination-sum/) (Medium)

   - 核心技巧：無限重複選擇
   - 時間複雜度：O(n^(target/min))
   - 空間複雜度：O(target/min)
   - 學習重點：
     - 可重複選擇的處理
     - 和為目標值的組合
     - 剪枝優化

5. [93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/) (Medium)

   - 核心技巧：字符串分割
   - 時間複雜度：O(1)
   - 空間複雜度：O(1)
   - 學習重點：
     - IP 地址的驗證
     - 分段處理
     - 邊界條件的處理

6. [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) (Medium)

   - 核心技巧：字符串分割與回文判斷
   - 時間複雜度：O(n \* 2^n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 回文串的判斷
     - 動態規劃優化
     - 結果收集的處理

7. [47. Permutations II](https://leetcode.com/problems/permutations-ii/) (Medium)
   - 核心技巧：重複元素的排列
   - 時間複雜度：O(n!)
   - 空間複雜度：O(n)
   - 學習重點：
     - 重複元素的處理
     - 排序與剪枝
     - 去重技巧的應用

## 附錄

### 常見變體模版

#### 1. 組合問題模板

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

迭代式實現：

```python
def combination_iterative(n, k):
    result = []
    # 堆疊項目：(current_path, start)
    stack = [([], 1)]

    while stack:
        path, start = stack.pop()

        # 找到一個有效組合
        if len(path) == k:
            result.append(path[:])
            continue

        # 注意：反向遍歷以保持與遞迴版本相同的順序
        for i in range(n, start - 1, -1):
            stack.append((path + [i], i + 1))

    return result
```

#### 2. 排列問題模板

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

迭代式實現：

```python
def permutation_iterative(nums):
    if not nums:
        return []

    result = []
    n = len(nums)

    # 堆疊項目：(current_path, used_set)
    stack = [([], set())]

    while stack:
        path, used = stack.pop()

        if len(path) == len(nums):
            result.append(path[:])
            continue

        # 反向遍歷以保持與遞迴版本相同的順序
        for i in range(n - 1, -1, -1):
            if i not in used:
                stack.append((path + [nums[i]], used | {i}))

    return result
```

#### 3. 子集問題模版

```python
def subsets(nums):
    result = []

    def backtrack(start, path):
        # 每個節點都是一個有效的子集
        result.append(path.copy())

        # 從 start 開始，嘗試添加每個剩餘元素（探索每個分支）
        for i in range(start, len(nums)):
            # 選擇一個分支
            path.append(nums[i])

            # 遞迴探索該分支（只考慮當前元素之後的元素，避免重複）
            backtrack(i + 1, path)

            # 回溯，撤銷選擇，準備探索下一個分支
            path.pop()

    backtrack(0, [])
    return result
```

迭代式實現：

```python
def subsets_iterative(nums):
    if not nums:
        return [[]]

    result = []
    # 堆疊項目：(current_path, start_index)
    stack = [([], 0)]

    while stack:
        path, start = stack.pop()

        # 每個路徑都是一個有效的子集
        result.append(path[:])

        # 反向遍歷以保持與遞迴版本相同的順序
        for i in range(len(nums) - 1, start - 1, -1):
            stack.append((path + [nums[i]], i + 1))

    return result
```
