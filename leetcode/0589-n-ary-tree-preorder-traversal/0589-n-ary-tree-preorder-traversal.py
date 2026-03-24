"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def traverse(r):
            if r == None:
                return
            ans.append(r.val)
            for child in r.children:
                traverse(child)
        traverse(root)
        return ans

