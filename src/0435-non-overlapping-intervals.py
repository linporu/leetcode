from typing import List


# Intuition: Sort by end time. When intervals overlap, remove interval  with later end time.
class Solution01:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def endtime(interval):
            return interval[1]

        intervals.sort(key=endtime)

        num_intervals = len(intervals)

        if num_intervals == 1:
            return 0

        removed = 0
        curr = 0
        next = 1

        for i in range(num_intervals):

            if i < curr:
                continue

            if next >= num_intervals:
                break

            while intervals[curr][1] > intervals[next][0]:  # Overlap
                next += 1
                removed += 1
                if next >= num_intervals:
                    break

            curr = next
            next += 1

        return removed


# AI optimized
class Solution02:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # 按照結束時間排序
        intervals.sort(key=lambda x: x[1])

        # 初始化：保留第一個區間
        end = intervals[0][1]
        count = 1  # 計算可以保留的區間數量

        # 遍歷剩餘區間
        for i in range(1, len(intervals)):
            # 如果當前區間的起始時間 >= 前一個保留區間的結束時間，則保留
            if intervals[i][0] >= end:
                end = intervals[i][1]  # 更新結束時間
                count += 1

        # 返回需要移除的區間數量
        return len(intervals) - count
