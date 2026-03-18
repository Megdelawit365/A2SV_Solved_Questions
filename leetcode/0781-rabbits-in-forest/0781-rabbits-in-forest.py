class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for k,v in count.items():
            if k == 0:
                ans += v
            else:
                # ans += k + 1
                # ans += ((v + k)//(v+1)) * (v+1)
                if v <= k + 1:
                    ans += k + 1
                else:
                    groups = math.ceil(v / (k + 1))
                    ans += groups * (k + 1)
        return ans