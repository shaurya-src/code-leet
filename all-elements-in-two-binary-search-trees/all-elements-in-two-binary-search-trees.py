# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ar1 = []
        ar2 = []
        self.inorder(root1, ar1)
        self.inorder(root2, ar2)
        
        return sorted(ar1+ar2)
    
    def inorder(self, root, ar):
        if root:
            self.inorder(root.left, ar)
            ar.append(root.val)
            self.inorder(root.right, ar)