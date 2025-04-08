from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr_idx = 0

        while k > 0 and curr_idx < len(nums):
            if nums[curr_idx] < 0:
                nums[curr_idx] = abs(nums[curr_idx])
                if curr_idx < len(nums) - 1:
                    if nums[curr_idx] > nums[curr_idx + 1]:
                        curr_idx += 1
            else:
                nums[curr_idx] = -nums[curr_idx]

            k -= 1

        return sum(nums)
