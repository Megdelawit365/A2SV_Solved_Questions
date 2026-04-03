# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")

        def dfs(r):
            nonlocal maxSum
            if r == None:
                return 0
            a = dfs(r.left)
            b = dfs(r.right)

            maxSum = max(maxSum, r.val + max(a, 0) + max(b, 0))
            return r.val + max(max(a,b),0) 

        dfs(root)
        return maxSum