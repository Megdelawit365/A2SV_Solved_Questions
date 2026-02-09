class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for n in range(1,num+1):
            string = str(n)
            splitted = []
            for s in string:
                splitted.append(int(s))
            Sum = sum(splitted)
            if Sum % 2 == 0:
                count += 1
        return count
            