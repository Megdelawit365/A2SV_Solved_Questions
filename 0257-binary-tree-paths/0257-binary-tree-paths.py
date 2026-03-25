# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        path  = []
        def traverse(r):
            path.append(str(r.val))
            if not r.left and not r.right:
                ans.append(path.copy())
                path.pop()
                return
            if r.left:
                traverse(r.left)
            if r.right:
                traverse(r.right)
            path.pop()
            return
        traverse(root)
        for i in range(len(ans)):
            ans[i] = "->".join(ans[i])
        return ans