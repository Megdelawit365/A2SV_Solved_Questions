class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        count1 = Counter(s1)
        count2 = Counter(s2)
        swap = 0
        while(count1):
            if count1["x"] >= 2 and count2["y"] >= 2:
                count1["x"] -= 2
                count2["y"] -= 2
                swap += 1
            elif count1["y"] >= 2 and count2["x"] >= 2:
                count1["y"] -= 2
                count2["x"] -= 2
                swap += 1
            elif count1["x"] == 1 and count1["y"] == 1 and count2["x"] == 1 and count2["y"] == 1:
                count1["y"] -= 1
                count2["x"] -= 1
                count1["x"] -= 1
                count2["y"] -= 1
                swap += 2
            else:
                return -1
            if count1["x"] == 0:
                del count1["x"]
            if count2["x"] == 0:
                del count2["x"]
            if count1["y"] == 0:
                del count1["y"]
            if count2["y"] == 0:
                del count2["y"]
        return swap
                
        return 2

