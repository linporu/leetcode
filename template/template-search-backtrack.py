"""
回溯算法模板 (Backtracking Template)

回溯算法的本質是在 N-ary 決策樹上進行深度優先搜索 (DFS)。
主要應用於排列、組合、子集等問題。

基本步驟：
1. 選擇：做出選擇，向前探索
2. 約束：檢查是否符合題目要求
3. 目標：檢查是否達到目標
4. 回溯：撤銷選擇，回到之前的狀態

剪枝優化策略：
1. 可行性剪枝：提前判斷當前路徑是否可能產生有效解
2. 重複元素剪枝：避免產生重複的組合或排列
3. 排序優化：通過預先排序來優化剪枝效果
"""

from typing import List, Set


class BacktrackingTemplate:
    def __init__(self):
        self.results = []  # 存儲所有合法解

    def backtrack_recursive(self, candidates: List[int]) -> List[List[int]]:
        """
        遞迴實現的回溯

        Args:
            candidates: 輸入候選元素集合

        Returns:
            List[List[int]]: 所有合法解的列表
        """

        # 判斷解是否完成的輔助函數
        def is_valid_solution(path):
            pass

        def backtrack(path: List[int], choices: Set[int]):
            # 達到目標（終止條件）
            if is_valid_solution(path):
                self.results.append(path.copy())  # 重要：要創建一個副本
                return

            # 遍歷所有可能的選擇
            for choice in choices:
                # 做選擇
                path.append(choice)
                new_choices = choices - {choice}  # 更新可用選擇

                # 遞迴
                backtrack(path, new_choices)

                # 撤銷選擇（回溯）
                path.pop()

        self.results = []
        initial_choices = set(candidates)
        backtrack([], initial_choices)
        return self.results

    def backtrack_iterative(self, candidates: List[int]) -> List[List[int]]:
        """
        迭代實現的回溯
        使用顯式的棧來模擬遞迴過程

        Args:
            candidates: 輸入候選元素集合

        Returns:
            List[List[int]]: 所有合法解的列表
        """

        # 判斷解是否完成的輔助函數
        def is_valid_solution(path):
            pass

        self.results = []
        if not candidates:
            return self.results

        # 棧中的每個元素是一個狀態，包含：
        # 1. 當前路徑
        # 2. 剩餘的選擇
        # 3. 下一個要處理的選擇的索引
        stack = [([], set(candidates), 0)]

        while stack:
            path, choices, next_choice_idx = stack.pop()

            # 達到目標
            if is_valid_solution(path):  # 判斷解是否完成
                self.results.append(path.copy())
                continue

            # 將剩餘的選擇轉換為列表以便索引
            choices_list = list(choices)

            # 遍歷剩餘的選擇
            for i in range(next_choice_idx, len(choices_list)):
                num = choices_list[i]
                new_path = path + [num]
                new_choices = choices - {num}

                # 將新狀態壓入棧中
                stack.append((new_path, new_choices, 0))  # next_choice_idx 可成為 pruning 的策略

        return self.results


class PruningBacktrackingTemplate:
    """
    包含剪枝優化的回溯算法模板

    剪枝策略能顯著提高回溯算法的效率，減少不必要的探索
    """

    def __init__(self):
        self.results = []  # 存儲所有合法解

    def feasibility_pruning_recursive(self, nums: List[int], target: int) -> List[List[int]]:
        """
        可行性剪枝的遞迴實現

        提前判斷當前路徑是否可能產生有效解，如果不可能則立即回溯

        Args:
            nums: 輸入數字集合
            target: 目標值

        Returns:
            List[List[int]]: 所有合法解的列表
        """
        self.results = []
        nums.sort()  # 排序以便更有效地剪枝

        def backtrack(start: int, path: List[int], current_sum: int):
            # 可行性剪枝：如果當前和已經超過目標值，則不再繼續
            if current_sum > target:
                return

            # 達到目標
            if current_sum == target:
                self.results.append(path.copy())
                return

            for i in range(start, len(nums)):
                # 排序後的剪枝：如果當前數字已經使得總和超過目標，後面的數字更大，也會超過
                if current_sum + nums[i] > target:
                    break

                path.append(nums[i])
                # 遞迴（注意：這裡是 i+1 表示每個數字只能用一次，若可以重複使用數字則為 i）
                backtrack(i + 1, path, current_sum + nums[i])
                path.pop()

        backtrack(0, [], 0)
        return self.results

    def feasibility_pruning_iterative(self, nums: List[int], target: int) -> List[List[int]]:
        """
        可行性剪枝的迭代實現

        Args:
            nums: 輸入數字集合
            target: 目標值

        Returns:
            List[List[int]]: 所有合法解的列表
        """
        self.results = []
        if not nums:
            return self.results

        nums.sort()  # 排序以便更有效地剪枝

        # 棧中的每個元素是一個狀態，包含：
        # 1. 當前路徑
        # 2. 當前和
        # 3. 開始索引
        stack = [([], 0, 0)]

        while stack:
            path, current_sum, start = stack.pop()

            # 可行性剪枝：如果當前和已經超過目標值，則不再繼續
            if current_sum > target:
                continue

            # 達到目標
            if current_sum == target:
                self.results.append(path.copy())
                continue

            for i in range(start, len(nums)):
                # 排序後的剪枝：如果當前數字已經使得總和超過目標，後面的數字更大，也會超過
                if current_sum + nums[i] > target:
                    break

                new_path = path + [nums[i]]
                # 將新狀態壓入棧中
                stack.append((new_path, current_sum + nums[i], i + 1))

        return self.results

    def duplicate_pruning_recursive(self, nums: List[int]) -> List[List[int]]:
        """
        重複元素剪枝的遞迴實現

        避免產生重複的組合或排列

        Args:
            nums: 輸入數字集合（可能包含重複元素）

        Returns:
            List[List[int]]: 所有不重複的子集
        """
        self.results = []
        nums.sort()  # 排序以便處理重複元素

        def backtrack(start: int, path: List[int]):
            self.results.append(path.copy())

            for i in range(start, len(nums)):
                # 重複元素剪枝：跳過同一層的重複元素
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return self.results

    def duplicate_pruning_iterative(self, nums: List[int]) -> List[List[int]]:
        """
        重複元素剪枝的迭代實現

        Args:
            nums: 輸入數字集合（可能包含重複元素）

        Returns:
            List[List[int]]: 所有不重複的子集
        """
        self.results = []
        if not nums:
            return [self.results]

        nums.sort()  # 排序以便處理重複元素

        # 棧中的每個元素是一個狀態，包含：
        # 1. 當前路徑
        # 2. 開始索引
        stack = [([], 0)]

        while stack:
            path, start = stack.pop()
            self.results.append(path.copy())

            for i in range(start, len(nums)):
                # 重複元素剪枝：跳過同一層的重複元素
                if i > start and nums[i] == nums[i - 1]:
                    continue

                new_path = path + [nums[i]]
                # 將新狀態壓入棧中
                stack.append((new_path, i + 1))

        return self.results

    def sorting_optimization_recursive(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        排序優化的遞迴實現

        通過預先排序來優化剪枝效果

        Args:
            candidates: 輸入候選元素集合
            target: 目標值

        Returns:
            List[List[int]]: 所有合法解的列表
        """
        self.results = []
        candidates.sort()  # 先排序以便優化

        def backtrack(start: int, path: List[int], remain: int):
            if remain < 0:  # 可行性剪枝
                return

            if remain == 0:  # 達到目標
                self.results.append(path.copy())
                return

            for i in range(start, len(candidates)):
                # 排序優化：如果當前元素已經大於剩餘目標值，後面的元素更大，也會超過
                if candidates[i] > remain:
                    break

                # 重複元素剪枝（如果需要）
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                # 注意：這裡是 i 而不是 i+1，因為可以重複使用相同元素
                backtrack(i, path, remain - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return self.results

    def sorting_optimization_iterative(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        排序優化的迭代實現

        Args:
            candidates: 輸入候選元素集合
            target: 目標值

        Returns:
            List[List[int]]: 所有合法解的列表
        """
        self.results = []
        if not candidates:
            return self.results

        candidates.sort()  # 先排序以便優化

        # 棧中的每個元素是一個狀態，包含：
        # 1. 當前路徑
        # 2. 剩餘目標值
        # 3. 開始索引
        stack = [([], target, 0)]

        while stack:
            path, remain, start = stack.pop()

            # 達到目標
            if remain == 0:
                self.results.append(path.copy())
                continue

            for i in range(start, len(candidates)):
                # 排序優化：如果當前元素已經大於剩餘目標值，後面的元素更大，也會超過
                if candidates[i] > remain:
                    break

                # 重複元素剪枝（如果需要）
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                new_path = path + [candidates[i]]
                new_remain = remain - candidates[i]

                # 可行性剪枝
                if new_remain >= 0:
                    # 注意：這裡是 i 而不是 i+1，因為可以重複使用相同元素
                    stack.append((new_path, new_remain, i))

        return self.results


def example_usage():
    """示範如何使用回溯模板"""
    # 基本回溯
    bt = BacktrackingTemplate()
    test_candidates = [1, 2, 3]

    print("基本回溯 - 遞迴實現的結果：")
    recursive_results = bt.backtrack_recursive(test_candidates)
    print(recursive_results)

    print("\n基本回溯 - 迭代實現的結果：")
    iterative_results = bt.backtrack_iterative(test_candidates)
    print(iterative_results)

    # 剪枝優化回溯
    pbt = PruningBacktrackingTemplate()

    # 可行性剪枝示例
    nums = [1, 5, 11, 5]
    target = 11

    print("\n可行性剪枝 - 遞迴實現的結果：")
    feasibility_results = pbt.feasibility_pruning_recursive(nums, target)
    print(feasibility_results)

    # 重複元素剪枝示例
    nums_with_duplicates = [1, 2, 2, 3]

    print("\n重複元素剪枝 - 遞迴實現的結果：")
    duplicate_results = pbt.duplicate_pruning_recursive(nums_with_duplicates)
    print(duplicate_results)

    # 排序優化示例
    candidates = [2, 3, 6, 7]
    target = 7

    print("\n排序優化 - 遞迴實現的結果：")
    sorting_results = pbt.sorting_optimization_recursive(candidates, target)
    print(sorting_results)


if __name__ == "__main__":
    example_usage()
