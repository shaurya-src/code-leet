# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ar = []
        itr = head
        while itr != None:
            ar.append(itr.val)
            itr = itr.next
        
        return ar == ar[::-1]