# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        ans = []
        level = 0
        while queue:
            size = len(queue)
            temp = []
            for i in range(size):
                curr = queue.pop(0)
                temp.append(curr.val)
                if curr.left: 
                    queue.append(curr.left)
                if curr.right: 
                    queue.append(curr.right)
            if temp:
                if level % 2 == 1:
                    temp.reverse()
                ans.append(temp)
            level += 1
        return ans