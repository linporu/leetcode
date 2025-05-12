from typing import List


# First take
class Solution01:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        remain = 0
        path = []

        if sum(gas) - sum(cost) < 0:  # Not enough gas
            return -1

        if n == 1:
            return 0

        for i in range(n):  # Try different start
            if gas[i] - cost[i] + remain < 0:
                path = []  # Reset path
                remain = 0  # Reset remain gas
                continue

            path.append(i)
            remain += gas[i] - cost[i]

        return path[0]


# AI optimized approach
class Solution02:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        # 如果總油量小於總消耗，不可能完成旅程
        if sum(gas) < sum(cost):
            return -1

        # 如果只有一個站點，直接返回0
        if n == 1:
            return 0

        start = 0  # 可能的起點
        current_tank = 0  # 從目前起點出發的累積汽油量

        for i in range(n):
            # 更新當前汽油量
            current_tank += gas[i] - cost[i]

            # 如果不能到達下一站，重置起點
            if current_tank < 0:
                start = i + 1  # 將起點設為下一個站
                current_tank = 0  # 重置當前汽油量

        # 如果start已經超出邊界，說明沒有解
        if start >= n:
            return -1

        return start
