# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = [0]
        _map = defaultdict(int)
        _map[0] = 1
        def search(r, prefix):
            if not r:
                return
            prefix += r.val
            ans[0] += _map[prefix - targetSum]
            _map[prefix] += 1
            search(r.left, prefix)
            search(r.right, prefix)
            _map[prefix] -= 1
            prefix -= r.val
            return
        
        search(root,0)
        return ans[0]

