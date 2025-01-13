# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_copy = head
        counter = 0

        while True:
            if head_copy.next:
                counter += 1
                head_copy = head_copy.next
                print(head_copy.val)
            else:
                break

        head_copy = head

        if counter & 1 == 1:
            for _ in range(int((counter + 1) / 2)):
                head_copy = head_copy.next
                
        else:
            for _ in range(int(counter / 2)):
                head_copy = head_copy.next

        return head_copy