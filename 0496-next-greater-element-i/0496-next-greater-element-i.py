class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     1-0
    #     3-1
    #     4-2
    #     2-3
        
    # 1 3 4 2
    #     4  -1
    # 1 5 2 3 7
    # 0 0 0 7 0
        prefix = [0] * (len(nums2) + 1)
        prefix[-1] = -1
        for i in range(len(nums2)-1,0,-1):
            if nums2[i] > nums2[i-1]:
                prefix[i] = nums2[i]
            else:
                prefix[i] = prefix[i+1]
        count = {}
        for i,n in enumerate(nums2):
            count[n] = i
        ans = []
        for n in nums1:
            idx = count[n]
            ans.append(prefix[idx+1])

        return ans
