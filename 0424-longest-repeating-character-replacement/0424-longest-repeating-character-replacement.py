class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        maxCount = 0
        count = defaultdict(int)
        i,j = 0,0
        while j < len(s):
            count[s[j]] += 1
            maxCount = max(maxCount, count[s[j]])
            while len(count) > k+1 or sum(count.values()) - maxCount > k:
                count[s[i]] -= 1
                i += 1
                if count[s[i]] == 0:
                    del count[s[i]]
            maxLen = max(maxLen, j - i + 1)
            j += 1
        return maxLen
