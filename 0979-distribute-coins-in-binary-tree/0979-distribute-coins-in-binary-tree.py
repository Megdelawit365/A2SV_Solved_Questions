# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = [0]
        def distribute(r):
            if not r:
                return 0

            _left = distribute(r.left)
            _right = distribute(r.right)

            moves[0] += abs(_left) + abs(_right)
            return _left + _right + r.val - 1
        distribute(root)
        return moves[0]