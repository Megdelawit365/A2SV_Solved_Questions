class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set()
        def dfs(i,path):
            if i == len(nums):
                if len(path) >= 2 and tuple(path) not in seen:
                    ans.append(path.copy())
                    seen.add(tuple(path))
                return
            if not path or path[-1] <= nums[i]:
                path.append(nums[i])
                dfs(i+1,path)
                path.pop()
            dfs(i+1,path)
            
        dfs(0,[])
        return ans
