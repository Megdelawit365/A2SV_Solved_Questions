class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        def subsets(i,path):
            nonlocal ans
            if i == len(nums):
                temp = 0
                for p in path:
                    temp ^= p
                ans += temp
                return
            
            path.append(nums[i])
            subsets(i+1,path)
            path.pop()
            subsets(i+1,path)

        subsets(0,[])

        return ans