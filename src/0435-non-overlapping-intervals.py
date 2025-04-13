from typing import List


# Intuition: Sort by end time. When intervals overlap, remove interval  with later end time.
class Solution:
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
