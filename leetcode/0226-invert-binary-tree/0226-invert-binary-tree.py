# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(r):
            if not r:
                return None
            if not r.left and not r.right:
                return r
            left = invert(r.left)
            right = invert(r.right)

            r.left = right
            r.right = left

            return r
        
        invert(root)
        return root

            