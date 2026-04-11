class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i,path,total):
            if total == target:
                ans.append(path.copy())
                return
            if total > target or i == len(candidates):
                return
            
            path.append(candidates[i])
            dfs(i,path,total + candidates[i])
            path.pop()
            dfs(i+1,path,total)
        
        dfs(0,[],0)
        return ans