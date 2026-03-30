# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        _map = {}

        for i in range(len(inorder)):
            _map[inorder[i]] = i

        def build(rootIdx, leftIdx, rightIdx):
            if leftIdx > rightIdx:
                return None
            root = TreeNode(preorder[rootIdx])
            idx = _map[preorder[rootIdx]]

            leftSize = idx - leftIdx

            _left = build(rootIdx + 1, leftIdx, idx - 1)
            root.left = _left
            _right = build(rootIdx + leftSize + 1, idx + 1, rightIdx)
            root.right = _right

            return root

        return build(0,0,len(inorder)-1)
        
