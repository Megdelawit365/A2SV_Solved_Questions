class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = 0,1
        if len(nums) < 2:
            return
        while right < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                right += 1
                left += 1
            elif nums[left] ==0 and nums[right] == 0:
                right += 1
            else:
                left += 1
                right += 1
            # 1 0 0 3 12
        