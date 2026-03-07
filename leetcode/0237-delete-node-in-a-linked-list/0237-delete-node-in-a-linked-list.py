# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp = node.next
        prev = node
        while temp != None:
            prev.val = temp.val
            if temp.next == None:
                prev.next = None
                break
            prev = prev.next
            temp = temp.next
