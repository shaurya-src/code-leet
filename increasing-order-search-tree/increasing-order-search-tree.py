# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []
        self.getInorder(root, arr)
        res = TreeNode(arr[0])
        node = res
        for i in range(1, len(arr)):
            node.right = TreeNode(val=arr[i])
            node = node.right
        
        return res
        
        
    def getInorder(self, root, arr):
        if root:
            self.getInorder(root.left, arr)
            arr.append(root.val)
            self.getInorder(root.right, arr)
            