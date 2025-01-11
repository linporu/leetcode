from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False

        while True:
            if not head.next:
                return False

            if head.val == "passed":
                return True

            head.val = "passed"
            head = head.next
