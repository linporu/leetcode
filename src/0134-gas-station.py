from typing import List


# First take
class Solution:
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
