class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = Counter(nums)
        if k == 1:
            nums.sort()
            for num in reversed(nums):
                if count[num] == 1:
                    return num
        elif n == k:
            return max(nums)
        else:
            temp = []
            if count[nums[-1]] == 1:
                temp.append(nums[-1])
            if count[nums[0]] == 1:
                temp.append(nums[0])
            if temp:
                return max(temp)

        return -1        