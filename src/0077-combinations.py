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


# Optimized solution
class Solution03:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start: int, curr: List[int]):
            if len(curr) == k:
                result.append(curr[:])  # 這裡還是需要複製，因為curr會被修改
                return

            # 優化：計算還需要幾個數字，確保有足夠的數字可以選
            # n - i + 1 >= k - len(curr)
            for i in range(start, n - (k - len(curr)) + 2):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()

        result = []
        backtrack(1, [])
        return result


# Itertools solution
class Solution04:
    def combine(self, n: int, k: int) -> List[List[int]]:
        import itertools

        return list(map(list, itertools.combinations([i for i in range(1, n + 1)], k)))
