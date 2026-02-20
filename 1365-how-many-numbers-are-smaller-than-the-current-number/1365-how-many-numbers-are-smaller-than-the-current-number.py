class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0]*100
        freq = {}
        sumBefore = 0
        for n in nums:
            count[n] += 1
        for i,n in enumerate(count):
            if n != 0:
                freq[i] = sumBefore
                sumBefore += n
        for i in range(len(nums)):
            nums[i] = freq[nums[i]]
        return nums
