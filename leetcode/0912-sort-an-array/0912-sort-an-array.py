class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left,right)

    def merge(self, arr1, arr2):
        ans = []
        i,j = 0,0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])
                j += 1
        
        for x in range(i,len(arr1)):
            ans.append(arr1[x])
        for x in range(j,len(arr2)):
            ans.append(arr2[x])

        return ans


    
