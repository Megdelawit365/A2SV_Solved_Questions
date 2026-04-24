# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node,path):
            nonlocal ans
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                ans += int("".join(path))
                path.pop()
                return
            dfs(node.right,path)
            dfs(node.left,path)
            path.pop()
        
        dfs(root,[])
        return ans