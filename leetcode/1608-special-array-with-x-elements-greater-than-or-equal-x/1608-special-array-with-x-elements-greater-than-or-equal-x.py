class Solution:
    def specialArray(self, nums: List[int]) -> int:
        prefix = [0]*1001
        for n in nums:
            prefix[n] += 1
        for i in range(1,1001):
            prefix[i] = prefix[i] + prefix[i-1]
        for i in range(1,len(nums)+1):
            if prefix[-1] - prefix[i-1] == i:
                return i
        return -1
