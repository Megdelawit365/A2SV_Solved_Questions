# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        path = []
        currSum = 0

        def search(r,currSum,path):
            if not r:
                return
            currSum += r.val
            path.append(r.val)
            if not r.left and not r.right:
                if currSum == targetSum:
                    ans.append(path.copy())
                path.pop()
                return
            l = search(r.left, currSum, path)
            r = search(r.right, currSum, path)

            path.pop()
            return
        
        search(root,currSum,path)
        return ans