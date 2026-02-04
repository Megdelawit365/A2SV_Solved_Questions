class Solution:
    def findUnion(self, a, b):
        freq = {}
        for num in a:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        for num in b:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        union = []
        for key, value in freq.items():
            union.append(key)
        return union
# 9
