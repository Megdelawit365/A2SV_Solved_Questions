class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 3 4 -5 -1
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums)+1
        
        for i in range(len(nums)):
            if abs(nums[i]) > len(nums):
                continue

            if nums[abs(nums[i])-1] < 0:
                continue
            nums[abs(nums[i])-1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        return len(nums) + 1
            
            


        