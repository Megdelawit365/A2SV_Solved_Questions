class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        key = ""
        for k,v in count.items():
            if v == 1:
                key = k
                break
        for i, char in enumerate(s):
            if char == key:
                return i
        return -1