class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        rangeSum = 0
        numsSum = 0
        for num in nums:
            numsSum += num
        for num in range(len(nums)+1):
            rangeSum += num
        return rangeSum - numsSum
# 3
