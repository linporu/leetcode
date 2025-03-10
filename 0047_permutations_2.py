from typing import List


# Recursive approach
class Solution01:
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


# Iterative approach
class Solution02:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        result = []
        path = []
        nums_size = len(nums)
        visited = [False] * nums_size

        # 每個狀態包含：當前路徑、已訪問的索引
        stack = [(path, visited)]

        while stack:
            path, visited = stack.pop()

            # 如果路徑已完成，加入結果
            if len(path) == nums_size:
                result.append(path)
                continue

            used_at_position = set()  # 追蹤在當前位置已經使用過的數字

            for i in range(nums_size):
                # 如果當前索引已被使用過或當前數字在此位置已經使用過，則跳過
                if visited[i] or nums[i] in used_at_position:
                    continue

                # 創建新的路徑和訪問狀態（避免修改原始數據）
                new_path = path.copy()
                new_path.append(nums[i])

                new_visited = visited.copy()
                new_visited[i] = True

                # 將新狀態加入堆疊
                stack.append((new_path, new_visited))

                # 記錄此數字在當前位置已使用
                used_at_position.add(nums[i])

        return result
