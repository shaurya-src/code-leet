# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        dec_val = ''
        while head != None:
            dec_val += str(head.val)
            head = head.next
            
        return int(dec_val, 2)