# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(r,v):
            if not r:
                return r
            if v < r.val:
                r.left = delete(r.left, v)
            elif v > r.val:
                r.right = delete(r.right, v)
            else:
                if not r.left:
                    return r.right
                elif not r.right:
                    return r.left
                
                temp = inorderSuccessor(r.right)
                r.val = temp.val

                r.right = delete(r.right, temp.val)
            
            return r
        
        def inorderSuccessor(v):
            curr = v
            while curr.left:
                curr = curr.left
            return curr

        return delete(root, key)

