from typing import List


# General backtracking approach
class Solution01:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            # 每次遞迴都將當前路徑加入結果集
            # 因為每個路徑都是一個有效的子集
            result.append(path.copy())

            # 從 start 開始，嘗試添加每個剩餘元素
            for i in range(start, len(nums)):
                # 做出選擇
                path.append(nums[i])

                # 遞迴探索（只考慮當前元素之後的元素，避免重複）
                backtrack(i + 1, path)

                # 撤銷選擇（回溯）
                path.pop()

        # 從空集開始，索引 0 開始
        backtrack(0, [])
        return result


# Binary tree backtrack approach
class Solution02:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        把整個問題想成探索一個二元樹，每一層都有「加入/不加入 nums[depth] 的兩個分支。
        """
        result = []
        path = []

        def backtrack(index):
            # 當處理完所有元素時，將當前路徑加入結果
            if index == len(nums):
                result.append(path.copy())
                return

            # 不選擇當前元素的情況
            backtrack(index + 1)

            # 選擇當前元素的情況
            path.append(nums[index])
            backtrack(index + 1)
            path.pop()  # 回溯，移除剛才加入的元素

        backtrack(0)
        return result


# Iterative approach
class Solution03:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]  # 初始時只有一個空集

        for num in nums:
            # 對於每個元素，將它添加到已有的所有子集中，形成新的子集
            new_subsets = []
            for subset in result:
                # 創建一個新的子集，包含當前元素
                new_subset = subset.copy()  # 必須複製，否則會修改原始子集
                new_subset.append(num)
                new_subsets.append(new_subset)

            # 將新生成的子集添加到結果集中
            result.extend(new_subsets)

        return result
