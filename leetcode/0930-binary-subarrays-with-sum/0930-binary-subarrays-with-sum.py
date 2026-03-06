class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        curr = 0
        ans = 0
        for num in nums:
            curr += num
            ans += count[curr - goal]
            count[curr] += 1
        return ans