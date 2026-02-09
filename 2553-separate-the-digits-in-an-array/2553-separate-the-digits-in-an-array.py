class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            sep = list(str(n))
            for s in sep:
                ans.append(int(s))
        return ans