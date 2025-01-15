from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """重要概念：鏈表節點的 .next 存取安全性

        在不同程式語言中，存取空指針的行為有所不同：

        1. Python 的特殊行為:
            - 節點存在但 .next 是 None（安全操作）:
                node = ListNode(1)  # node.next 預設為 None
                node = node.next    # node 會變成 None
            - 節點本身就是 None（危險操作）:
                node = None
                node = node.next    # AttributeError: 'NoneType' object has no attribute 'next'

        2. 其他語言的行為:
            - Java:
                node = null
                node = node.next    # NullPointerException
            - C++:
                node = nullptr
                node = node->next   # Undefined behavior
            - JavaScript:
                node = null
                node = node.next    # TypeError
                node = node?.next   # 使用可選鏈接運算符，結果為 undefined
            - Go:
                node = nil
                node = node.Next    # panic: nil pointer dereference

        因此在 Python 中處理鏈表時：
        1. 需要檢查：節點本身是否存在 (if node)
        2. 不需要檢查：節點的 .next 是否存在
        """
        # Create a dummy head
        dummy = ListNode(0)
        current = dummy

        # link the least value node
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # After complete one link, attach the remaining nodes directly
        current.next = list1 if list1 else list2

        return dummy.next
