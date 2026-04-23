"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        imp = defaultdict(int)
        sub = defaultdict(list)
        ans = 0

        for e in employees:
            imp[e.id] = e.importance
            sub[e.id] = e.subordinates 

        def dfs(node):
            nonlocal ans
            ans += imp[node]
            for s in sub[node]:
                dfs(s)
        
        
        for i,j in sub.items():
            if i == id:
                dfs(i)
        
        return ans