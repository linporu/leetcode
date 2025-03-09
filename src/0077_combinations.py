from typing import List


# Recursive approach
class Solution01:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(choices, path):
            if len(path) == k:  # 當路徑長度達到 k 時收集結果
                result.append(path.copy())
                return

            remaining = set(choices)
            for choice in remaining:
                path.append(choice)
                new_choices = {
                    new_choice for new_choice in remaining if new_choice > choice
                }  # 只選擇比當前數字大的
                backtrack(new_choices, path)
                path.pop()

        result = []
        choices = {i for i in range(1, n + 1)}  # 修正範圍到 n
        backtrack(choices, [])

        return result


# Iterative approach
class Solution02:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []
        choices = {i for i in range(1, n + 1)}
        stack = [(path, choices)]

        while stack:
            path, remaining = stack.pop()

            if len(path) == k:
                result.append(path.copy())

            for choice in remaining:
                new_path = path + [choice]
                new_choices = {new_choice for new_choice in remaining if new_choice > choice}
                stack.append((new_path, new_choices))

        return result
