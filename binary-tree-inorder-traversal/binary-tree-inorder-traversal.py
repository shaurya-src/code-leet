# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse = []
        if root:
            self.travel(root)
        return self.traverse
    
    def travel(self, node):
        if node:
            self.travel(node.left)
            self.traverse.append(node.val)
            self.travel(node.right)