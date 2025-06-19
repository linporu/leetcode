# Buttom up DP
class Solution01:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2

        # 空間未優化版
        # dp = [0] * n
        # dp[0] = 1
        # dp[1] = 2

        # for idx in range(2, n):
        #     dp[idx] = dp[idx - 1] + dp[idx - 2]

        step_1 = 1
        step_2 = 2

        for _ in range(n - 2):
            step_n = step_1 + step_2
            step_1 = step_2
            step_2 = step_n

        return step_n


# Top down DP
class Solution02:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(n: int) -> int:
            if n == 1:
                return 1
            if n == 2:
                return 2

            if n in memo:
                return memo[n]

            memo[n] = climb(n - 1) + climb(n - 2)
            return memo[n]

        return climb(n)


# Top down DP with cache decorator
class Solution03:
    def climbStairs(self, n: int) -> int:
        from functools import cache

        @cache
        def climb(n: int) -> int:
            if n == 1:
                return 1
            if n == 2:
                return 2

            return climb(n - 1) + climb(n - 2)

        return climb(n)
