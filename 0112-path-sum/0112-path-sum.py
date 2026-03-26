# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def search(r,currSum):
            if not r:
                return False
            currSum += r.val
            if not r.left and not r.right:
                return currSum == targetSum
            l = search(r.left, currSum)
            r = search(r.right, currSum)

            return l or r
        
        return search(root, 0)