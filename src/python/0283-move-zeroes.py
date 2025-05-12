from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Move all zeros to the end of the array while maintaining the relative order
        of non-zero elements.

        Algorithm:
        1. Use two pointers approach:
           - insert_pos: points to the position where next non-zero element should be placed
           - curr: iterates through the array

        2. When curr finds a non-zero element:
           - Move it to insert_pos
           - Increment insert_pos

        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - only using two pointers

        Example:
        Input: [0,1,0,3,12]
        Process:
        - First non-zero (1): [1,0,0,3,12]
        - Second non-zero (3): [1,3,0,0,12]
        - Third non-zero (12): [1,3,12,0,0]
        """

        insert_pos, curr = 0, 0  # Pointers of insert position and current index

        for _ in nums:
            if nums[curr] != 0:
                nums[curr], nums[insert_pos] = nums[insert_pos], nums[curr]
                insert_pos += 1
            curr += 1
