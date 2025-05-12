from typing import List


# Index Tracking Approach
class Solution01:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """使用索引追蹤法生成所有排列（Index Tracking Approach）

        思路：
        1. 維護一個 remained_indexes 列表來追蹤還未使用的數字的索引
        2. 使用 path 列表來構建當前的排列
        3. 每次遞迴時：
           - 從 remained_indexes 中選擇一個索引
           - 將對應的數字加入 path
           - 創建新的 remained_indexes（排除已選擇的索引）
           - 遞迴處理剩餘的索引

        時間複雜度：O(n!)，每次遞迴還需要 O(n) 來創建新的 remained_indexes
        空間複雜度：O(n * n!)，需要額外空間來存儲每次遞迴的 remained_indexes
        """
        result = []
        remained_indexes = [i for i in range(len(nums))]

        def backtrack(remained_indexes, path):
            if not remained_indexes:
                result.append(path.copy())
                return

            for index in remained_indexes:
                path.append(nums[index])
                # Create a new list excluding the current index
                next_remained = [i for i in remained_indexes if i != index]
                backtrack(next_remained, path)
                path.pop()

        backtrack(remained_indexes, [])
        return result


# Swap-based Approach
class Solution02:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """使用交換法生成所有排列（Swap-based Approach）

        思路：
        1. 將問題視為：對於位置 i，與之後的每個位置交換，形成不同排列
        2. 使用 first 參數來標記當前處理到的位置
        3. 每次遞迴時：
           - 將位置 first 與之後的每個位置交換
           - 遞迴處理下一個位置 (first + 1)
           - 交換回來（回溯）以恢復原始狀態

        優勢：
        1. 原地操作，不需要額外空間存儲中間狀態
        2. 每次操作都是 O(1) 的交換操作

        時間複雜度：O(n!)
        空間複雜度：O(n)，只需要遞迴調用棧的空間

        示例：
        對於 nums = [1, 2, 3]
        第一層遞迴 (first = 0):
            - [1, 2, 3] -> 處理 2, 3 的排列
            - [2, 1, 3] -> 處理 1, 3 的排列
            - [3, 2, 1] -> 處理 2, 1 的排列

        以 [1, 2, 3] 為例，第二層遞迴 (first = 1):
            - [1, 2, 3] -> 處理 3
            - [1, 3, 2] -> 處理 2
        """
        result = []
        n = len(nums)

        def backtrack(first=0):
            if first == n:
                result.append(nums[:])
                return

            for i in range(first, n):
                # 交換當前位置和待處理位置的元素
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                # 回溯，恢復原狀
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return result


# Iterative Approach
class Solution03:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """使用迭代式方法生成所有排列（Iterative Approach）

        思路：
        1. 使用堆疊來模擬遞迴
        2. 每個堆疊項目包含：
           - 當前的路徑 (path)
           - 剩餘可用的數字索引 (remained_indexes)
        3. 使用迭代方式處理堆疊，直到堆疊為空

        優勢：
        1. 避免遞迴調用的開銷
        2. 在某些情況下可能比遞迴更快
        3. 不會有堆疊溢出的風險

        時間複雜度：O(n!)
        空間複雜度：O(n * n!)，需要存儲所有狀態

        示例：
        對於 nums = [1, 2]：

        堆疊操作過程：
        1. ([],     [0,1])         # 初始狀態
        2. ([1],    [1])           # 選擇 index 0
        3. ([1,2],  [])           # 選擇 index 1，得到第一個排列 [1,2]
        4. ([2],    [0])           # 回溯到選擇 index 1
        5. ([2,1],  [])           # 選擇 index 0，得到第二個排列 [2,1]
        """
        if not nums:
            return []

        result = []
        n = len(nums)

        # 堆疊項目格式：(current_path, remained_indexes)
        stack = [([], list(range(n)))]

        while stack:
            path, remained_indexes = stack.pop()

            # 如果沒有剩餘的數字，表示找到一個完整的排列
            if not remained_indexes:
                result.append([nums[i] for i in path])
                continue

            # 注意：我們需要反向遍歷，因為使用堆疊（後進先出）
            for i in range(len(remained_indexes) - 1, -1, -1):
                next_remained = remained_indexes[:i] + remained_indexes[i + 1:]
                next_path = path + [remained_indexes[i]]
                stack.append((next_path, next_remained))

        return result


# Itertools Approach
class Solution04:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """使用 Python 內建的 itertools 模組生成排列（Itertools Approach）

        思路：
        直接使用 Python 標準庫中的 itertools.permutations，它使用高度優化的 C 實現

        優勢：
        1. 程式碼最簡潔
        2. 執行效率最高（C 語言實現）
        3. 不需要自己處理遞迴和回溯邏輯
        4. 記憶體使用最優化

        限制：
        1. 只適用於 Python
        2. 在面試時可能會被要求手動實現
        3. 不容易客製化或修改演算法邏輯

        時間複雜度：O(n!)
        空間複雜度：O(n)，itertools 使用迭代器，非常節省記憶體

        轉換過程說明：
        1. itertools.permutations(nums) 返回排列的迭代器
           例如：輸入 [1,2,3] 會得到
           ((1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1))

        2. map(list, ...) 將每個 tuple 轉換成 list
           變成：([1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1])

        3. 最外層的 list(...) 將迭代器轉換成實際的列表
           最終得到：[[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
        """
        import itertools

        # 方法一：使用 map（最簡潔）
        return list(map(list, itertools.permutations(nums)))

        # 方法二：使用列表推導式（較易理解）
        # return [list(p) for p in itertools.permutations(nums)]

        # 方法三：直接使用列表推導式（錯誤示範）
        # return [p for p in itertools.permutations(nums)]  # 錯誤：返回的是 List[Tuple]

        # 方法四：分步驟（最易理解但較冗長）
        # perms = itertools.permutations(nums)
        # return [list(p) for p in perms]
