# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True
        left, right = True, True
        if root.left:
            if root.val <= root.left.val:
                return False
            left =  self.isValidBST(root.left)
        if root.right:
            if root.val >= root.right.val:
                return False
            right =  self.isValidBST(root.right)
        
        if left and right:
            return True
        return False