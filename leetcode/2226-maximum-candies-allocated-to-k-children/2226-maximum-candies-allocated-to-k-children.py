class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l,r = 1, max(candies)
        minC = min(candies)

        while l <= r:
            mid = l + (r-l)//2
            count = 0
            for c in candies:
                if mid > c: continue
                count += c//mid
            if count >= k:
                l = mid + 1
            else:
                r = mid - 1
        
        return l - 1
