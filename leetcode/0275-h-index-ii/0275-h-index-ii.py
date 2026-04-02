class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l,r = 1,len(citations)
        ans = 0
        n = len(citations)
        while l <= r:
            mid = l + (r-l) // 2
            h = n - mid
            if citations[mid-1] >= h+1:
                print(mid)
                ans = h + 1
                r = mid - 1
            else:
                l = mid + 1
        return ans
        # 1 + 2 = 3//2 = 1
        # h = 2 - 1 = 1
        # 2 + 2 = 4//2 = 2
        # h = 2 - 2 = 0

