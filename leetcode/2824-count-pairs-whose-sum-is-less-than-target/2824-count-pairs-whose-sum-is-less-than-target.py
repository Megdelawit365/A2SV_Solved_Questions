class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        seen = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i: continue
                if nums[i] + nums[j] < target:
                    ans += 1
                    seen.add((min(i,j),max(i,j)))
        return len(seen)