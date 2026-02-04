class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums = []
        for r in ranges:
            for n in range(r[0], r[-1]+1):
                nums.append(n)
        for num in range(left, right+1):
            if num not in nums:
                return False
        return True
# 4
