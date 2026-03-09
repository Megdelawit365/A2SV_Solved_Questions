class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = [0]
        curr = 0
        for n in nums:
            curr += n
            prefix.append(curr)
        for i in range(len(nums)+1):
            prefix[i] = prefix[i] % k
        count = Counter(prefix)
        ans = 0
        for p in prefix:
            ans += count[p] - 1
            count[p] -= 1
        return ans