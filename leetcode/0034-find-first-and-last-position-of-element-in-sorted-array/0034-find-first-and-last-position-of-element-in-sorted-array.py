class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(nums,target):
            l = 0
            r = len(nums) - 1

            ans = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    ans = mid
                    r = mid - 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return ans
        
        def last(nums,target):
            l = 0
            r = len(nums) - 1
            ans = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    ans = mid
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return ans
        
        return [first(nums,target),last(nums,target)]
