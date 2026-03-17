class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)
        for b in bills:
            if b == 10:
                if change[5] == 0:
                    return False
                else:
                    change[5] -= 1
            elif b == 20:
                if (change[5] > 0 and change[10] > 0):
                    change[5] -= 1
                    change[10] -= 1  
                elif (change[5] >= 3):
                    change[5] -= 3             
                else:
                    return False
            change[b] += 1
        return True