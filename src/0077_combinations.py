from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(choices, path):
            if len(path) == k:  # 當路徑長度達到 k 時收集結果
                result.append(path.copy())
                return

            remaining = set(choices)
            for choice in remaining:
                path.append(choice)
                new_choices = {x for x in remaining if x > choice}  # 只選擇比當前數字大的
                backtrack(new_choices, path)
                path.pop()

        result = []
        choices = {i for i in range(1, n + 1)}  # 修正範圍到 n
        backtrack(choices, [])

        return result
