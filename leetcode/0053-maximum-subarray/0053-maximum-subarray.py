class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -10**5
        currSum = -10**5
        for num in nums:
            currSum = max(num, num + currSum)
            maxSum = max(maxSum, currSum)
        return maxSum