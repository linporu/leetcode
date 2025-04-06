from typing import List


# Bellman-Ford
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:

        distances = [float("inf")] * n
        distances[src] = 0

        for i in range(k + 1):  # k 個中轉站意味著 k + 1 個航班
            temp = distances.copy()  # 創建當前距離的副本
            for u, v, price in flights:
                if distances[u] != float("inf") and distances[u] + price < temp[v]:
                    temp[v] = distances[u] + price
            distances = temp  # 更新距離表

        return distances[dst] if distances[dst] != float("inf") else -1
