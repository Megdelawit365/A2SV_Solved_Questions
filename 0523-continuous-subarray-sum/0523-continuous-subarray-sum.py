class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        prefix = [0]
        curr = 0
        for num in nums:
            curr += num
            prefix.append(curr)
        # return prefix
        for i,p in enumerate(prefix):
            prefix[i] = p % k
        # return prefix
        for i,p in enumerate(prefix):
            prefix[i] = -1
            if p in prefix:
                return True
        return False
        