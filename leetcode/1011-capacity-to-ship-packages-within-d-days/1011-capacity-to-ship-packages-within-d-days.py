class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(weight):
            _days = 1
            curr = 0
            for w in weights:
                if curr + w > weight:
                    _days += 1
                    curr = w
                else:
                    curr += w
            return _days <= days
        
        l = max(weights)
        r = sum(weights)

        ans = 0
        while l <= r:
            mid = l + (r-l)//2
            if possible(mid):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans