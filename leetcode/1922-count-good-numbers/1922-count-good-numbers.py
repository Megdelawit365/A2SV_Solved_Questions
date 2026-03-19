class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # 5^(n) * 4^(n-1)
        def power(num, p):
            result = 1
            while p > 0:
                if p % 2 == 1:
                    result = (result * num) % (10**9 + 7)
                num = (num * num) % (10**9 + 7)
                p = p // 2
            return result
        even, odd = 0, 0
        if n % 2 == 0:
            even = n//2
        else:
            even = (n//2) + 1
        odd = n - even
        return (power(5,even) * power(4,odd)) % (10**9 + 7)
        