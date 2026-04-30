# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return True, 0, float('inf'), float('-inf')
            
            left_valid, left_sum, left_min, left_max = dfs(node.left)
            right_valid, right_sum, right_min, right_max = dfs(node.right)

            if left_valid and right_valid and left_max < node.val < right_min:
                curr_sum = left_sum + right_sum + node.val
                ans = max(ans, curr_sum)

                return True, curr_sum, min(left_min, node.val), max(right_max, node.val)
            
            return False, 0, 0, 0

        dfs(root)
        return ans

            
