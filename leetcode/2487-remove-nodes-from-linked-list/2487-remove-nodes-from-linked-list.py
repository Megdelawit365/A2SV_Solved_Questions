# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head = prev
        temp = prev
        maxNum = temp.val
        while temp:
            if temp.val < maxNum:
                prev.next = temp.next
            else:
                prev = temp
            maxNum = max(maxNum, temp.val)
            temp = temp.next

        prev = None
        curr = head

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
