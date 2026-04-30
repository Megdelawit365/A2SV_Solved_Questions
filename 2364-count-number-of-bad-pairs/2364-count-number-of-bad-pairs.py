class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        diff = []
        for i,n in enumerate(nums):
            diff.append(n-i)
        count = Counter(diff)
        print(count)
        ans = 0
        good = 0
        for i,j in count.items():
            if j > 1:
                good += (j*(j-1))//2

        n = len(nums)
        total = (n*(n-1))//2
        
        return total - good
        
