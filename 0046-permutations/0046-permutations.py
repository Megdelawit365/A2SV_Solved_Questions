class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []
        n = len(nums)
        def backtrack(nums):
            if len(path) == n:
                ans.append(path.copy())
                return
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(nums[:i] + nums[i+1:])
                path.pop()
            
        backtrack(nums)
        return ans