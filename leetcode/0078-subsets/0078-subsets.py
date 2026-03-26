class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def traverse(i,path):
            if i == len(nums):
                ans.append(path.copy())
                return
            path.append(nums[i])
            traverse(i+1,path)
            path.pop()
            traverse(i+1,path)
            return
        traverse(0,[])
        return ans
