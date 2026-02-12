class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums)
        dominant = count.most_common(1)[0][0]
        freq = count[dominant]
        countLeft = 0
        for i,n in enumerate(nums):
            if n == dominant:
                countLeft += 1
            countRight = freq - countLeft
            if countLeft * 2 > i + 1 and countRight * 2 > len(nums) - i - 1:
                return i
        return -1