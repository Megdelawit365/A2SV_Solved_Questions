class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        # 1 2 2
        maxPerimeter = 0
        for i in range(len(nums)-2):
            if nums[i] * nums[i+1] * nums[i+2] != 0:
                if nums[i] + nums[i+1] > nums[i+2] and nums[i+1] + nums[i+2] > nums[i] and nums[i+2] + nums[i] > nums[i+1]:
                    maxPerimeter = max(maxPerimeter, nums[i] + nums[i+1] + nums[i+2])
        return maxPerimeter
