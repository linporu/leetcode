from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 儲存過往節點
class Solution01:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        passed = set()

        while head.next:
            if head in passed:
                return head
            passed.add(head)
            head = head.next
