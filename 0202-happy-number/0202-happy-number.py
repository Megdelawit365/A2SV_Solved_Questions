class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            digits = list(str(n))
            squareSum = 0
            for d in digits:
                squareSum += int(d)**2
            if squareSum in seen:
                return False
            if squareSum == 1:
                return True
            seen.add(squareSum)
            n = squareSum


            
        # 1 = 1
        # 2 = 4
        # 3 = 9
        # 4 = 16
        # 5 = 25
        # 6 = 36
        # 7 = 49
        # 8 = 64
        # 9 = 81

        # #8:29
        # 2 
        # 4
        # 16
        # 37
        # 58
        # 89
        # 145
        # 42
        # 20
        # 4