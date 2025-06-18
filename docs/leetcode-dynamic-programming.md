# 動態規劃解題技巧與 LeetCode 學習清單

## 基本解題技巧

### 1. 一維動態規劃 (1D DP)

- 使用時機：
  - 問題具有最優子結構性質
  - 當前狀態只依賴於前面的狀態
  - 涉及序列、陣列的最優化問題
- 實作重點：
  - 定義 dp[i] 的含義
  - 找出狀態轉移方程
  - 確定初始條件和邊界情況
  - 考慮空間優化（滾動陣列）

### 2. 二維動態規劃 (2D DP)

- 使用時機：
  - 涉及兩個序列或二維網格的問題
  - 需要記錄多維狀態資訊
  - 路徑計算、配對問題
- 實作重點：
  - 定義 dp[i][j] 的含義
  - 分析狀態之間的依賴關係
  - 正確處理邊界條件
  - 考慮狀態壓縮的可能性

### 3. 背包問題 (Knapsack Problems)

- 使用時機：
  - 資源有限的最優化問題
  - 選擇/不選擇的決策問題
  - 組合優化問題
- 實作重點：
  - 01背包：每個物品只能選一次
  - 完全背包：每個物品可以選無限次
  - 多重背包：每個物品有限定數量
  - 空間優化技巧

### 4. 區間動態規劃 (Interval DP)

- 使用時機：
  - 涉及區間合併的問題
  - 字符串切割、矩陣連乘等問題
  - 需要考慮子區間最優解的問題
- 實作重點：
  - 區間長度由小到大遍歷
  - 狀態定義：dp[i][j] 表示區間 [i,j] 的最優解
  - 枚舉分割點求最優
  - 注意區間邊界的處理

### 5. 樹形動態規劃 (Tree DP)

- 使用時機：
  - 在樹結構上的最優化問題
  - 節點選擇/不選擇的決策
  - 樹的路徑、子樹相關問題
- 實作重點：
  - 定義節點狀態（選擇/不選擇）
  - 自底向上計算
  - 處理根節點的特殊情況
  - 考慮樹的重心分解

### 6. 狀態壓縮動態規劃 (Bitmask DP)

- 使用時機：
  - 集合的子集枚舉問題
  - 狀態數量較小（通常 ≤ 20）
  - 排列組合的最優化問題
- 實作重點：
  - 用位元遮罩表示狀態
  - 位元運算的熟練應用
  - 狀態轉移的正確性
  - 時間和空間複雜度分析

### 7. 記憶化搜索 (Memoization)

#### 核心概念

記憶化搜索是自頂向下的動態規劃實現方式，通過**遞迴 + 快取**來避免重複計算。

#### 實現方式

1. **遞迴函數設計**
```python
# 基本模式
def dfs(參數列表):
    # 檢查快取
    if 參數 in memo:
        return memo[參數]
    
    # 基本情況
    if 終止條件:
        return 基本值
    
    # 遞迴計算
    result = 根據子問題計算結果
    
    # 儲存到快取
    memo[參數] = result
    return result
```

2. **Python 裝飾器**
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def dfs(參數):
    # 遞迴邏輯
    pass
```

#### 適用場景

- 遞迴結構清晰的問題
- 子問題重疊明顯
- 狀態空間不太大
- 不需要考慮計算順序

#### 記憶化 vs 迭代 DP

| 特點 | 記憶化搜索 | 迭代 DP |
|------|------------|---------|
| 方向 | 自頂向下 | 自底向上 |
| 實現 | 遞迴 + 快取 | 迭代 + 表格 |
| 空間 | 只計算需要的狀態 | 計算所有狀態 |
| 理解 | 更接近問題本質 | 需要分析依賴關係 |
| 效率 | 可能有遞迴開銷 | 通常更高效 |

#### 實作要點

1. **參數設計**
   - 確保參數能唯一標識狀態
   - 避免使用可變物件作為快取鍵
   - 考慮參數的範圍和類型

2. **終止條件**
   - 清晰定義基本情況
   - 避免無限遞迴
   - 正確處理邊界條件

3. **快取策略**
   - 選擇合適的快取容器（dict, lru_cache等）
   - 考慮記憶體使用量
   - 必要時清理快取

4. **狀態轉移**
   - 確保子問題的正確性
   - 避免狀態之間的循環依賴
   - 考慮最優化原則

## 練習題目

### 1. 基礎一維 DP（由易到難）

1. [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (Easy)
   - 核心技巧：基礎遞推關係
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)（優化後）
   - 學習重點：
     - DP 思維的建立
     - 空間優化技巧
     - 斐波那契數列的變形

2. [198. House Robber](https://leetcode.com/problems/house-robber/) (Medium)
   - 核心技巧：選擇/不選擇的決策
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)（優化後）
   - 學習重點：
     - 狀態定義的技巧
     - 相鄰限制條件的處理
     - 滾動陣列優化

3. [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) (Easy)
   - 核心技巧：最小成本路徑
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)（優化後）
   - 學習重點：
     - 起始條件的設定
     - 狀態轉移的選擇
     - 最終答案的確定

4. [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) (Medium)
   - 核心技巧：LIS 問題
   - 時間複雜度：O(n²) 或 O(n log n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 子序列問題的處理
     - 二分搜尋優化
     - 實際序列的重建

### 2. 二維 DP 練習

1. [62. Unique Paths](https://leetcode.com/problems/unique-paths/) (Medium)
   - 核心技巧：網格路徑計數
   - 時間複雜度：O(m×n)
   - 空間複雜度：O(n)（優化後）
   - 學習重點：
     - 二維狀態的定義
     - 邊界條件的處理
     - 空間優化的實現

2. [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) (Medium)
   - 核心技巧：網格最短路徑
   - 時間複雜度：O(m×n)
   - 空間複雜度：O(n)（優化後）
   - 學習重點：
     - 最優路徑的選擇
     - 原地修改技巧
     - 狀態轉移方程

3. [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) (Medium)
   - 核心技巧：LCS 問題
   - 時間複雜度：O(m×n)
   - 空間複雜度：O(min(m,n))（優化後）
   - 學習重點：
     - 雙序列 DP 的經典問題
     - 字符匹配的處理
     - 空間壓縮技巧

4. [72. Edit Distance](https://leetcode.com/problems/edit-distance/) (Hard)
   - 核心技巧：編輯距離
   - 時間複雜度：O(m×n)
   - 空間複雜度：O(min(m,n))（優化後）
   - 學習重點：
     - 多種操作的綜合考慮
     - 狀態轉移的複雜性
     - 實際編輯序列的追蹤

### 3. 背包問題練習

1. [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) (Medium)
   - 核心技巧：01背包變形
   - 時間複雜度：O(n×sum)
   - 空間複雜度：O(sum)
   - 學習重點：
     - 背包問題的識別
     - 布林 DP 的應用
     - 空間優化實現

2. [322. Coin Change](https://leetcode.com/problems/coin-change/) (Medium)
   - 核心技巧：完全背包
   - 時間複雜度：O(amount×n)
   - 空間複雜度：O(amount)
   - 學習重點：
     - 無限使用的背包問題
     - 最少數量的求取
     - 不可達狀態的處理

3. [518. Coin Change 2](https://leetcode.com/problems/coin-change-2/) (Medium)
   - 核心技巧：完全背包計數
   - 時間複雜度：O(amount×n)
   - 空間複雜度：O(amount)
   - 學習重點：
     - 組合數的計算
     - 順序與組合的區別
     - 狀態轉移的正確性

4. [474. Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/) (Medium)
   - 核心技巧：多維背包
   - 時間複雜度：O(l×m×n)，l為字符串數量
   - 空間複雜度：O(m×n)
   - 學習重點：
     - 多約束條件的背包
     - 三維狀態的處理
     - 空間優化的考慮

### 4. 區間 DP 練習

1. [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) (Medium)
   - 核心技巧：區間回文子序列
   - 時間複雜度：O(n²)
   - 空間複雜度：O(n²)
   - 學習重點：
     - 區間 DP 的基本模式
     - 回文性質的利用
     - 狀態轉移的設計

2. [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) (Medium)
   - 核心技巧：回文子字符串
   - 時間複雜度：O(n²)
   - 空間複雜度：O(n²) 或 O(1)
   - 學習重點：
     - 中心擴展法
     - Manacher 算法
     - 子串與子序列的區別

3. [312. Burst Balloons](https://leetcode.com/problems/burst-balloons/) (Hard)
   - 核心技巧：區間最優分割
   - 時間複雜度：O(n³)
   - 空間複雜度：O(n²)
   - 學習重點：
     - 逆向思維的應用
     - 分割點的枚舉
     - 虛擬邊界的設置

### 5. 記憶化搜索練習

1. [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) (Easy)
   - 核心技巧：基礎記憶化
   - 時間複雜度：O(n)
   - 空間複雜度：O(n)
   - 學習重點：
     - 記憶化的基本概念
     - 遞迴到迭代的轉換
     - @lru_cache 裝飾器的使用

2. [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) (Hard)
   - 核心技巧：二維記憶化搜索
   - 時間複雜度：O(m×n)
   - 空間複雜度：O(m×n)
   - 學習重點：
     - 多維狀態的記憶化
     - DFS + 記憶化的結合
     - 拓撲排序的應用

3. [1444. Number of Ways of Cutting a Pizza](https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/) (Hard)
   - 核心技巧：三維記憶化搜索
   - 時間複雜度：O(k×m²×n²)
   - 空間複雜度：O(k×m×n)
   - 學習重點：
     - 複雜狀態的記憶化
     - 前綴和的預處理
     - 剪枝策略的應用

### 6. 狀態壓縮 DP 練習

1. [338. Counting Bits](https://leetcode.com/problems/counting-bits/) (Easy)
   - 核心技巧：位運算 DP
   - 時間複雜度：O(n)
   - 空間複雜度：O(1)（不計結果陣列）
   - 學習重點：
     - 位運算的性質利用
     - 狀態轉移的巧妙性
     - Brian Kernighan 算法

2. [1986. Minimum Number of Work Sessions to Finish the Tasks](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/) (Medium)
   - 核心技巧：子集枚舉
   - 時間複雜度：O(3^n)
   - 空間複雜度：O(2^n)
   - 學習重點：
     - 狀態壓縮的應用
     - 子集的枚舉技巧
     - 時間複雜度的分析

### 7. 樹形 DP 練習

1. [198. House Robber](https://leetcode.com/problems/house-robber/) vs [337. House Robber III](https://leetcode.com/problems/house-robber-iii/) (Medium)
   - 核心技巧：樹上選擇問題
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)，h為樹高
   - 學習重點：
     - 線性到樹形的轉換
     - 節點狀態的定義
     - 後序遍歷的應用

2. [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) (Hard)
   - 核心技巧：樹形路徑問題
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - 路徑定義的理解
     - 全局最優的維護
     - 子樹貢獻的計算

## 學習建議

### 1. 學習順序

1. **第一週：基礎概念建立**
   - 爬樓梯問題 (70)
   - 費用最小爬樓梯 (746)
   - 打家劫舍 (198)

2. **第二週：一維 DP 熟練**
   - 最長遞增子序列 (300)
   - 多種解法比較和優化

3. **第三週：二維 DP 入門**
   - 不同路徑 (62)
   - 最小路徑和 (64)
   - 最長公共子序列 (1143)

4. **第四週：背包問題專項**
   - 分割等和子集 (416)
   - 零錢兌換 (322, 518)

5. **第五週：記憶化搜索**
   - 基礎記憶化練習
   - 與迭代 DP 的對比

6. **第六週：進階主題**
   - 區間 DP (516, 5)
   - 狀態壓縮 DP (338)

7. **第七週：綜合應用**
   - 樹形 DP (337, 124)
   - 複雜問題的分解

### 2. 學習方法

1. **理解問題本質**
   - 識別最優子結構
   - 找出重疊子問題
   - 確定狀態定義

2. **建立解題模式**
   - 狀態定義 → 轉移方程 → 初始條件 → 答案獲取
   - 記憶化：遞迴 → 終止條件 → 狀態轉移 → 快取

3. **實作技巧掌握**
   - 邊界條件的仔細處理
   - 空間和時間複雜度的優化
   - 程式碼的清晰性和可讀性

4. **調試和驗證**
   - 手動追蹤小規模例子
   - 檢查邊界情況
   - 對比不同解法的結果

### 3. 進階建議

1. **深度理解**
   - 從記憶化搜索到迭代 DP 的轉換
   - 不同問題類型的共通模式
   - 複雜度分析的精確性

2. **技巧提升**
   - 狀態壓縮和空間優化
   - 滾動陣列的靈活運用
   - 預處理和後處理的技巧

3. **擴展學習**
   - 線性 DP 到環形 DP
   - 概率 DP 和期望 DP
   - 數位 DP 和計數 DP

4. **實際應用**
   - 理解 DP 在演算法競賽中的地位
   - 學習如何快速識別 DP 問題
   - 培養最優化思維

### 4. 常見陷阱與解決方案

1. **狀態定義不清**
   - 問題：無法正確表達子問題
   - 解決：仔細分析問題的結構，多嘗試不同的狀態定義

2. **邊界條件錯誤**
   - 問題：初始狀態設置不當
   - 解決：手動追蹤最小規模的例子

3. **轉移方程錯誤**
   - 問題：子問題之間的關係不正確
   - 解決：驗證轉移方程的邏輯正確性

4. **空間和時間複雜度**
   - 問題：忽略優化的可能性
   - 解決：學習常見的優化技巧

5. **記憶化實現問題**
   - 問題：快取鍵設計不當、遞迴深度過大
   - 解決：注意參數的不可變性、考慮迭代替代

### 5. 解題思維框架

#### 識別 DP 問題的信號
- 問題要求最優解（最大、最小、最多、最少）
- 具有最優子結構性質
- 存在重疊子問題
- 涉及計數或組合問題

#### 解題步驟
1. **問題分析**：理解題意，識別是否為 DP 問題
2. **狀態設計**：定義 dp[i] 或 dp[i][j] 的含義
3. **轉移方程**：找出狀態之間的關係
4. **邊界條件**：確定初始狀態
5. **實現優化**：考慮空間和時間的優化
6. **驗證測試**：檢查邊界情況和典型例子

#### 記憶化搜索的選擇時機
- 遞迴關係清晰明確
- 不需要考慮狀態的計算順序
- 只需要計算部分狀態
- 問題具有明顯的遞迴結構