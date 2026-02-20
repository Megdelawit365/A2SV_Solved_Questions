class Solution:
    def smallestPalindrome(self, s: str) -> str:
        string = list(set(s))
        count = Counter(s)
        ans = ""
        mid = ""
        for c,v in count.items():
            if v%2 != 0:
                mid = c
            ans += c*(v//2)
            v-=v//2
        
        ans = "".join(sorted(ans))
        res = ans + mid + ans[::-1]
        return res