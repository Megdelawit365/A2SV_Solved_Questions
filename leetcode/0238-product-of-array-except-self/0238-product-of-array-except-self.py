class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [i for i in nums]

        curr = 1
        for i in range(len(nums)):
            temp = arr[i]
            arr[i] = arr[i] * curr
            curr *= temp
        curr = 1
        for i in range(len(nums)-1,0,-1):
            temp = nums[i]
            arr[i] = arr[i-1] * curr
            curr *= temp
        arr[0] = curr
        return arr
                    
        