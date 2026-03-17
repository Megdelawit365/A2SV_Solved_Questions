class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                for j in range(3):
                    nums[i + j] = 1 - nums[i + j]
                ans += 1
        if sum(nums) != len(nums):
            return -1
        return ans
            