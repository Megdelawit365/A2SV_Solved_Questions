class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 1,n
        while l <= r:
            mid = l + (r - l)//2
            num = (mid/2) * (mid+1)
            if num <= n:
                l = mid + 1
            else:
                r = mid - 1
        return r