# 動態規劃解題技巧與 LeetCode 學習清單

## 1. 動態規劃核心概念

### 什麼是動態規劃

動態規劃 (Dynamic Programming, DP) 是一種通過**分解問題為子問題**並**避免重複計算**來解決最優化問題的演算法思想。

**核心特徵：**
- **最優子結構**：大問題的最優解包含子問題的最優解
- **重疊子問題**：相同的子問題會被多次計算
- **無後效性**：當前狀態的選擇不會影響之前已確定的狀態

### 兩種實作方法

| 特點 | Bottom-Up (自底向上) | Top-Down (自頂向下) |
|------|---------------------|-------------------|
| **思維方式** | 逐步建構最優解 | 從大問題分解 |
| **實現方式** | 迭代 + DP 表格 | 遞歸 + 記憶化 |
| **計算方向** | 從最小子問題開始 | 從目標問題開始 |
| **空間使用** | 計算所有狀態 | 只計算需要的狀態 |
| **執行效率** | 通常更高效 | 可能有遞歸開銷 |
| **理解難度** | 需要分析依賴關係 | 更接近問題本質 |

---

## 2. Bottom-Up DP (自底向上)

### 核心思維

**「逐步決策」思維：** 想像你從頭開始遍歷問題，在每個決策點上，基於「已知的最佳結果」做出當前最優選擇。

**為什麼這樣思考？**
- 利用電腦「線性處理」的優勢
- 每次只處理一個決策點，避免指數級複雜度
- 通過 dp 陣列「記住」之前的最佳結果

### 實作步驟

#### 1. 狀態定義
```
定義 dp[i] 的明確含義（例如：考慮前 i+1 個元素的最優解）
```

#### 2. 找出狀態轉移方程
```
分析在第 i 個位置上有哪些選擇，每種選擇如何影響結果
dp[i] = f(dp[i-1], dp[i-2], ..., nums[i])
```

#### 3. 初始化 DP 陣列
```python
# 🚨 關鍵步驟：必須正確初始化基礎值
dp = [0] * n
dp[0] = 初始值  # 只考慮第一個元素的情況
dp[1] = 初始值  # 考慮前兩個元素的情況
```

#### 4. 確定遍歷順序
```python
# 通常從小到大計算
for i in range(2, n):  # 從第3個元素開始
    dp[i] = 狀態轉移方程
```

#### 5. 返回最終答案
```python
return dp[n-1]  # 或根據問題需求返回
```

### 基礎模版

```python
def bottom_up_dp(nums):
    n = len(nums)
    
    # 處理邊界情況
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])  # 根據問題調整
    
    # 初始化 DP 陣列
    dp = [0] * n
    dp[0] = nums[0]  # 🚨 必須設置！
    dp[1] = max(nums[0], nums[1])  # 🚨 必須設置！
    
    # 狀態轉移
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])  # 根據問題調整
    
    return dp[n-1]
```

### 常見錯誤與避免方法

#### ❌ 錯誤 1：忘記初始化 DP 陣列
```python
# 錯誤：創建全零陣列但不設初值
dp = [0] * n
for i in range(2, n):  # dp[0], dp[1] 仍然是 0！
    dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

**✅ 正確做法：**
```python
dp = [0] * n
dp[0] = nums[0]  # 明確設置基礎值
dp[1] = max(nums[0], nums[1])  # 明確設置基礎值
```

#### ❌ 錯誤 2：邊界條件處理不當
```python
# 錯誤：沒有處理 n=1, n=2 的情況
def rob(nums):
    dp = [0] * len(nums)  # 如果 nums=[5]，會出錯
    dp[1] = max(nums[0], nums[1])  # IndexError!
```

**✅ 正確做法：**
```python
def rob(nums):
    n = len(nums)
    if n == 1: return nums[0]  # 先處理特殊情況
    if n == 2: return max(nums[0], nums[1])
    # 然後處理一般情況
```

#### ❌ 錯誤 3：狀態轉移方程錯誤
```python
# 錯誤：只考慮當前值，忽略累積效果
dp[i] = max(dp[i-1], nums[i])  # 應該是 dp[i-2] + nums[i]
```

---

## 3. Top-Down DP (記憶化搜索)

### 核心思維

**「分解問題」思維：** 從目標問題開始，遞歸地分解成更小的子問題，並通過記憶化避免重複計算。

**適用場景：**
- 遞歸結構清晰的問題
- 子問題重疊明顯
- 不需要考慮計算順序
- 只需要計算部分狀態

### 實作步驟

#### 1. 定義遞歸函數
```python
def solve(參數):
    # solve(i) 的明確含義（例如：從位置 i 開始的最優解）
```

#### 2. 檢查記憶化
```python
if 參數 in memo:
    return memo[參數]
```

#### 3. 設定終止條件 (Base Cases)
```python
if 終止條件:
    return 基礎值
```

#### 4. 遞歸計算並存入記憶化
```python
result = 根據子問題計算結果
memo[參數] = result  # 🚨 關鍵步驟：必須存入！
return result
```

### 基礎模版

#### 方法一：手動記憶化
```python
def top_down_dp(nums):
    n = len(nums)
    memo = {}
    
    def solve(i):
        # 檢查記憶化
        if i in memo:
            return memo[i]
        
        # 終止條件
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        
        # 遞歸計算
        result = max(solve(i-1), solve(i-2) + nums[i])
        
        # 🚨 存入記憶化
        memo[i] = result
        return result
    
    return solve(n-1)
```

#### 方法二：裝飾器記憶化
```python
from functools import cache

def top_down_dp(nums):
    n = len(nums)
    
    @cache
    def solve(i):
        # 終止條件
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        
        # 遞歸計算（自動記憶化）
        return max(solve(i-1), solve(i-2) + nums[i])
    
    return solve(n-1)
```

### 常見錯誤與避免方法

#### ❌ 錯誤 1：忘記存入記憶化
```python
def solve(i):
    if i in memo:
        return memo[i]
    
    result = max(solve(i-1), solve(i-2) + nums[i])
    # 忘記這行！memo[i] = result
    return result  # 導致重複計算，TLE
```

**✅ 正確做法：**
```python
result = max(solve(i-1), solve(i-2) + nums[i])
memo[i] = result  # 必須存入
return result
```

#### ❌ 錯誤 2：終止條件錯誤
```python
# 錯誤：邊界值不正確
def solve(i):
    if i == 0:
        return nums[1]  # 應該是 nums[0]
    if i == 1:
        return max(nums[0], nums[1])
```

#### ❌ 錯誤 3：遞歸深度過大
```python
# 對於大數據集，可能導致 RecursionError
# 解決方案：增加遞歸限制或改用 bottom-up
import sys
sys.setrecursionlimit(10000)
```

#### ❌ 錯誤 4：使用可變物件作為快取鍵
```python
# 錯誤：list 不能作為 dict 的 key
memo = {}
def solve(arr, i):  # arr 是 list
    if (arr, i) in memo:  # TypeError!
        return memo[(arr, i)]
```

**✅ 正確做法：**
```python
# 只用不可變的參數作為 key
def solve(i):  # 只傳遞 index
    if i in memo:
        return memo[i]
```

---

## 4. 兩種方法的選擇與對比

### 何時選擇 Bottom-Up？

✅ **推薦使用場景：**
- 需要計算所有子問題的解
- 對空間和時間效率要求較高
- 狀態轉移順序明確
- 容易進行空間優化（滾動陣列）

### 何時選擇 Top-Down？

✅ **推薦使用場景：**
- 遞歸關係清晰直觀
- 只需要部分子問題的解
- 複雜的狀態轉移（如多維狀態）
- 快速原型設計和調試

### 實作複雜度對比

| 複雜度類型 | Bottom-Up | Top-Down |
|-----------|-----------|----------|
| 思考難度 | 需要分析依賴關係 | 直觀的問題分解 |
| 代碼複雜度 | 需要正確的初始化和順序 | 需要正確的終止條件 |
| 調試難度 | 逐步追蹤狀態變化 | 遞歸調用棧追蹤 |
| 優化難度 | 容易進行空間優化 | 較難優化遞歸開銷 |

---

## 5. 解題思維框架

### 識別 DP 問題的信號

🔍 **問題特徵：**
- 要求最優解（最大、最小、最多、最少）
- 具有最優子結構性質
- 存在重疊子問題
- 涉及計數或組合問題
- 出現「選擇/不選擇」的決策

### 解題步驟框架

#### 第一步：問題分析
- [ ] 理解題意，確認是否為 DP 問題
- [ ] 識別決策點和約束條件
- [ ] 分析最優子結構性質

#### 第二步：狀態設計
- [ ] 選擇 Top-Down 或 Bottom-Up 方法
- [ ] 定義狀態含義（`dp[i]` 或 `solve(i)` 代表什麼）
- [ ] 確定狀態維度（一維、二維、多維）

#### 第三步：轉移方程
- [ ] 分析在每個狀態下有哪些選擇
- [ ] 寫出狀態轉移方程
- [ ] 驗證轉移方程的邏輯正確性

#### 第四步：邊界條件
- [ ] 確定終止條件或初始狀態
- [ ] 處理特殊情況（空數組、單元素等）
- [ ] 驗證邊界條件的正確性

#### 第五步：實現與優化
- [ ] 選擇合適的數據結構
- [ ] 考慮空間和時間優化
- [ ] 處理潛在的邊界錯誤

#### 第六步：測試驗證
- [ ] 手動追蹤小規模例子
- [ ] 測試邊界情況
- [ ] 分析時間和空間複雜度

---

## 6. 動態規劃題型分類

### 6.1 一維動態規劃

**特徵：** 問題狀態只依賴於一個變數，通常是位置或索引。

**使用時機：**
- 序列、數組的最優化問題
- 當前狀態只依賴於前面的狀態
- 涉及選擇/不選擇的決策

**實作重點：**
- 正確定義 `dp[i]` 的含義
- 找出狀態轉移方程
- 處理初始條件和邊界情況
- 考慮空間優化（滾動數組）

**經典模式：**
```python
# 基本模式
dp[i] = max/min(dp[i-1] + choice1, dp[i-2] + choice2, ...)

# 空間優化版本
prev2, prev1 = base1, base2
for i in range(2, n):
    current = max/min(prev1 + choice1, prev2 + choice2)
    prev2, prev1 = prev1, current
```

### 6.2 二維動態規劃

**特徵：** 需要記錄二維狀態信息，通常涉及兩個序列或二維網格。

**使用時機：**
- 兩個序列的配對、比較問題
- 二維網格的路徑問題
- 需要記錄位置和狀態的複合信息

**實作重點：**
- 定義 `dp[i][j]` 的含義
- 分析狀態間的依賴關係
- 正確處理邊界條件
- 考慮狀態壓縮的可能性

**經典模式：**
```python
# 基本模式
for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j] = f(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

# 空間優化：只保留兩行
prev_row = [0] * (n+1)
curr_row = [0] * (n+1)
```

### 6.3 背包問題

**特徵：** 在資源有限的條件下，選擇物品以達到最優效果。

**使用時機：**
- 資源有限的最優化問題
- 選擇/不選擇的決策問題
- 組合優化問題

**類型與模式：**

#### 01背包（每個物品只能選一次）
```python
for i in range(1, n+1):
    for w in range(W, weight[i]-1, -1):  # 逆序遍歷
        dp[w] = max(dp[w], dp[w-weight[i]] + value[i])
```

#### 完全背包（每個物品可以選無限次）
```python
for i in range(1, n+1):
    for w in range(weight[i], W+1):  # 正序遍歷
        dp[w] = max(dp[w], dp[w-weight[i]] + value[i])
```

### 6.4 區間動態規劃

**特徵：** 在區間上進行合併操作，求解最優方案。

**使用時機：**
- 涉及區間合併的問題
- 字符串切割、矩陣連乘等問題
- 需要考慮子區間最優解的問題

**實作重點：**
- 區間長度由小到大遍歷
- 狀態定義：`dp[i][j]` 表示區間 `[i,j]` 的最優解
- 枚舉分割點求最優
- 注意區間邊界的處理

**經典模式：**
```python
# 按區間長度遍歷
for length in range(2, n+1):  # 區間長度從2開始
    for i in range(n-length+1):
        j = i + length - 1
        for k in range(i, j):  # 枚舉分割點
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + cost)
```

### 6.5 樹形動態規劃

**特徵：** 在樹結構上進行動態規劃，通常涉及節點的選擇/不選擇。

**使用時機：**
- 樹結構上的最優化問題
- 節點選擇/不選擇的決策
- 樹的路徑、子樹相關問題

**實作重點：**
- 定義節點狀態（選擇/不選擇）
- 自底向上計算（後序遍歷）
- 處理根節點的特殊情況
- 考慮樹的重心分解

**經典模式：**
```python
def tree_dp(node):
    if not node:
        return 0, 0  # (選擇當前節點, 不選擇當前節點)
    
    select_current = node.val
    not_select_current = 0
    
    for child in node.children:
        child_select, child_not_select = tree_dp(child)
        select_current += child_not_select  # 選擇父節點，不能選子節點
        not_select_current += max(child_select, child_not_select)  # 不選父節點，子節點可選可不選
    
    return select_current, not_select_current
```

### 6.6 狀態壓縮動態規劃

**特徵：** 使用位元遮罩表示狀態，通常用於集合的子集枚舉。

**使用時機：**
- 集合的子集枚舉問題
- 狀態數量較小（通常 ≤ 20）
- 排列組合的最優化問題

**實作重點：**
- 用位元遮罩表示狀態
- 位元運算的熟練應用
- 狀態轉移的正確性
- 時間和空間複雜度分析

**經典模式：**
```python
# 遍歷所有狀態
for mask in range(1 << n):
    if valid(mask):  # 檢查狀態是否有效
        for i in range(n):
            if mask & (1 << i):  # 檢查第i位是否為1
                new_mask = mask ^ (1 << i)  # 翻轉第i位
                dp[mask] = min(dp[mask], dp[new_mask] + cost[i])
```

---

## 7. 練習題庫

### 7.1 基礎一維 DP（建議先練習）

#### 入門級 (Easy)
1. **[70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)**
   - 核心技巧：基礎遞推關係
   - 複雜度：Time O(n), Space O(1)
   - 學習重點：DP 思維建立、空間優化

2. **[746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)**
   - 核心技巧：最小成本路徑
   - 複雜度：Time O(n), Space O(1)
   - 學習重點：起始條件設定、狀態轉移選擇

#### 進階級 (Medium)
3. **[198. House Robber](https://leetcode.com/problems/house-robber/)**
   - 核心技巧：選擇/不選擇決策
   - 複雜度：Time O(n), Space O(1)
   - 學習重點：相鄰限制條件處理、滾動數組優化

4. **[300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)**
   - 核心技巧：LIS 問題
   - 複雜度：Time O(n²) 或 O(n log n), Space O(n)
   - 學習重點：子序列問題、二分搜尋優化

### 7.2 二維 DP 練習

#### 路徑問題
1. **[62. Unique Paths](https://leetcode.com/problems/unique-paths/)**
   - 核心技巧：網格路徑計數
   - 複雜度：Time O(m×n), Space O(n)
   - 學習重點：二維狀態定義、空間優化

2. **[64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)**
   - 核心技巧：網格最短路徑
   - 複雜度：Time O(m×n), Space O(n)
   - 學習重點：最優路徑選擇、原地修改技巧

#### 字符串問題
3. **[1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)**
   - 核心技巧：LCS 問題
   - 複雜度：Time O(m×n), Space O(min(m,n))
   - 學習重點：雙序列 DP、字符匹配處理

4. **[72. Edit Distance](https://leetcode.com/problems/edit-distance/)**
   - 核心技巧：編輯距離
   - 複雜度：Time O(m×n), Space O(min(m,n))
   - 學習重點：多操作綜合考慮、狀態轉移複雜性

### 7.3 背包問題練習

1. **[416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)**
   - 核心技巧：01背包變形
   - 複雜度：Time O(n×sum), Space O(sum)
   - 學習重點：背包問題識別、布林 DP 應用

2. **[322. Coin Change](https://leetcode.com/problems/coin-change/)**
   - 核心技巧：完全背包
   - 複雜度：Time O(amount×n), Space O(amount)
   - 學習重點：無限使用背包、不可達狀態處理

3. **[518. Coin Change 2](https://leetcode.com/problems/coin-change-2/)**
   - 核心技巧：完全背包計數
   - 複雜度：Time O(amount×n), Space O(amount)
   - 學習重點：組合數計算、順序與組合區別

### 7.4 區間 DP 練習

1. **[516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)**
   - 核心技巧：區間回文子序列
   - 複雜度：Time O(n²), Space O(n²)
   - 學習重點：區間 DP 基本模式、回文性質利用

2. **[5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)**
   - 核心技巧：回文子字符串
   - 複雜度：Time O(n²), Space O(1)
   - 學習重點：中心擴展法、子串與子序列區別

3. **[312. Burst Balloons](https://leetcode.com/problems/burst-balloons/)** (Hard)
   - 核心技巧：區間最優分割
   - 複雜度：Time O(n³), Space O(n²)
   - 學習重點：逆向思維應用、虛擬邊界設置

### 7.5 記憶化搜索練習

1. **[509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)**
   - 核心技巧：基礎記憶化
   - 複雜度：Time O(n), Space O(n)
   - 學習重點：記憶化基本概念、@lru_cache 使用

2. **[329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)** (Hard)
   - 核心技巧：二維記憶化搜索
   - 複雜度：Time O(m×n), Space O(m×n)
   - 學習重點：多維狀態記憶化、DFS + 記憶化結合

### 7.6 樹形 DP 練習

1. **[337. House Robber III](https://leetcode.com/problems/house-robber-iii/)**
   - 核心技巧：樹上選擇問題
   - 複雜度：Time O(n), Space O(h)
   - 學習重點：線性到樹形轉換、節點狀態定義

2. **[124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)** (Hard)
   - 核心技巧：樹形路徑問題
   - 複雜度：Time O(n), Space O(h)
   - 學習重點：路徑定義理解、全局最優維護

### 7.7 狀態壓縮 DP 練習

1. **[338. Counting Bits](https://leetcode.com/problems/counting-bits/)**
   - 核心技巧：位運算 DP
   - 複雜度：Time O(n), Space O(1)
   - 學習重點：位運算性質、Brian Kernighan 算法

2. **[1986. Minimum Number of Work Sessions to Finish the Tasks](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/)**
   - 核心技巧：子集枚舉
   - 複雜度：Time O(3^n), Space O(2^n)
   - 學習重點：狀態壓縮應用、子集枚舉技巧

---

## 8. 學習建議與調試技巧

### 調試技巧

#### Bottom-Up DP 調試
1. **打印 DP 表格**
```python
# 添加調試輸出
for i in range(n):
    print(f"dp[{i}] = {dp[i]}")
```

2. **手動追蹤小例子**
- 用簡單例子（如 nums=[2,7,9]）逐步計算
- 驗證每一步的狀態轉移是否正確

3. **檢查邊界條件**
- 測試 n=1, n=2 的情況
- 確保不會出現 IndexError

#### Top-Down DP 調試
1. **添加遞歸追蹤**
```python
def solve(i, depth=0):
    print("  " * depth + f"solve({i})")
    # 遞歸邏輯
    result = ...
    print("  " * depth + f"solve({i}) = {result}")
    return result
```

2. **檢查記憶化狀態**
```python
# 在函數結束前打印 memo
print(f"memo: {memo}")
```

### 常見問題排查清單

- [ ] DP 陣列是否正確初始化？
- [ ] 邊界條件是否處理完整？
- [ ] 狀態轉移方程是否正確？
- [ ] 記憶化是否正確存儲和檢索？
- [ ] 遞歸終止條件是否正確？
- [ ] 參數範圍是否有效？
- [ ] 時間和空間複雜度是否合理？

透過系統性的學習和練習，你將能夠熟練掌握動態規劃的精髓，並在 LeetCode 中取得優異成績！