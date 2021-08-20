# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        itr = root
        flag = False
        while itr != None:
            if val == itr.val:
                return itr
                
            if val > itr.val:
                itr = itr.right
            else:
                itr = itr.left
        
        return None