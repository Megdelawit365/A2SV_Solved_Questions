class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = defaultdict(lambda:-1)
        stack = []
        for i,num in enumerate(nums2):
            while stack and nums2[stack[-1]] < num:
                count[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        ans = []
        for i in range(len(nums1)):
            ans.append(count[nums1[i]])
        return(ans)
