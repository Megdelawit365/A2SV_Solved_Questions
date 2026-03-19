# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(r):
            if r == None:
                return TreeNode(val)
            if val > r.val:
                r.right = insert(r.right)
            else:
                r.left = insert(r.left)
            return r
        insert(root)
        return root