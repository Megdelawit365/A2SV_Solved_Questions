class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # 22
        def play(left, right):
            if left == right:
                return nums[left]
            l = nums[left] - play(left + 1, right)
            r = nums[right] - play(left, right - 1)
            return max(l,r)
        return play(0,len(nums)-1) >= 0
        