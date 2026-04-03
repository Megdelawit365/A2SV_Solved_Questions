class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n = len(nums1) + len(nums2)
        half = (n+1)//2
        l,r = 0, len(nums1)

        while l <= r:
            mid = l + (r - l)//2
            j = half - mid

            if j < 0 or j > len(nums2):
                if j < 0:
                    r = mid - 1
                else:
                    l = mid + 1
                continue
         
            left1, left2, right1, right2 = float("-inf"), float("-inf"),float("inf"), float("inf")
            
            if mid > 0:
                left1 = nums1[mid - 1]
            if mid < len(nums1):
                right1 = nums1[mid]
            if j > 0:
                left2 = nums2[j-1]
            if j < len(nums2):
                right2 = nums2[j]

            if left1 <= right2 and left2 <= right1:
                if n % 2 != 0:
                    return max(left1, left2)
                else:
                    return (max(left1,left2) + min(right1,right2))/2

            elif left1 > right2:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1

