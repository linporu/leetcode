# 迭代解題技巧與 LeetCode 學習清單

## 基本解題技巧

### 1. 迭代的基本概念

- 使用時機：
  - 問題可以通過重複性的步驟解決
  - 需要明確的循環控制
  - 需要優化空間複雜度（相比遞迴）
  - 避免堆疊溢出問題
- 實作重點：
  - 設計清晰的循環條件
  - 正確維護迭代狀態
  - 確保循環終止
  - 注意邊界條件處理

### 2. 迭代的思考模式

#### 直接迭代（Direct Iteration）

- 特點：
  - 使用簡單的 for/while 循環
  - 狀態更新明確直觀
  - 適合線性處理問題
- 實作模板：

```python
def direct_iteration(data):
    # 1. 初始化
    result = initial_value

    # 2. 迭代處理
    for item in data:
        # 更新狀態
        result = process(result, item)

    # 3. 返回結果
    return result
```

#### 雙指針迭代（Two Pointers）

- 特點：
  - 使用兩個或多個指針
  - 通常用於陣列或鏈結串列
  - 適合區間處理或搜尋
- 實作模板：

```python
def two_pointers(data):
    # 1. 初始化指針
    left, right = 0, len(data) - 1

    # 2. 迭代處理
    while left < right:
        # 根據條件移動指針
        if condition(data[left], data[right]):
            left += 1
        else:
            right -= 1

    # 3. 返回結果
    return result
```

#### 堆疊迭代（Stack Iteration）

- 特點：
  - 使用堆疊模擬遞迴
  - 自行管理處理順序
  - 適合樹形結構遍歷
- 實作模板：

```python
def stack_iteration(root):
    # 1. 初始化堆疊
    stack = [root]
    result = []

    # 2. 迭代處理
    while stack:
        # 取出並處理當前節點
        node = stack.pop()
        result.append(node.val)

        # 加入子節點（根據需求調整順序）
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    # 3. 返回結果
    return result
```

### 3. 迭代優化技巧

#### 狀態管理優化

- 使用時機：
  - 需要追蹤多個狀態
  - 狀態轉換複雜
  - 需要優化空間使用
- 實作重點：
  - 選擇合適的資料結構
  - 最小化狀態資訊
  - 適時清理無用狀態
- 實作模板：

```python
def optimized_state_iteration(data):
    # 1. 初始化狀態
    state = initialize_state()

    # 2. 迭代處理
    for item in data:
        # 更新狀態
        new_state = update_state(state, item)

        # 優化狀態（移除不需要的資訊）
        state = optimize_state(new_state)

    # 3. 返回結果
    return process_final_state(state)
```

#### 循環優化

- 特點：
  - 減少不必要的迭代
  - 提前終止條件
  - 跳躍式迭代
- 實作重點：
  - 設計高效的終止條件
  - 識別可以跳過的情況
  - 合理使用 break/continue
- 實作模板：

```python
def optimized_loop_iteration(data):
    # 1. 初始化
    result = initial_value

    # 2. 優化的迭代
    i = 0
    while i < len(data):
        # 提前終止檢查
        if early_termination_condition():
            break

        # 跳躍條件檢查
        if skip_condition():
            i = next_valid_position()
            continue

        # 正常處理
        result = process(result, data[i])
        i += 1

    # 3. 返回結果
    return result
```

## 練習題目

### 1. 基礎迭代練習（由易到難）

1. [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) (Easy)

   - 核心技巧：狀態迭代
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 狀態轉換的實現
     - 空間優化技巧
     - 與遞迴解法的比較

2. [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (Easy)

   - 核心技巧：指針迭代
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 指針操作技巧
     - 迭代版本的空間優勢
     - 狀態追蹤方法

3. [344. Reverse String](https://leetcode.com/problems/reverse-string/) (Easy)
   - 核心技巧：雙指針迭代
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)
   - 學習重點：
     - 雙指針技巧應用
     - 原地修改陣列
     - 邊界條件處理

### 2. 進階迭代練習

1. [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) (Medium)

   - 核心技巧：堆疊迭代
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)，h 為樹高
   - 學習重點：
     - 使用堆疊模擬遞迴
     - 樹的迭代遍歷
     - 空間優化技巧

2. [46. Permutations](https://leetcode.com/problems/permutations/) (Medium)

   - 核心技巧：狀態迭代
   - 時間複雜度：O(n!)
   - 空間複雜度：O(n)
   - 學習重點：
     - 排列生成的迭代實現
     - 狀態管理技巧
     - 結果收集方法

3. [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) (Medium)
   - 核心技巧：堆疊迭代
   - 時間複雜度：O(4^n / sqrt(n))
   - 空間複雜度：O(n)
   - 學習重點：
     - 使用堆疊追蹤狀態
     - 有效狀態的生成
     - 結果的組合方式

### 3. 複雜迭代練習

1. [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) (Medium)

   - 核心技巧：堆疊迭代 + 範圍檢查
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - BST 的迭代驗證
     - 範圍資訊的維護
     - 最優化實現方式

2. [133. Clone Graph](https://leetcode.com/problems/clone-graph/) (Medium)

   - 核心技巧：BFS/DFS 迭代
   - 時間複雜度：O(V + E)
   - 空間複雜度：O(V)
   - 學習重點：
     - 圖的迭代遍歷
     - 節點複製與對應關係
     - 循環檢測處理

3. [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) (Medium)
   - 核心技巧：堆疊迭代 + 路徑追蹤
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - 路徑追蹤技巧
     - 最近公共祖先的迭代查找
     - 狀態回溯的處理

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
