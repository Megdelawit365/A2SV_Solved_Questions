class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        r = target
        while r >= 1:
            if maxDoubles == 0:
                ans += r
                break
            if r % 2 == 0 and r/2  > 1:
                maxDoubles -= 1
                r = r // 2
            else:
                r -= 1
            ans += 1
        return ans - 1
