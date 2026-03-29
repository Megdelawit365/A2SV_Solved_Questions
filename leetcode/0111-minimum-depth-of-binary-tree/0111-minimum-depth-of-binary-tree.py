# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        minDep = [float("inf")]
        def search(r, curr):
            if not r:
                return
            curr += 1
            if not r.left and not r.right:
                minDep[0] = min(minDep[0], curr)
                return
            search(r.left, curr)
            search(r.right, curr)
            return
        search(root,0)
        return minDep[0]
