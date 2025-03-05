# 樹狀結構解題技巧與 LeetCode 學習清單

## 基本解題技巧

### 1. 樹的遍歷 (Tree Traversal)

- 使用時機：
  - 需要按特定順序訪問樹的節點
  - 需要收集或處理樹中的所有節點
  - 需要在樹中搜索特定值或模式
- 實作重點：
  - 選擇合適的遍歷方式（前序、中序、後序、層序）
  - 遞迴 vs 迭代實現的選擇
  - 空間複雜度的考量

### 2. 遞迴解題 (Recursion)

- 使用時機：
  - 問題可以分解為子問題
  - 需要自底向上或自頂向下處理
  - 樹的結構轉換或比較
- 實作重點：
  - 設計清晰的遞迴終止條件
  - 確保遞迴參數的正確傳遞
  - 注意遞迴深度和堆疊溢出

### 3. 深度與高度計算 (Depth & Height)

- 使用時機：
  - 需要計算樹的深度或高度
  - 需要判斷樹的平衡性
  - 需要處理特定深度的節點
- 實作重點：
  - 深度與高度的區別理解
  - 自頂向下 vs 自底向上的選擇
  - 優化重複計算

### 4. 路徑問題 (Path Problems)

- 使用時機：
  - 尋找特定和的路徑
  - 收集所有可能的路徑
  - 計算最長或最短路徑
- 實作重點：
  - 路徑狀態的維護
  - 回溯的使用
  - 路徑驗證的條件

### 5. 樹的修改與構造 (Tree Modification & Construction)

- 使用時機：
  - 需要修改樹的結構
  - 從其他資料結構構造樹
  - 樹的序列化與反序列化
- 實作重點：
  - 保持樹的特性（如 BST 性質）
  - 處理節點間的連接
  - 考慮邊界情況

### 6. 遞迴轉迭代的思維方式

#### 核心概念

遞迴轉迭代的關鍵在於：**遞迴隱含了系統調用堆疊（call stack），而迭代則是我們手動模擬這個堆疊**。

#### 各種遍歷的思維模式

1. **前序遍歷 (Preorder)**

```python
# 遞迴思維：根 -> 左 -> 右
result.append(node.val)
dfs(node.left)
dfs(node.right)

# 迭代思維：
# 1. 立即處理當前節點
# 2. 確保接下來會先處理左子樹，再處理右子樹
stack.append(right)  # 後進先出，所以右節點先進
stack.append(left)   # 左節點後進，會先被處理
```

2. **中序遍歷 (Inorder)**

```python
# 遞迴思維：左 -> 根 -> 右
dfs(node.left)
result.append(node.val)
dfs(node.right)

# 迭代思維：
# 1. 把所有左子節點壓入堆疊
# 2. 當無法繼續往左時，處理當前節點
# 3. 移動到右子節點，重複步驟1
```

3. **後序遍歷 (Postorder)**

```python
# 遞迴思維：左 -> 右 -> 根
dfs(node.left)
dfs(node.right)
result.append(node.val)

# 迭代思維：
# 1. 使用標記來追蹤節點是否已經處理過右子樹
# 2. 只有在以下情況才處理節點：
#    - 是葉節點
#    - 或已經處理過右子樹
```

#### 迭代解題要點

1. **堆疊的角色**

   - 堆疊用來記錄「待處理」的節點
   - 堆疊的順序決定了處理順序

2. **狀態追蹤**

   - 前序：最簡單，直接處理當前節點
   - 中序：需要追蹤「是否已經到達最左」
   - 後序：需要追蹤「是否已經處理過右子樹」

3. **處理順序設計**
   - 想要先處理什麼，就後放入堆疊
   - 堆疊是 LIFO（後進先出）的特性

#### 解題步驟建議

1. 先理解遞迴版本中的處理順序
2. 思考如何用堆疊模擬這個順序
3. 確定需要追蹤什麼狀態
4. 設計入堆疊的順序來實現期望的處理順序

## 練習題目

### 1. 基礎遍歷練習（由易到難）

1. [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) (Easy)

   - 核心技巧：中序遍歷
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)，h 為樹高
   - 學習重點：
     - 遞迴與迭代的實現
     - Morris 遍歷的概念
     - 空間優化技巧

2. [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) (Easy)

   - 核心技巧：前序遍歷
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - 遞迴到迭代的轉換
     - 堆疊的使用
     - 不同實現方式的比較

3. [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) (Easy)

   - 核心技巧：後序遍歷
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - 後序遍歷的特性
     - 雙堆疊方法
     - 處理遍歷順序

4. [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) (Medium)
   - 核心技巧：層序遍歷
   - 時間複雜度：O(n)
   - 空間複雜度：O(w)，w 為最寬層的節點數
   - 學習重點：
     - 隊列的使用
     - 層級資訊的維護
     - 結果的組織方式

### 2. 遞迴應用練習（由易到難）

1. [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) (Easy)

   - 核心技巧：遞迴轉換
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - 遞迴思維的建立
     - 子樹處理的順序
     - 節點交換的實現

2. [100. Same Tree](https://leetcode.com/problems/same-tree/) (Easy)

   - 核心技巧：同步遞迴
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - 結構比較的方法
     - 終止條件的設計
     - 遞迴的效率

3. [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) (Easy)

   - 核心技巧：對稱遞迴
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - 對稱性的判斷
     - 遞迴參數的設計
     - 迭代解法的實現

4. [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) (Easy)
   - 核心技巧：高度平衡檢查
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - 平衡條件的驗證
     - 高度計算的優化
     - 提前終止的條件

### 3. 路徑問題練習

1. [112. Path Sum](https://leetcode.com/problems/path-sum/) (Easy)

   - 核心技巧：路徑和檢查
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - 目標值的追蹤
     - 葉節點的判斷
     - 路徑完整性驗證

2. [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) (Easy)
   - 核心技巧：路徑收集
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - 路徑字串的構建
     - 回溯的應用
     - 結果格式的處理

### 4. 二元搜尋樹練習

1. [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) (Medium)

   - 核心技巧：BST 性質驗證
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - BST 性質的理解
     - 範圍限制的傳遞
     - 中序遍歷的應用

2. [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) (Easy)
   - 核心技巧：BST 搜尋
   - 時間複雜度：O(h)
   - 空間複雜度：O(1)
   - 學習重點：
     - BST 搜尋特性
     - 迭代實現
     - 效率分析

### 5. N 叉樹練習（N-ary Tree）

#### N 叉樹的特性與挑戰

- **節點結構差異**：每個節點可以有多個子節點，而非僅有左右兩個
- **遍歷方式調整**：需要處理多個子節點的遍歷順序
- **無中序遍歷**：N 叉樹沒有明確的中序遍歷定義
- **深度與廣度優先搜索**：實現方式需要適應多子節點的特性

#### N 叉樹節點定義

```python
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
```

#### 練習題目

1. [589. N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/) (Easy)

   - 核心技巧：N 叉樹前序遍歷
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)，h 為樹高
   - 學習重點：
     - 處理多子節點的遍歷
     - 遞迴與迭代實現的差異
     - 堆疊使用方式的調整

2. [590. N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/) (Easy)

   - 核心技巧：N 叉樹後序遍歷
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - 後序遍歷的實現方式
     - 子節點處理順序的重要性
     - 迭代解法的複雜度

3. [429. N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) (Medium)

   - 核心技巧：N 叉樹層序遍歷
   - 時間複雜度：O(n)
   - 空間複雜度：O(w)，w 為最寬層的節點數
   - 學習重點：
     - 隊列在層序遍歷中的應用
     - 層級資訊的維護方式
     - 與二元樹層序遍歷的異同

4. [559. Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/) (Easy)

   - 核心技巧：深度計算
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - 深度計算的遞迴實現
     - 多子節點的最大值比較
     - 迭代解法的實現方式

5. [431. Encode N-ary Tree to Binary Tree](https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/) (Hard)

   - 核心技巧：樹結構轉換
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - 不同樹結構間的轉換思路
     - 編碼與解碼的對應關係
     - 保持結構信息的完整性

#### N 叉樹解題模板

```python
from typing import List
from collections import deque

# 前序遍歷（遞迴）
def preorder_recursive(root):
    """N 叉樹前序遍歷（遞迴）- 根->子節點"""
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.val)  # 訪問根節點
        for child in node.children:  # 遍歷所有子節點
            dfs(child)

    dfs(root)
    return result

# 前序遍歷（迭代）
def preorder_iterative(root):
    """N 叉樹前序遍歷（迭代）- 根->子節點"""
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)
        # 注意：因為是堆疊（後進先出），所以要倒序加入子節點
        for child in reversed(node.children):
            stack.append(child)

    return result

# 後序遍歷（遞迴）
def postorder_recursive(root):
    """N 叉樹後序遍歷（遞迴）- 子節點->根"""
    result = []

    def dfs(node):
        if not node:
            return
        for child in node.children:  # 先遍歷所有子節點
            dfs(child)
        result.append(node.val)  # 最後訪問根節點

    dfs(root)
    return result

# 層序遍歷
def levelorder(root):
    """N 叉樹層序遍歷"""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            for child in node.children:
                queue.append(child)

        result.append(current_level)

    return result

# 計算樹的最大深度
def max_depth(root):
    """計算 N 叉樹的最大深度"""
    if not root:
        return 0

    if not root.children:
        return 1

    # 找出所有子樹中的最大深度
    max_child_depth = 0
    for child in root.children:
        max_child_depth = max(max_child_depth, max_depth(child))

    # 當前節點的深度 = 最大子樹深度 + 1
    return max_child_depth + 1
```

#### 更多簡單的 N 叉樹題目

6. [1302. Deepest Leaves Sum](https://leetcode.com/problems/deepest-leaves-sum/) (Medium)

   - 核心技巧：層序遍歷 + 深度追蹤
   - 時間複雜度：O(n)
   - 空間複雜度：O(w)
   - 學習重點：
     - 識別最深層的節點
     - 層序遍歷的應用
     - 深度與節點值的結合處理

7. [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) (Easy)

   - 核心技巧：樹的比較
   - 時間複雜度：O(m\*n)，m 和 n 分別為兩棵樹的節點數
   - 空間複雜度：O(h)
   - 學習重點：
     - 子樹判斷的條件
     - 遞迴比較的實現
     - 優化比較過程

8. [993. Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/) (Easy)

   - 核心技巧：節點關係判斷
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - 節點深度的計算
     - 父節點的識別
     - 堂兄弟關係的判定

9. [1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) (Medium)

   - 核心技巧：路徑最大值追蹤
   - 時間複雜度：O(n)
   - 空間複雜度：O(h)
   - 學習重點：
     - 路徑上的值比較
     - 遞迴參數的傳遞
     - 計數條件的設計

#### N 叉樹解題技巧

1. **子節點處理順序**

   - 前序遍歷：先處理當前節點，再處理子節點
   - 後序遍歷：先處理所有子節點，再處理當前節點
   - 迭代實現時，注意堆疊的壓入順序（通常需要倒序）

2. **遞迴到迭代的轉換**

   - 使用堆疊模擬系統調用堆疊
   - 前序遍歷：直接處理當前節點，再壓入子節點（倒序）
   - 後序遍歷：可以考慮「前序遍歷的倒序」技巧

3. **層序遍歷的實現**

   - 使用隊列（Queue）而非堆疊
   - 記錄每一層的大小，以便分層處理
   - 處理當前節點後，將所有子節點加入隊列

4. **狀態追蹤技巧**

   - 路徑問題：傳遞當前路徑狀態（如和、最大值等）
   - 深度問題：傳遞當前深度或從子節點返回深度
   - 關係問題：記錄父節點、兄弟節點或其他關係

5. **N 叉樹與二元樹的轉換**
   - 左子節點：指向第一個子節點
   - 右子節點：指向兄弟節點
   - 這種轉換可以讓二元樹算法應用於 N 叉樹

```python
# N 叉樹轉二元樹的示例
def encode(root):
    """將 N 叉樹編碼為二元樹"""
    if not root:
        return None

    binary_root = TreeNode(root.val)

    if not root.children:
        return binary_root

    # 第一個子節點作為左子節點
    binary_root.left = encode(root.children[0])

    # 構建兄弟鏈（右子節點指向兄弟）
    current = binary_root.left
    for i in range(1, len(root.children)):
        current.right = encode(root.children[i])
        current = current.right

    return binary_root
```

## Python 解題模板

### 1. 樹節點定義

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### 2. 遍歷模板

```python
from typing import List, Optional
from collections import deque


# 1. 遞迴實現
def preorder_recursive(root: Optional[TreeNode]) -> List[int]:
    """前序遍歷（遞迴）- 根->左->右"""
    def dfs(node: Optional[TreeNode], result: List[int]) -> None:
        if not node:
            return
        result.append(node.val)  # 訪問根節點
        dfs(node.left, result)   # 遍歷左子樹
        dfs(node.right, result)  # 遍歷右子樹

    result = []
    dfs(root, result)
    return result


def inorder_recursive(root: Optional[TreeNode]) -> List[int]:
    """中序遍歷（遞迴）- 左->根->右"""
    def dfs(node: Optional[TreeNode], result: List[int]) -> None:
        if not node:
            return
        dfs(node.left, result)   # 遍歷左子樹
        result.append(node.val)  # 訪問根節點
        dfs(node.right, result)  # 遍歷右子樹

    result = []
    dfs(root, result)
    return result


def postorder_recursive(root: Optional[TreeNode]) -> List[int]:
    """後序遍歷（遞迴）- 左->右->根"""
    def dfs(node: Optional[TreeNode], result: List[int]) -> None:
        if not node:
            return
        dfs(node.left, result)   # 遍歷左子樹
        dfs(node.right, result)  # 遍歷右子樹
        result.append(node.val)  # 訪問根節點

    result = []
    dfs(root, result)
    return result


def levelorder_recursive(root: Optional[TreeNode]) -> List[List[int]]:
    """層序遍歷（遞迴）"""
    def dfs(node: Optional[TreeNode], level: int, result: List[List[int]]) -> None:
        if not node:
            return
        # 如果當前層級還沒有對應的列表，就創建一個
        if len(result) == level:
            result.append([])
        # 將當前節點的值加入對應層級的列表
        result[level].append(node.val)
        # 遞迴處理左右子樹，層級加1
        dfs(node.left, level + 1, result)
        dfs(node.right, level + 1, result)

    result = []
    dfs(root, 0, result)
    return result


# 2. 迭代實現
def preorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """前序遍歷（迭代）- 根->左->右"""
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)
        # 注意：因為是使用堆疊，所以要先將右子節點壓入堆疊
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """中序遍歷（迭代）- 左->根->右"""
    result = []
    stack = []
    current = root

    while current or stack:
        # 一直往左走，將所有左子節點壓入堆疊
        while current:
            stack.append(current)
            current = current.left

        # 處理當前節點
        current = stack.pop()
        result.append(current.val)

        # 移動到右子節點
        current = current.right

    return result


def postorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """後序遍歷（迭代）- 左->右->根"""
    if not root:
        return []

    result = []
    stack = [(root, False)]  # (節點, 是否已訪問過右子樹)

    while stack:
        node, visited = stack.pop()
        # 如果是葉節點或已經訪問過右子樹
        if not node.left and not node.right or visited:
            result.append(node.val)
        else:
            # 重新壓入當前節點，標記為已訪問
            stack.append((node, True))
            # 先壓入右子節點（因為後序遍歷是左->右->根）
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))

    return result


def levelorder_iterative(root: Optional[TreeNode]) -> List[List[int]]:
    """層序遍歷（迭代）"""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result
```

### 3. 路徑問題模板

```python
# 路徑和檢查
def has_path_sum(root, target):
    if not root:
        return False

    def dfs(node, curr_sum):
        if not node:
            return False
        curr_sum += node.val
        if not node.left and not node.right:  # 葉節點
            return curr_sum == target
        return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)

    return dfs(root, 0)

# 收集所有路徑
def binary_tree_paths(root):
    def dfs(node, path):
        if not node:
            return
        path.append(str(node.val))
        if not node.left and not node.right:  # 葉節點
            result.append('->'.join(path))
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        path.pop()  # 回溯

    result = []
    dfs(root, [])
    return result
```

### 4. BST 操作模板

```python
# BST 驗證
def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return validate(node.left, min_val, node.val) and \
               validate(node.right, node.val, max_val)

    return validate(root, float('-inf'), float('inf'))

# BST 搜尋
def search_bst(root, val):
    curr = root
    while curr and curr.val != val:
        curr = curr.left if val < curr.val else curr.right
    return curr
```

## 學習建議

### 1. 學習順序

1. 第一週：基本遍歷 (94, 144, 145)
2. 第二週：層序遍歷與基本遞迴 (102, 226)
3. 第三週：樹的對稱與比較 (100, 101)
4. 第四週：路徑相關問題 (112, 257)
5. 第五週：BST 特性與操作 (98, 700)
6. 第六週：N 叉樹基礎 (589, 590, 429)
7. 第七週：N 叉樹進階應用 (559, 1302, 431)

### 2. 學習方法

1. 先掌握四種基本遍歷方式
2. 理解遞迴與迭代的轉換
3. 從簡單的結構判斷開始
4. 逐步過渡到複雜的路徑問題

### 3. 進階建議

1. 練習不同遍歷方法的互相轉換
2. 關注空間複雜度的優化
3. 嘗試將遞迴解法改寫為迭代
4. 理解並實現 Morris 遍歷

### 4. N 叉樹學習建議

1. **學習順序**

   - 先掌握基本的 N 叉樹遍歷（前序、後序、層序）
   - 理解 N 叉樹與二元樹的差異和聯繫
   - 學習如何將二元樹的解題思路應用到 N 叉樹

2. **解題技巧**

   - 遍歷時注意子節點的處理順序
   - 迭代實現時特別注意堆疊/隊列的使用方式
   - 善用「狀態追蹤」來解決複雜問題

3. **常見錯誤**

   - 忘記處理空節點或空子節點列表
   - 迭代實現時子節點壓入順序錯誤
   - 忽略 N 叉樹沒有中序遍歷的特點

4. **進階方向**

   - 嘗試 N 叉樹與二元樹的相互轉換
   - 實現更高效的遍歷算法
   - 解決涉及多棵 N 叉樹的複雜問題

5. **實際應用場景**
   - 文件系統的目錄結構
   - 組織架構圖
   - DOM 樹結構
   - 多叉搜尋樹（如 B 樹、B+ 樹）
