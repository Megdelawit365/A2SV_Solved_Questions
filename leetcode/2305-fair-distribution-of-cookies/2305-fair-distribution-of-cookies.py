class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        def distribute(child, i):
            # base case
            nonlocal ans
            if i == len(cookies):
                ans = min(ans, max(child))
                return
            for j in range(len(child)):
                child[j] += cookies[i]
                if child[j] < ans:
                    distribute(child, i + 1)
                child[j] -= cookies[i]
            
            return
        
        distribute([0 for i in range(k)], 0)
        return ans