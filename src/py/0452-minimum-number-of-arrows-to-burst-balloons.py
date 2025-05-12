from typing import List


# Intuition: find all baloons not overlapping, each baloon need one arrow
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        prev_right = points[0][1]
        no_overlap_baloon = 1

        for baloon in points[1:]:
            if baloon[0] > prev_right:  # No overlap
                no_overlap_baloon += 1
                prev_right = baloon[1]

        return no_overlap_baloon
