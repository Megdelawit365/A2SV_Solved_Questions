class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        i = 0
        for n in nums:
            if n % 2 == 0:
                ans[i] = 0
                i += 1
        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna