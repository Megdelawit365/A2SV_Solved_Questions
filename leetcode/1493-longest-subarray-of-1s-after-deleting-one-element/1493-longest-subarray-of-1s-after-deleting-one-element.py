class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroCount = 0
        maxLen = 0
        currLen = 0
        i,j = 0,0
        while j < len(nums):
            if nums[j] == 0:
                zeroCount += 1
            while zeroCount > 1:
                if nums[i] == 0:
                    zeroCount -= 1
                i += 1
                currLen -= 1
            currLen += 1
            maxLen = max(maxLen,currLen)
            j += 1
        return maxLen - 1
            