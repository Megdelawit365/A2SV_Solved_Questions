class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            if n == 1:
                return 1
            else:
                return -1
        graph = defaultdict(list)
        for e in trust:
            graph[e[0]].append(e[1])

        count = 0
        ans = 0
        for i in range(1,n+1):
            if not graph[i]:
                count += 1
                ans = i
        if count == 1:
            return ans
        return -1