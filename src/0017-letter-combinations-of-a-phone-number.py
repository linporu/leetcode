from typing import List


# Recursive DFS
class Solution01:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def backtrack(idx, path):
            if idx == len(digits):
                result.append(path)
                return

            curr_digit = digits[idx]

            for letter in map[curr_digit]:
                # 直接創建新字串並傳遞給下一層遞迴
                backtrack(idx + 1, path + letter)

        if not digits:
            return []

        result = []
        backtrack(0, "")
        return result


# Iterative DFS
class Solution02:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if not digits:
            return []

        result = []
        stack = [(0, "")]

        while stack:
            idx, path = stack.pop()

            if idx == len(digits):
                result.append(path)
                continue

            for letter in map[digits[idx]]:
                new_path = path + letter
                stack.append((idx + 1, new_path))

        return result
