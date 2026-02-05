class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = Counter(chars)
        ans = 0
        for word in words:
            count = Counter(word)
            good = True
            for k,v in count.items():
                if k not in freq:
                    good = False
                    break
                if v > freq[k]:
                    good = False
                    break
            if good == True:
                ans += len(word)
        return ans
                


        