from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 用 Array 儲存資訊，比較首尾是否相同
class Solution01:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        n = len(arr)

        for i in range(n // 2):
            if arr[i] != arr[n - 1 - i]:
                return False
        return True


# 反轉後半鏈
class Solution02:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 快慢指標，先求中點
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 反轉後半鏈表
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # 兩側往中間跑，核對每一個元素
        left = head
        right = prev  # 最後一個元素為 prev，此時 curr 為 None
        while right:
            if left.val != right.val:
                return False
            else:
                left = left.next
                right = right.next
        return True


# 反轉後半鏈 + 還原
class Solution03:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # 快慢指標，先求中點
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 反轉後半鏈表
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # 比較兩半部分
        left = head
        right = prev
        is_palindrome = True  # 儲存結果
        while right:
            if left.val != right.val:
                is_palindrome = False
                break
            left = left.next
            right = right.next

        # 再次反轉後半部分，恢復原始結構
        prev = None
        curr = prev  # prev 是最後一個節點
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        return is_palindrome
