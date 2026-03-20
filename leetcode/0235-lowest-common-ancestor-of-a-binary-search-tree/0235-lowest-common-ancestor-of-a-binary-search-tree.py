# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # case1 : p and q on either sides of node
        # case2 : p and q on same side of node
        # case3 : p child of q or vice versa

        if (p.val > root.val and q.val < root.val) or (p.val < root.val and q.val > root.val):
            return root
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif root.val == p.val or root.val == q.val:
            return root