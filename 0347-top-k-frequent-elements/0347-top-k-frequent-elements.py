class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = Counter(nums)
        for c in count.most_common(k):
            ans.append(c[0])
        return ans
        #5