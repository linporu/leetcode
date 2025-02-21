"""
回溯算法模板 (Backtracking Template)

回溯算法的本質是在決策樹上進行深度優先搜索 (DFS)。
主要應用於排列、組合、子集等問題。

基本步驟：
1. 選擇：做出選擇，向前探索
2. 約束：檢查是否符合題目要求
3. 目標：檢查是否達到目標
4. 回溯：撤銷選擇，回到之前的狀態
"""

from typing import List, Set


class BacktrackingTemplate:
    def __init__(self):
        self.results = []  # 存儲所有合法解

    def backtrack_recursive(self, nums: List[int]) -> List[List[int]]:
        """
        遞迴實現的回溯

        Args:
            nums: 輸入數組

        Returns:
            List[List[int]]: 所有合法解的列表
        """

        def backtrack(path: List[int], choices: Set[int]):
            # 達到目標（終止條件）
            if len(path) == len(nums):
                self.results.append(path[:])  # 重要：要創建一個副本
                return

            # 遍歷所有可能的選擇
            for num in choices:
                # 做選擇
                path.append(num)
                new_choices = choices - {num}  # 更新可用選擇

                # 遞迴
                backtrack(path, new_choices)

                # 撤銷選擇（回溯）
                path.pop()

        self.results = []
        initial_choices = set(nums)
        backtrack([], initial_choices)
        return self.results

    def backtrack_iterative(self, nums: List[int]) -> List[List[int]]:
        """
        迭代實現的回溯
        使用顯式的棧來模擬遞迴過程

        Args:
            nums: 輸入數組

        Returns:
            List[List[int]]: 所有合法解的列表
        """
        self.results = []
        if not nums:
            return self.results

        # 棧中的每個元素是一個狀態，包含：
        # 1. 當前路徑
        # 2. 剩餘的選擇
        # 3. 下一個要處理的選擇的索引
        stack = [([], set(nums), 0)]

        while stack:
            path, choices, next_choice_idx = stack.pop()

            # 達到目標
            if len(path) == len(nums):
                self.results.append(path[:])
                continue

            # 將剩餘的選擇轉換為列表以便索引
            choices_list = list(choices)

            # 遍歷剩餘的選擇
            for i in range(next_choice_idx, len(choices_list)):
                num = choices_list[i]
                new_path = path + [num]
                new_choices = choices - {num}

                # 將新狀態壓入棧中
                stack.append((new_path, new_choices, 0))

        return self.results


def example_usage():
    """示範如何使用回溯模板"""
    bt = BacktrackingTemplate()

    # 測試數據
    test_nums = [1, 2, 3]

    # 使用遞迴方式
    print("遞迴實現的結果：")
    recursive_results = bt.backtrack_recursive(test_nums)
    print(recursive_results)

    # 使用迭代方式
    print("\n迭代實現的結果：")
    iterative_results = bt.backtrack_iterative(test_nums)
    print(iterative_results)


if __name__ == "__main__":
    example_usage()
