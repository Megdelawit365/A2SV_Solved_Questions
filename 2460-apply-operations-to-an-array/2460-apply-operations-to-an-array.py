class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums[i] = nums[i+1]*2
                nums[i+1] = 0
                i += 2
            else:
                i += 1
        ans = []
        count = 0
        for n in nums:
            if n == 0:
                count += 1
            else:
                ans.append(n)
        ans += [0]*count
        return ans
