class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxLen = 0
        for n in hashset:
            if n-1 in hashset:
                continue
            num = n
            currLen = 1
            while num + 1 in hashset:
                currLen += 1
                num += 1
            maxLen = max(maxLen, currLen)
        return maxLen
        