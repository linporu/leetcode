from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 用 Array 儲存節點值，並利用 Array 資料來創造新的 liked list
class Solution01:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy_ptr = dummy
        node_values = []
        while head:
            node_values.append(head.val)
            head = head.next

        n = len(node_values)
        for i in range(n):
            dummy_ptr.next = ListNode(node_values[n - i - 1])
            dummy_ptr = dummy_ptr.next
        return dummy.next


class Solution02:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """反轉鏈結串列

        使用三個指標來實現反轉:
        1. prev: 指向前一個節點
        2. curr: 指向當前節點
        3. next_temp: 暫存下一個節點

        演算法步驟:
        1. 暫存 curr.next 到 next_temp (避免改變指向後遺失下一個節點)
        2. 將 curr.next 指向 prev (反轉指向)
        3. 將 prev 移到 curr (為下一輪做準備)
        4. 將 curr 移到 next_temp (移動到下一個要處理的節點)

        時間複雜度: O(n) - 需遍歷整個串列一次
        空間複雜度: O(1) - 只需要三個指標變數

        Args:
            head: 鏈結串列的頭節點

        Returns:
            反轉後鏈結串列的新頭節點
        """
        # 處理空串列或只有一個節點的情況
        if not head or not head.next:
            return head

        prev = None
        curr = head

        while curr:
            next_temp = curr.next  # 暫存下一個節點
            curr.next = prev  # 改變指向
            prev = curr  # 移動 prev
            curr = next_temp  # 移動 curr

        return prev
