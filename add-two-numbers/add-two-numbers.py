# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.get_num(l1)
        b = self.get_num(l2)
        total = str(a+b)[::-1]
        res = ListNode(total[0])
        itr = res
        for i in range(1, len(total)):
            curr = ListNode(total[i])
            itr.next = curr
            itr = itr.next
        
        return res
        
    def get_num(self, ll):
        if not ll:
            return 0
        num = ""
        curr = ll
        while curr:
            num += str(curr.val)
            curr = curr.next
        return int(num[::-1])