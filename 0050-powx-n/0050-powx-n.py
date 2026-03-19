class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 0
        if n <= 2:
            return x ** n
        def power(num, p):
            if p == 2:
                return num ** p
            elif p % 2 == 0:
                return power(num**2, p//2)
            else:
                return num* power(num, p-1)
        return power(x,n)
        # 2 ^ 10
        # (2 ^ 2)^5
        # 4 * (4) ^ 4
        # 4 * (4 ^ 2) ^ 2
        # 4 * 16 ^ 2

