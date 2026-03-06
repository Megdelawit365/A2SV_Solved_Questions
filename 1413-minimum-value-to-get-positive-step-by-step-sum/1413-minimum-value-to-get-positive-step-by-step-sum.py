class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = []
        curr = 0
        for num in nums:
            curr += num
            prefix.append(curr)
        minNum = min(prefix)
        if (0 - minNum) + 1 <= 0:
            return 1
        else:
            return (0 - minNum) + 1
