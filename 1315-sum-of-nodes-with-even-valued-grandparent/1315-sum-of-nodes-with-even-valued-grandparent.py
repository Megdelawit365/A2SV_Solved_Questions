# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        ans = []
        def search(parent, grandP, r):
            if not r:
                return
            if not parent:
                search(r,None,r.left)
                search(r,None,r.right)
            elif not grandP:
                search(r,parent,r.left)
                search(r,parent,r.right)
            else:
                if grandP.val % 2 == 0:
                    ans.append(r.val)
                search(r,parent,r.left)
                search(r,parent,r.right)
            return
        search(None,None,root)
        return sum(ans)


        