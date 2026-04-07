# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return []
        queue = [root]
        while queue:
            size = len(queue)
            temp = []
            for i in range(size):
                curr = queue.pop(0)
                if curr.left: 
                    queue.append(curr.left)
                    temp.append(curr.left.val)
                else:
                    temp.append(None)
                if curr.right: 
                    queue.append(curr.right)
                    temp.append(curr.right.val)
                else:
                    temp.append(None)
            if temp and temp != list(reversed(temp)):
                return False
            if temp:
                print(temp)

        return True

