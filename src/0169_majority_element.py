from typing import List


# Hashmap
class Solution01:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        max_count = 0

        for num in hashmap:
            if hashmap[num] > max_count:
                max_count = hashmap[num]
                majority_element = num

        return majority_element


# Boyer-Moore Voting Algorithm
class Solution02:
    def majorityElement(self, nums: List[int]) -> int:
        """使用 Boyer-Moore Voting Algorithm 找出多數元素。

        原理說明：
        1. 此算法基於「多數元素出現次數 > n/2」的特性
        2. 使用計數器(count)和候選人(candidate)進行追蹤：
           - 遇到相同元素時 count += 1
           - 遇到不同元素時 count -= 1
           - 當 count 歸零時，表示前面的元素互相抵消，選新的候選人
        3. 由於多數元素出現次數超過一半，最後必定會「勝出」成為 candidate

        時間複雜度：O(n) - 只需遍歷一次陣列
        空間複雜度：O(1) - 只需兩個變數(count, candidate)

        Args:
            nums: List[int] - 輸入的整數陣列

        Returns:
            int - 出現次數超過 n/2 的多數元素

        Example:
            >>> majorityElement([2,2,1,1,1,2,2])
            2
        """
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
