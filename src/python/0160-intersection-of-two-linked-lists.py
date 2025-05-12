from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 第一直覺
class Solution01:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        startA, startB = headA, headB
        countA, countB = 0, 0

        # A 先跑到盡頭
        while headA.next:
            headA = headA.next
            countA += 1

        # B 跑到盡頭
        while headB.next:
            headB = headB.next
            countB += 1

        # 檢查是否有交集
        if headA != headB:
            return None

        # 重置回原點
        headA = startA
        headB = startB

        # 讓跑遠的偷跑 gap 步
        gap = countA - countB
        if gap > 0:
            for _ in range(gap):
                headA = headA.next
        elif gap < 0:
            for _ in range(-gap):
                headB = headB.next
        else:
            pass

        # 同步跑
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA


# 交換跑道，讓兩者跑一樣多步
class Solution02:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pA, pB = headA, headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA  # Either intersection node or None
