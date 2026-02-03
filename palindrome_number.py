class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left, right = 0, len(x)-1
        while left < right:
            if x[left] != x[right]:
                return False
            right -= 1
            left += 1
        return True
