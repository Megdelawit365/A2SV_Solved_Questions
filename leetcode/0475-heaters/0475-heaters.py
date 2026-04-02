class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        l,r = 0, max(abs(houses[-1] - heaters[0]), abs(heaters[-1] - houses[0]))
        print(r)
        def check(r):
            p = 0
            for i in range(len(houses)):
                while p < len(heaters) and abs(houses[i] - heaters[p]) > r:
                    # print(p)
                    p += 1
                if p==len(heaters) or abs(houses[i] - heaters[p]) > r:
                    return False
            return True

        ans = 0
        while l <= r:
            mid = l + (r - l)//2
            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans
        # 3-0//2 = 1



