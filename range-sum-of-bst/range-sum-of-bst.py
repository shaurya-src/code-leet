# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if node == None:
                return
            
            if low <= node.val <= high:
                self.count += node.val
            
            if node.val > low:
                dfs(node.left)
            
            if node.val < high:
                dfs(node.right)
                
        self.count = 0
        dfs(root)
        return self.count