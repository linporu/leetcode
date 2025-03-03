from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Base case
        if not nums:
            return [-1, -1]

        # Search leftmost:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        if nums[left] != target:
            return [-1, -1]

        left_most = left

        # Search rightmost:
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1

        right_most = left - 1

        return [left_most, right_most]
