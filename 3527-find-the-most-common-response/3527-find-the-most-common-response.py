class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = defaultdict(int)
        for r in responses:
            unique = set(r)
            for u in unique:
                count[u]+=1
        highestFreq = 0
        for k,v in count.items():
            highestFreq = max(highestFreq,v)
        words = []
        for k,v in count.items():
            if v == highestFreq:
                words.append(k)
        if len(words) > 1:
            words.sort()
        return words[0]

            