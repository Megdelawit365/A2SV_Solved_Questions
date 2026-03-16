class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 0
        num = self.fib(n-1) + self.fib(n-2)
        return num
        # f(0) - 0
        # f(1) - 1
        # f(2) =  f(1) + f(0)
        # f
        # 2
        # 0 1
        # fib(2) fib(1)