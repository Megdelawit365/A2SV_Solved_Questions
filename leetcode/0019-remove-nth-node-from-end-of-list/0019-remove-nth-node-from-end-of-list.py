# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp != None:
            temp = temp.next
            size += 1
        prev = head
        if size - n == 0:
            return head.next
        for i in range(size-n-1):
            prev = prev.next
        prev.next = prev.next.next
        return head