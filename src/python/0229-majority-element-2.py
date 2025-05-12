from typing import List


# 從可能的結果反推，只可能返回一到兩個數字，所以隨時確保誰是前兩名就好？如果第一名是第二名兩倍以上，只返回第一名
# https://leetcode.com/problems/majority-element-ii/description/
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        # Boyer-Moore Algorithm 追蹤前兩名
        candidate_1, candidate_2 = None, None
        count_1, count_2 = 0, 0

        for num in nums:
            # 先檢查是否和現有選項相同
            if num == candidate_1:
                count_1 += 1
            elif num == candidate_2:
                count_2 += 1

            # 檢查前兩名是否被歸零
            elif num != candidate_1 and count_1 == 0:
                candidate_1 = num
                count_1 = 1
            elif num != candidate_2 and count_2 == 0:
                candidate_2 = num
                count_2 = 1

            # 處理和前兩名不同的數字
            else:
                count_1 -= 1
                count_2 -= 1

        # 遍歷 array，確認個數
        count_1, count_2 = 0, 0
        for num in nums:
            if num == candidate_1:
                count_1 += 1
            if num == candidate_2:
                count_2 += 1

        # 返回超過 n/3 門檻的選項
        threshold = len(nums) / 3
        answer = []
        if count_1 > threshold:
            answer.append(candidate_1)
        if count_2 > threshold:
            answer.append(candidate_2)
        return answer
