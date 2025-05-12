from typing import List


# Dijkstra
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq

        graph = {node: {} for node in range(1, n + 1)}
        for u, v, weight in times:
            graph[u][v] = weight

        distances = {node: float("inf") for node in range(1, n + 1)}
        distances[k] = 0
        pq = [(0, k)]

        while pq:
            curr_distance, curr_node = heapq.heappop(pq)
            if curr_distance > distances[curr_node]:
                continue

            for neighbor in graph[curr_node]:
                distance = curr_distance + graph[curr_node][neighbor]
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        min_time = 0
        for node in distances:
            if distances[node] == float("inf"):
                return -1

            # 最短遍歷整張圖的時間，即是 k 到所有 node 最短路徑中的最長者
            min_time = max(min_time, distances[node])

        return min_time
