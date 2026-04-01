class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k):
            hours = 0
            for p in piles:
                if p <= k:
                    hours += 1
                else:
                    hours += ceil(p/k)
            return hours <= h
        
        l = 1
        r = max(piles)

        ans = 0
        while l <= r:
            mid = l + (r-l)//2
            if possible(mid):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans
