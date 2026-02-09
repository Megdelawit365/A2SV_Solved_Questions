class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        ans = []
        evenSum q[0] q[1] nums       ans
        6       1    0    [1,2,3,4]  []
        6       1    0    [1,2,3,4]  []
        for n in nums:
            if n%2 == 0:
                evenSum += n
        for q in queries:
            nums[q[1]] += q[0]
            if nums[q[1]] % 2 == 0:
                evenSum += nums[q[1]]
            else:
                evenSum -= nums[q[1]] - q[0]
            ans.append(evenSum)
        return ans

        