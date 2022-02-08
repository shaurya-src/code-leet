# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dct = {}
        max_twin = 0
        idx = 0
        while (head != None):
            dct[idx] = head.val
            idx += 1
            head = head.next
        
        n = idx - 1
        
        for key, value in dct.items():
            curr = value + dct[n-key]
            max_twin = max(max_twin, curr)
        
        return max_twin
            