from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
