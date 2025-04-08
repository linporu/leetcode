from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n > 0:
            ptr1, ptr2 = m - 1, n - 1
            curr = m + n - 1  # 當前要填入的位置

            # 當兩個指針都還有效時
            while ptr1 >= 0 and ptr2 >= 0:
                if nums1[ptr1] >= nums2[ptr2]:
                    nums1[curr] = nums1[ptr1]
                    ptr1 -= 1
                else:
                    nums1[curr] = nums2[ptr2]
                    ptr2 -= 1
                curr -= 1

            # 如果 nums2 還有剩餘的元素
            while ptr2 >= 0:
                nums1[curr] = nums2[ptr2]
                ptr2 -= 1
                curr -= 1
