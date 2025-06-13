class Solution:
    def mySqrt(self, x: int) -> int:

        left, right = 0, x

        while left <= right:
            mid = left + (right - left) // 2

            if (mid * mid <= x) and ((mid + 1) * (mid + 1) > x):
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
