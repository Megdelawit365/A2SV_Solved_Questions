class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        diff = []
        for i,n in enumerate(nums):
            rev = int("".join(reversed(str(n))))
            diff.append(n-rev)
        print(Counter(nums))
        count = Counter(diff)
        print(count)
        good = 0
        for i,j in count.items():
            good += (j*(j-1))//2
        
        return good % (10**9 + 7)