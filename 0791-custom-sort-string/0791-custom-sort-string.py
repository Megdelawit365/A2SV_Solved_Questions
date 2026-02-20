class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        ans = ""
        for o in order:
            if o in count:
                ans += o*count[o]
                del count[o]
        for c,v in count.items():
            ans += c*v
        return ans