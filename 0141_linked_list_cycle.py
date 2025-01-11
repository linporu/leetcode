from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 標記法
class Solution01:
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


# 快慢指針法
class Solution02:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next        # 移動一步
            fast = fast.next.next   # 移動兩步

        return True
