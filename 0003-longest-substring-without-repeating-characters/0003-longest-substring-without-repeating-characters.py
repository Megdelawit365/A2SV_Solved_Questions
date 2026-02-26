class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        count = set(s[0])
        left,right = 0,1
        maxLen = 0
        while right < len(s):
            while s[right] in count:
                count.remove(s[left])
                left += 1
            count.add(s[right])
            maxLen = max(maxLen, right-left+1)
            right += 1
        return maxLen