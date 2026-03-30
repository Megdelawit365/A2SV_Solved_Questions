class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = [0]
        chars = ["a","b","c"]
        def build(s):
            if len(s) == n:
                count[0] += 1
                if count[0] == k:
                    return s
                return None
            for char in chars:
                if not s or s[-1] != char:
                    s += char
                    ans = build(s)
                    if ans: return ans
                    s = s[:-1]
            return None
        res = build("")
        if res: return res
        return ""
