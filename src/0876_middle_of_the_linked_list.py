from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution01:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        counter = 0

        # 數總共有幾個 node
        while ptr:
            counter += 1
            ptr = ptr.next

        # 重置指針，讓它跑到中間
        ptr = head
        for _ in range(counter // 2):
            ptr = ptr.next

        return ptr


# 快慢指針
class Solution02:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
