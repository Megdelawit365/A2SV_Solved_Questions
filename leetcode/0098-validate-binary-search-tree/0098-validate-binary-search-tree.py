# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def compare(r, low, high):
            if not r:
                return True
            if r.val <= low or r.val >= high:
                return False
            right = compare(r.right, r.val, high)
            left = compare(r.left, low, r.val)

            return right and left
        
        return compare(root, float('-inf'), float('inf'))