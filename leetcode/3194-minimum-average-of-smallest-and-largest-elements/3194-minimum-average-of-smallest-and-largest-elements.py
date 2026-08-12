class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg = []
        nums.sort()
        left, right = 0, len(nums)-1
        for i in range(len(nums)//2):
            avg.append((nums[left] + nums[right])/2)
            left += 1
            right -= 1
        
        return min(avg)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna