class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0]*len(nums)
        for r in requests:
            prefix[r[0]] += 1
            if r[1] < len(nums) - 1:
                prefix[r[1]+1] -= 1

        for i in range(1,len(nums)):
            prefix[i] = prefix[i] + prefix[i-1]
        
        prefix.sort()
        nums.sort()
        for i in range(len(nums)):
            nums[i] *= prefix[i]
        return sum(nums)