# 遞迴解題技巧與 LeetCode 學習清單

## 基本解題技巧

### 1. 遞迴的基本概念

- 使用時機：
  - 問題可以分解為相同性質的子問題
  - 問題有明確的終止條件（Base Case）
  - 需要自底向上或自頂向下處理
- 實作重點：
  - 設計清晰的遞迴終止條件
  - 確保遞迴參數的正確傳遞
  - 注意遞迴深度和堆疊溢出
  - 避免重複計算（考慮記憶化）

### 2. 遞迴的思考模式

#### 自頂向下（Top-down）

- 特點：
  - 從大問題開始，逐步分解為小問題
  - 通常使用參數傳遞當前狀態
  - 適合需要路徑追蹤的問題
- 實作模板：

```python
def top_down(node, state):
    # 1. 終止條件
    if not node:
        return ...

    # 2. 處理當前層級
    # ... 處理當前節點 ...

    # 3. 遞迴子問題
    left = top_down(node.left, new_state)
    right = top_down(node.right, new_state)

    # 4. 返回結果
    return ...
```

#### 自底向上（Bottom-up）

- 特點：
  - 從最小子問題開始解決
  - 結果由子問題的解構建
  - 適合需要匯總資訊的問題
- 實作模板：

```python
def bottom_up(node):
    # 1. 終止條件
    if not node:
        return ...

    # 2. 遞迴獲取子問題的解
    left = bottom_up(node.left)
    right = bottom_up(node.right)

    # 3. 根據子問題的解構建當前問題的解
    return ...
```

### 3. 遞迴優化技巧

#### 記憶化遞迴（Memoization）

- 使用時機：
  - 存在重複子問題
  - 子問題的解可以被重複使用
- 實作重點：
  - 選擇合適的緩存結構
  - 設計有效的緩存鍵
  - 平衡時間和空間複雜度
- 實作模板：

```python
def memoized_recursion(args):
    def helper(state, memo={}):
        # 1. 檢查是否已有結果
        key = str(state)
        if key in memo:
            return memo[key]

        # 2. 終止條件
        if is_base_case(state):
            return base_value

        # 3. 遞迴求解
        result = ...

        # 4. 儲存並返回結果
        memo[key] = result
        return result

    return helper(initial_state)
```

#### 尾遞迴優化（Tail Recursion）

- 特點：

  - 遞迴調用是函數的最後一個操作
  - 不需要保存中間狀態
  - 可以被編譯器優化為迭代
  - 避免堆疊溢出問題

- 實作重點：

  - 使用參數傳遞狀態（累加器模式）
  - 避免遞迴後的運算
  - 確保遞迴調用是最後一個操作

- 為什麼需要尾遞迴優化：

  1. 堆疊空間優化：
     - 一般遞迴：每次調用都需要保存當前狀態
     - 尾遞迴：可以重用堆疊空間，不需要保存中間狀態
  2. 避免堆疊溢出：
     - 一般遞迴：深度太大時可能溢出
     - 尾遞迴：可被優化為循環，無溢出風險
  3. 執行效率：
     - 一般遞迴：需要保存和恢復狀態
     - 尾遞迴：可以直接重用堆疊空間

- Python 中的應用：

  - Python 預設不支援尾遞迴優化（TCO）
  - 但理解尾遞迴概念有助於：
    1. 在其他支援 TCO 的語言中使用（如 Scala、Haskell）
    2. 寫出更好的遞迴程式
    3. 手動將尾遞迴轉換為迭代版本

- 實際例子 - 斐波那契數列：

```python
# 一般遞迴
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)  # 需要保存兩個遞迴調用的結果

# 尾遞迴版本
def fib(n, a=0, b=1):
    if n == 0:
        return a
    return fib(n - 1, b, a + b)  # 所有狀態都在參數中傳遞

# 對應的迭代版本
def fib_iter(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

- 實作模板：

```python
def tail_recursion(args, acc=None):
    # 1. 終止條件
    if is_base_case(args):
        return acc

    # 2. 計算新的狀態
    new_acc = ...  # 在這裡進行所有必要的計算

    # 3. 尾遞迴調用（確保是最後一個操作）
    return tail_recursion(new_args, new_acc)
```

## 練習題目

### 1. 基礎遞迴練習（由易到難）

1. [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) (Easy)

   - 核心技巧：基本遞迴、記憶化
   - 時間複雜度：O(n)（使用記憶化）
   - 空間複雜度：O(n)
   - 學習重點：
     - 遞迴與記憶化的實現
     - 空間與時間的優化
     - 不同解法的比較

2. [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (Easy)

   - 核心技巧：遞迴反轉
   - 時間複雜度：O(n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 鏈結串列的遞迴操作
     - 遞迴與迭代的轉換
     - 指針操作的技巧

3. [344. Reverse String](https://leetcode.com/problems/reverse-string/) (Easy)
   - 核心技巧：遞迴交換
   - 時間複雜度：O(n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 陣列的遞迴操作
     - 原地修改的實現
     - 遞迴終止條件的設計

### 2. 進階遞迴練習

1. [779. K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/) (Medium)

   - 核心技巧：遞迴模式識別
   - 時間複雜度：O(n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 模式識別與分析
     - 遞迴關係的建立
     - 優化計算過程

2. [95. Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/) (Medium)

   - 核心技巧：遞迴生成樹
   - 時間複雜度：O(4^n / n^(1/2))
   - 空間複雜度：O(4^n / n^(1/2))
   - 學習重點：
     - 樹的遞迴構建
     - 子問題的劃分
     - 結果的組合方式

3. [241. Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/) (Medium)
   - 核心技巧：分治遞迴
   - 時間複雜度：O(2^n)
   - 空間複雜度：O(2^n)
   - 學習重點：
     - 運算式的遞迴解析
     - 結果的組合與計算
     - 記憶化的應用

### 3. 回溯遞迴練習

1. [46. Permutations](https://leetcode.com/problems/permutations/) (Medium)

   - 核心技巧：排列遞迴
   - 時間複雜度：O(n!)
   - 空間複雜度：O(n)
   - 學習重點：
     - 回溯算法的應用
     - 狀態的維護與恢復
     - 結果的收集方式

2. [78. Subsets](https://leetcode.com/problems/subsets/) (Medium)
   - 核心技巧：子集生成
   - 時間複雜度：O(2^n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 組合的遞迴生成
     - 選擇與不選擇的處理
     - 結果的構建方式

## 常見錯誤與解決方案

1. 堆疊溢出（Stack Overflow）

   - 原因：遞迴深度過大
   - 解決方案：
     - 考慮使用迭代方法
     - 實作尾遞迴優化
     - 增加終止條件檢查

2. 重複計算

   - 原因：相同子問題重複求解
   - 解決方案：
     - 使用記憶化遞迴
     - 優化遞迴結構
     - 考慮自底向上的方法

3. 參數傳遞錯誤

   - 原因：狀態沒有正確傳遞或更新
   - 解決方案：
     - 仔細檢查參數更新邏輯
     - 確保狀態的正確複製或修改
     - 使用不可變數據結構

4. 終止條件不完整
   - 原因：沒有覆蓋所有基本情況
   - 解決方案：
     - 全面分析邊界情況
     - 增加防禦性檢查
     - 完善終止條件邏輯

## 遞迴與迭代的比較

### 1. 適用場景比較

#### 遞迴適用場景

- 問題具有自相似性質（Self-similarity）
  - 樹狀結構的遍歷和處理
  - 圖形的深度優先搜索（DFS）
  - 分治算法（如合併排序、快速排序）
- 問題可以被分解為相同性質的子問題
  - 數學遞迴定義（如斐波那契數列）
  - 組合問題（生成排列、組合）
- 代碼邏輯清晰度重要
  - 需要保持代碼的可讀性和維護性
  - 算法的自然表達方式是遞迴的

#### 迭代適用場景

- 線性處理問題
  - 簡單的循環和計數
  - 陣列的順序處理
  - 鏈結串列的操作
- 圖形的廣度優先搜索（BFS）
- 空間效率要求高
  - 避免堆疊溢出風險
  - 需要最小化記憶體使用
- 性能要求嚴格
  - 需要精確控制執行流程
  - 避免函數調用開銷

### 2. 效能比較

#### 時間複雜度

- 遞迴：
  - 優點：邏輯清晰，易於實現複雜算法
  - 缺點：函數調用開銷較大，可能有重複計算
- 迭代：
  - 優點：直接執行，無函數調用開銷
  - 缺點：某些複雜算法實現較困難

#### 空間複雜度

- 遞迴：
  - 需要額外的堆疊空間（與遞迴深度成正比）
  - 可能導致堆疊溢出
  - 記憶化遞迴需要額外的記憶體空間
- 迭代：
  - 通常只需要固定的額外空間
  - 空間使用更可控
  - 不會有堆疊溢出的風險

### 3. 代碼特性比較

#### 可讀性和維護性

- 遞迴：
  - 代碼更簡潔優雅
  - 邏輯結構清晰
  - 更接近問題的數學描述
- 迭代：
  - 代碼可能較冗長
  - 需要手動管理狀態
  - 邏輯可能較難理解

#### 除錯和測試

- 遞迴：
  - 除錯較困難（需要追蹤多層調用）
  - 堆疊追蹤可能很長
  - 邊界情況測試重要
- 迭代：
  - 除錯相對容易（狀態可見）
  - 執行流程清晰
  - 容易進行單步調試

### 4. 實際應用建議

1. 優先考慮迭代的情況：

   - 簡單的循環處理
   - 對性能和記憶體有嚴格要求
   - 問題本質是線性的
   - 需要精確控制執行流程

2. 優先考慮遞迴的情況：

   - 樹或圖的遍歷
   - 需要回溯的問題
   - 分治算法
   - 代碼清晰度重要於性能

3. 混合使用策略：
   - 根據具體問題選擇合適方法
   - 考慮將遞迴轉換為迭代（需要時）
   - 使用尾遞迴優化（如果語言支援）
   - 權衡代碼可讀性和性能需求
