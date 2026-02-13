class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        posCount, negCount = 0,0
        for n in nums:
            if n > 0:
                posCount += 1
            if n < 0:
                negCount += 1
        return max(posCount, negCount)
        