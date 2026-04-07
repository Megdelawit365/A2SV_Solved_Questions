# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def add(r,lft):
            nonlocal ans
            if not r.left and not r.right:
                if lft:
                    ans += r.val
                return
            
            if r.left: add(r.left,True)
            if r.right: add(r.right,False)

        add(root,False)
        return ans