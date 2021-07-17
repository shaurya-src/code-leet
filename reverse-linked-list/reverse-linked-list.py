# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        itr = head
        while itr != None:
            nxt = itr.next
            itr.next = prev
            prev = itr
            itr = nxt         
        head = prev
        return head