class Solution:
    def mySqrt(self, x: int) -> int:
        ans = -1
        l,r = 0, x
        while l <= r:
            mid = l + (r - l)//2
            if mid ** 2 > x:
                r = mid - 1
            elif mid ** 2 < x:
                ans = mid
                l = mid + 1
            else:
                return mid
        return ans
        