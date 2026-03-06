class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1

        ans = 0
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            ans +=  freq[prefix-k]
            freq[prefix] += 1
        return ans