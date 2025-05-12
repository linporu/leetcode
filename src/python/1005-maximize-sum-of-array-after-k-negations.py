from typing import List


# First take
class Solution01:
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


# Optimized greedy approach
class Solution02:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 按絕對值大小從大到小排序
        nums.sort(key=abs, reverse=True)

        # 處理負數
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1

        # 如果剩下奇數次操作，翻轉最小的數（在排序後的尾部）
        if k % 2 == 1:
            nums[-1] = -nums[-1]

        return sum(nums)
