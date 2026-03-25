class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        ans = []

        def backtrack(num):
            if len(path) == k:
                ans.append(path.copy())
                return
            for i in range(num,n+1):
                path.append(i)
                backtrack(i+1)
                path.pop()
        
        backtrack(1)
        return ans
                