class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        prev = ""
        res = 0
        for char in reversed(s):
            if prev and values[char] < values[prev]:
                res -= values[prev]
                res += values[prev] - values[char]
            else:
                res += values[char]
            prev = char
        return res
