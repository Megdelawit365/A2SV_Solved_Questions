class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # 1 2 3 4 5 6 7 8 9
        ans = 0
        piles.sort()
        left, right = 0, len(piles)-1
        while left < right:
            ans += piles[right-1]
            left += 1
            right -= 2
        return ans