class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                ans.append(abs(nums[i]))
                continue
            nums[abs(nums[i])-1] *= -1
        
        for i in range(len(nums)):
            if nums[i] >= 0:
                ans.append(i+1)
                break

        return ans

        # 4,8,1,-5,2,7,4,6
