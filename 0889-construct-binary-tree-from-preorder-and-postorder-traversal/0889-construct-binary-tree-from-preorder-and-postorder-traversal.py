# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        _map = {}
        for i in range(len(postorder)):
            _map[postorder[i]] = i

        def build(preL,preR,posL,posR):
            if preL == preR:
                return TreeNode(preorder[preL])
            if preL > preR:
                return None
            root = TreeNode(preorder[preL])
            idx = _map[preorder[preL + 1]]
            leftSize = idx - posL + 1
            root.left = build(preL + 1, preL + leftSize, posL, idx)
            root.right = build(preL + leftSize + 1, preR, idx + 1, posR - 1)
            return root
        
        return build(0, len(preorder)-1, 0, len(postorder)-1)

        # preorder: root -> left -> right
        # postorder: left -> right -> root

        