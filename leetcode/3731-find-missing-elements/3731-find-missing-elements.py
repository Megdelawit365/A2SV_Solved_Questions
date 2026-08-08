class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        unique = set(nums)
        maxNum = max(nums)
        minNum = min(nums)
        ans = []
        for i in range(minNum+1,maxNum):
            if i not in unique:
                ans.append(i)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna