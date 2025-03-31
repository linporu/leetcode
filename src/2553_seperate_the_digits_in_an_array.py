from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            str_num = str(num)
            for digit in str_num:
                result.append(int(digit))

        return result
