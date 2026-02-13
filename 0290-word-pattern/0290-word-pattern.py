class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = {}
        hashmap2 = {}
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        for i in range(len(s)):
            if pattern[i] in hashmap and hashmap[pattern[i]] != s[i] or s[i] in hashmap2 and hashmap2[s[i]] != pattern[i]:
                return False
            hashmap[pattern[i]] = s[i] 
            hashmap2[s[i]] = pattern[i]
        return True