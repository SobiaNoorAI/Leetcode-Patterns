# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        
        def dfs(node, a):
            if not node:
                return
            
            a = a * 10 + node.val

            if not node.left and not node.right:
                self.result += a
                return
            
            dfs(node.left, a)
            dfs(node.right, a)

        dfs(root, 0)
        return self.result