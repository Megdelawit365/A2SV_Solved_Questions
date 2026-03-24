class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        curr = 1
        patch = 0
        i = 0

        while curr <= n:
            if i < len(nums) and nums[i] <= curr:
                curr += nums[i]
                i += 1
            else:
                curr += curr
                patch += 1
        
        return patch






        # key idea here is that if I can form all numbers until 
        # a certain number, say 4, and i get an additonal number,
        # say 3, I can add 3 with all numbers less than or equal to 4
        # and get new numbers until 4 + 3 = 7 (1+3, 2+3, 3+3, 4+3).
        # If the additional number is greater than the number we can 
        # currently form, like 5, then we can form 5 by adding the biggest
        # number we can form, 4, to the array and form all numbers until 8.
        # if the number is way bigger, like 10, we can keep on adding the biggest
        # element to the array. Greedy sucks.
