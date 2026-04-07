# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def count(r):
            if not r:
                return 0
            left = count(r.left)
            right = count(r.right)

            return left + right + 1
        
        return count(root)
        