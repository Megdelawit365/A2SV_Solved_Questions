class Solution:
    def sortSentence(self, s: str) -> str:
        string = s.split(" ")
        ans = sorted(string, key=lambda a: int(a[-1]))
        ans = [a[:-1] for a in ans]
        return " ".join(ans)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna