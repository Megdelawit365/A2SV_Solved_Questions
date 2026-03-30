# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        def search(r):
            if not r:
                return False
            if k - r.val in seen:
                return True
            seen.add(r.val)
            return search(r.left) or search(r.right)
        return search(root)