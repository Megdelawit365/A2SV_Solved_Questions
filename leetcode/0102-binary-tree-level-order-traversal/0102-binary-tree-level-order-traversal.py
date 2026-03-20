# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        ans = [[root.val]]
        while queue:
            size = len(queue)
            temp = []
            for i in range(size):
                curr = queue.pop(0)
                if curr.left: 
                    queue.append(curr.left)
                    temp.append(curr.left.val)
                if curr.right: 
                    queue.append(curr.right)
                    temp.append(curr.right.val)
            if temp:
                ans.append(temp)
        return ans