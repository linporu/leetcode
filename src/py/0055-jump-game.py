from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 記錄能到達的最遠位置
        max_reach = 0

        # 遍歷數組 (只需要遍歷到能到達的範圍內)
        for i in range(len(nums)):
            # 如果當前位置已經超過了能到達的最遠位置，則失敗
            if i > max_reach:
                return False

            # 更新能到達的最遠位置
            max_reach = max(max_reach, i + nums[i])

            # 如果已經能到達終點，就提前返回成功
            if max_reach >= len(nums) - 1:
                return True

        return True  # 如果遍歷完整個數組，說明能到達終點
