from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict and i != dict[complement]:
                return [i, dict[complement]]
            dict[nums[i]] = i
        return []
