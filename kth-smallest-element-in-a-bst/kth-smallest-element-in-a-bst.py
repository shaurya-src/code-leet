# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.k = k
        self.inorder(root, res)
        return res[k-1]
    
    def inorder(self, root, arr):
        if root:
            self.inorder(root.left, arr)
            arr.append(root.val)
            if len(arr) == self.k:
                return
            self.inorder(root.right, arr)
        