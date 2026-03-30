# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        _map = {}
        n = len(nums)
        for i,num in enumerate(nums):
            _map[num] = i
        def build(l,r):
            if l == r:
                return None
            num = max(nums[l:r])
            idx = _map[num]
            root = TreeNode(num)
            root.left = build(l,idx)
            root.right = build(idx+1,r)
            return root
        return build(0,n)

