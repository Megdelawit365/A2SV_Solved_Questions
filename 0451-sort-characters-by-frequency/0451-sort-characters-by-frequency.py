class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_char = sorted(count, key=count.get, reverse = True)
        ans = ""
        for c in sorted_char:
            ans += c*count[c]
        return ans