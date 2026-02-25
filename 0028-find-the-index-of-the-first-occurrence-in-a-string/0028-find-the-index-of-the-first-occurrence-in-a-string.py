class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for left in range(len(haystack)):
            if haystack[left] == needle[0] and left + len(needle) <= len(haystack) and haystack[left:left+len(needle)] == needle:
                return left
        return -1
            