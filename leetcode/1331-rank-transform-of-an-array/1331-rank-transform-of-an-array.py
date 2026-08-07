class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        copy = list(set(arr.copy()))
        copy.sort()
        before = defaultdict(int)
        for i in range(len(copy)):
            before[copy[i]] = i+1
        ans = []
        for a in arr:
            ans.append(before[a])
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna