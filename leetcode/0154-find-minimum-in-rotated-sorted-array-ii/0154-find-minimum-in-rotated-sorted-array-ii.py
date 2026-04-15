class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l < r:
            mid = l + (r - l)//2
            if nums[mid] == nums[r] and mid != r:
                r -= 1
                continue
            if nums[mid] == nums[l] and mid != l:
                l += 1
                continue
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
                
        return nums[l]
        # 5 3 3 3