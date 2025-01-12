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


# Two pointers
class Solution02:
    """
    ## 解題步驟：
    1. 使用快慢指針找到相遇點
    2. 將其中一個指針重置到起點
    3. 兩個指針同速前進直到相遇，相遇點即為環的入口

    ## 解題思路
    當快慢指針相遇時：
    慢指針走了：x + y 步
    快指針走了：x + y + n(y + z) 步，其中 n 是圈數
    因為快指針速度是慢指針的兩倍，所以 2(x + y) = x + y + n(y + z)
    從這個等式可以推導出 x = (n-1)(y + z) + z
    特別是當 n = 1 時 x = z
    這告訴我們，從起點到環的入口的距離(x)等於從相遇點到環的入口的距離(z)
    如果我們在快慢指針相遇後，讓一個指針回到起點，另一個留在相遇點，然後兩個指針都以相同速度（每次走 1 步）前進
    兩者就會在環的入口相遇
    """

    def detectCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return None

        # 初始化指針
        slow = head
        fast = head

        # 第一階段：找相遇點
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # 找到相遇點
                # 第二階段：找環的入口
                slow = head  # 重置慢指針到起點
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None  # 沒有環或到達尾端
