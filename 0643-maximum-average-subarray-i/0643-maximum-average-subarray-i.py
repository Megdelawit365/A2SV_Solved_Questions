class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = float('-inf')
        left,right = 0,k-1
        currSum = sum(nums[left:right])
        while right < len(nums):
            currSum += nums[right]
            maxAvg = max(maxAvg,currSum/k)
            currSum -= nums[left]
            right += 1
            left += 1
        return maxAvg