class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l <= r:
            mid = l + (r - l)//2
            if mid == len(nums)-1:
                break
            if nums[mid] < nums[mid+1]:
                print(l,mid,r)
                l = mid + 1
            else:
                print(l,mid,r)
                r = mid - 1
        
        return l