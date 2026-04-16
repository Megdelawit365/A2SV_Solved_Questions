class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] <= ans[-1]:
                l,r = 0,len(ans)-1
                temp = -1
                while l <= r:
                    mid = l + (r - l)//2
                    if ans[mid] >= nums[i]:
                        temp = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                
                if temp != -1:
                    ans[temp] = nums[i]
            
            else:
                ans.append(nums[i])
            # print(ans)
        return len(ans)