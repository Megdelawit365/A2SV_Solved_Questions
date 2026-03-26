class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def traverse(i,path):
            if i == len(nums):
                ans.add(tuple(path.copy()))
                return
            path.append(nums[i])
            traverse(i+1,path)
            path.pop()
            traverse(i+1,path)
            return
        traverse(0,[])
        return list(ans)