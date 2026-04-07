class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l,r = 0,0
        while l < len(s) and r < len(t):
            if t[r] == s[l]:
                l += 1
            r += 1
        
        if l < len(s):
            return False
        return True