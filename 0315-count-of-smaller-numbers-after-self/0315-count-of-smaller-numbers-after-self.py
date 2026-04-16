class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = (nums[i],i)
        ans = [0]*len(nums)

        def mergesort(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr)//2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])
            return merge(left,right)
        
        def merge(arr1,arr2):
            nonlocal ans
            count = 0
            i,j = 0,0
            temp = []
            # 2,5,7
            # 1,6,8
            # 1 2
            while i < len(arr1) and j < len(arr2):
                if arr1[i][0] > arr2[j][0]:
                    temp.append(arr2[j])
                    count += 1
                    j += 1
                else:
                    temp.append(arr1[i])
                    ans[arr1[i][1]] += count
                    i += 1
            temp.extend(arr1[i:])
            temp.extend(arr2[j:])
            for k in range(i, len(arr1)):
                ans[arr1[k][1]] += count
            return temp

        mergesort(nums)
        return ans


        