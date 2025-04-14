from typing import List


# Intuition: find all baloons not overlapping, each baloon need one arrow
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        num_baloon = len(points)
        prev_right = points[0][1]
        no_overlap_baloon = 1

        for i in range(1, num_baloon):
            if points[i][0] > prev_right:  # No overlap
                no_overlap_baloon += 1
                prev_right = points[i][1]

        return no_overlap_baloon
