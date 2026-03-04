class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        prefix = [0]
        curr = 0
        for num in nums:
            curr += num
            prefix.append(curr)
        for i,p in enumerate(prefix):
            prefix[i] = p % k
        count = defaultdict(list)
        for i,p in enumerate(prefix):
            count[p].append(i)

        for k,v in count.items():
            if v[-1] - v[0] >=2:
                return True 
        return False
        