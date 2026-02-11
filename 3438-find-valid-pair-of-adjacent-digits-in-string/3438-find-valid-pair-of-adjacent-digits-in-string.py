class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)
        for i in range(1,len(s)):
            if count[s[i]] == int(s[i]) and count[s[i-1]] == int(s[i-1]) and s[i] !=  s[i-1]:
                return s[i-1] + s[i]
        return ""