class Solution:
    def countSegments(self, s: str) -> int:
        # if s.strip() == "":
        #     return 0
        # else:
        #     return len(s.split(" "))

        segments = s.split(" ")
        ans = [seg for seg in segments if seg != ""]
        return len(ans)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna