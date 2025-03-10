from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path):
            if len(path) == nums_size:
                result.append(path.copy())
                return

            used_at_position = set()  # 追蹤在當前位置已經使用過的數字

            for i in range(nums_size):
                # 如果當前索引已被使用過或當前數字在此位置已經使用過，則跳過
                if visited[i] or nums[i] in used_at_position:
                    continue

                # 記錄此數字在當前位置已使用
                used_at_position.add(nums[i])
                visited[i] = True
                path.append(nums[i])

                backtrack(path)

                path.pop()
                visited[i] = False

        nums.sort()  # 排序以便相同的數字相鄰
        result = []
        nums_size = len(nums)
        visited = [False] * nums_size  # 使用索引來追蹤元素是否被使用
        backtrack([])
        return result
