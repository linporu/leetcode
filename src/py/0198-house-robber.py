from typing import List


# Buttom up DP
class Solution01:
    def rob(self, nums: List[int]) -> int:
        num_house = len(nums)

        if num_house == 1:
            return nums[0]
        if num_house == 2:
            return max(nums[0], nums[1])

        # Initialize dp array
        dp = [0] * num_house  # Money robbed until ith house
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, num_house):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])  # Choose to rob or not to rob the ith house

        return dp[num_house - 1]


# Buttom up DP with space optimization
class Solution02:
    def rob(self, nums: List[int]) -> int:
        num_house = len(nums)

        if num_house == 1:
            return nums[0]
        if num_house == 2:
            return max(nums[0], nums[1])

        prev1 = nums[0]
        prev2 = max(nums[0], nums[1])

        for i in range(2, num_house):
            current = max(prev1 + nums[i], prev2)
            prev1 = prev2
            prev2 = current

        return current


# Top down DP
class Solution03:
    def rob(self, nums: List[int]) -> int:

        num_house = len(nums)
        if num_house == 1:
            return nums[0]
        if num_house == 2:
            return max(nums[0], nums[1])

        # Initialize memoization
        memo = {}
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        def money_robbed(i):
            if i in memo:
                return memo[i]

            # Cache the result
            memo[i] = max(money_robbed(i - 2) + nums[i], money_robbed(i - 1))

            return memo[i]

        return money_robbed(num_house - 1)


# Top down DP with cache decorator
class Solution04:
    def rob(self, nums: List[int]) -> int:
        from functools import cache

        num_house = len(nums)
        if num_house == 1:
            return nums[0]
        if num_house == 2:
            return max(nums[0], nums[1])

        @cache
        def money_robbed(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            return max(money_robbed(i - 2) + nums[i], money_robbed(i - 1))

        return money_robbed(num_house - 1)
