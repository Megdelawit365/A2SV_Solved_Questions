class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        nums = list(range(1,10))
        def build(s,i,used):
            if len(s) == n + 1:
                return s
            for num in nums:
                if num in used:
                    continue
                elif not s:
                    s += str(num)
                    used.add(num)
                else:
                    if pattern[i-1] == "I" and num > int(s[-1]):
                        s += str(num)
                        used.add(num)
                    elif pattern[i-1] == "D" and num < int(s[-1]):
                        s += str(num)
                        used.add(num)
                    else:
                        continue
                res = build(s,i+1,used)
                if res: return res
                used.remove(int(s[-1]))
                s = s[:-1]
        return build("",0,set())
            
