from typing import List


# Recursive DFS (RecursionError: maximum recursion depth exceeded)
class Solution01:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(path, remaining_target, start_idx):
            stop_idx = len(candidates)
            if remaining_target < 0:
                return

            if remaining_target == 0:
                result.append(path.copy())
                return

            for i in range(start_idx, stop_idx):
                candidate = candidates[i]

                if remaining_target < candidate:
                    break

                new_remaining_target = remaining_target - candidate
                path.append(candidate)
                backtrack(path, new_remaining_target, i)
                path.pop()

        if not candidates:
            return []

        candidates.sort()
        result = []
        backtrack([], target, 0)

        return result


# Iterative DFS
class Solution02:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        candidates.sort()

        result = []
        path = []
        remaining_target = target
        start_idx = 0
        stop_idx = len(candidates)
        stack = [(path, remaining_target, start_idx)]

        while stack:
            path, remaining_target, start_idx = stack.pop()

            if remaining_target < 0:
                continue

            if remaining_target == 0:
                result.append(path.copy())
                continue

            for i in range(start_idx, stop_idx):
                candidate = candidates[i]

                if candidate > remaining_target:
                    break

                new_remaining_target = remaining_target - candidate
                new_path = path + [candidate]
                stack.append((new_path, new_remaining_target, i))

        return result
