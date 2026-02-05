class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = set(range(1,len(nums)+1))
        for n in nums:
            if n in ans:
                ans.discard(n)
        return list(ans)
        