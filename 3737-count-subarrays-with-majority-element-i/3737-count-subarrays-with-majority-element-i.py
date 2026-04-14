class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # 0 1 1 0
        # 0 0 1 2 2
        prefix = [0]*(len(nums)+1)
        ans = 0
        for i in range(len(nums)):
            if nums[i] == target:
                prefix[i+1] = prefix[i] + 1
            else:
                prefix[i+1] = prefix[i]
        
        for i in range(1,len(prefix)):
            for j in range(i,len(prefix)):
                count = prefix[j] - prefix[i-1]
                if count * 2 > (j-i+1):
                    ans += 1
        return ans