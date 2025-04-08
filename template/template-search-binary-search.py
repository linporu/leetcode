"""
二分搜尋演算法模板集合
包含各種常見的二分搜尋變體實作

時間複雜度: O(log n)
空間複雜度: O(1)
"""


class BinarySearchTemplate:
    def __init__(self):
        pass

    @staticmethod
    def basic_binary_search(nums: list[int], target: int) -> int:
        """
        基本二分搜尋
        若找到目標值則返回索引，否則返回 -1

        Args:
            nums: 已排序的整數列表
            target: 要搜尋的目標值

        Returns:
            int: 目標值的索引，若不存在則返回 -1
        """
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2  # 避免整數溢出的寫法

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    @staticmethod
    def binary_search_leftmost(nums: list[int], target: int) -> int:
        """
        尋找最左側的目標值（第一個出現的位置）
        若目標值不存在，則返回應該插入的位置

        Args:
            nums: 已排序的整數列表
            target: 要搜尋的目標值

        Returns:
            int: 最左側目標值的索引或應插入的位置
        """
        if not nums:
            return 0

        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left

    @staticmethod
    def binary_search_rightmost(nums: list[int], target: int) -> int:
        """
        尋找最右側的目標值（最後一個出現的位置）
        若目標值不存在，則返回最後一個小於目標值的位置

        Args:
            nums: 已排序的整數列表
            target: 要搜尋的目標值

        Returns:
            int: 最右側目標值的索引，若不存在則返回最後一個小於目標值的位置
        """
        if not nums:
            return -1

        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1

        return left - 1

    @staticmethod
    def binary_search_closest(nums: list[int], target: int) -> int:
        """
        尋找最接近目標值的元素索引

        Args:
            nums: 已排序的整數列表
            target: 要搜尋的目標值

        Returns:
            int: 最接近目標值的元素索引
        """
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

        # 比較左右兩個端點誰更接近目標值
        if abs(nums[left] - target) <= abs(nums[right] - target):
            return left
        return right

    @staticmethod
    def binary_search_range(nums: list[int], target: int) -> tuple[int, int]:
        """
        尋找目標值的起始和結束位置

        Args:
            nums: 已排序的整數列表
            target: 要搜尋的目標值

        Returns:
            tuple[int, int]: 目標值的起始和結束位置，若不存在則返回 (-1, -1)
        """
        if not nums:
            return (-1, -1)

        # 尋找左邊界
        left = BinarySearchTemplate.binary_search_leftmost(nums, target)

        # 如果左邊界超出範圍或值不等於目標值，表示目標值不存在
        if left == len(nums) or nums[left] != target:
            return (-1, -1)

        # 尋找右邊界
        right = BinarySearchTemplate.binary_search_rightmost(nums, target)

        return (left, right)

    @staticmethod
    def binary_search_rotated(nums: list[int], target: int) -> int:
        """
        在旋轉排序數組中搜尋目標值

        Args:
            nums: 旋轉後的排序數組
            target: 要搜尋的目標值

        Returns:
            int: 目標值的索引，若不存在則返回 -1
        """
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # 判斷哪一側是有序的
            if nums[left] <= nums[mid]:  # 左側有序
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 右側有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


def test_binary_search():
    bs = BinarySearchTemplate()

    # 測試基本二分搜尋
    assert bs.basic_binary_search([1, 2, 3, 4, 5], 3) == 2
    assert bs.basic_binary_search([1, 2, 3, 4, 5], 6) == -1

    # 測試最左側搜尋
    assert bs.binary_search_leftmost([1, 2, 2, 2, 3], 2) == 1
    assert bs.binary_search_leftmost([1, 3, 5, 7], 4) == 2

    # 測試最右側搜尋
    assert bs.binary_search_rightmost([1, 2, 2, 2, 3], 2) == 3
    assert bs.binary_search_rightmost([1, 3, 5, 7], 4) == 1

    # 測試最接近值搜尋
    assert bs.binary_search_closest([1, 2, 4, 5], 3) == 1

    # 測試範圍搜尋
    assert bs.binary_search_range([1, 2, 2, 2, 3], 2) == (1, 3)
    assert bs.binary_search_range([1, 2, 3, 4, 5], 6) == (-1, -1)

    # 測試旋轉數組搜尋
    assert bs.binary_search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert bs.binary_search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1

    print("所有測試都通過了！")


if __name__ == "__main__":
    test_binary_search()
