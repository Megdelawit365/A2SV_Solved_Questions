class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        currSum, ans = 0, 0
        for right in range(len(nums)):
            currSum += nums[right]
            while currSum > k:
                currSum -= nums[left]
                left += 1
            if currSum == k:
                ans += 1
        return ans