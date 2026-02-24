class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(c+1):
            if c-(a**2) < 0:
                continue
            b = sqrt(c-(a**2))
            if floor(b) == b:
                return True
        return False