class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = {}
        players = set()
        for m in matches:
            winners.add(m[0])   
            if m[1] in losers:
                losers[m[1]] += 1
            else:
                losers[m[1]] = 1 
            players.add(m[0])
            players.add(m[1]) 
        ans1 = []
        ans2 = []
        for p in players:
            if p in winners and p not in losers:
                ans1.append(p)
            elif p in losers and losers[p]==1:
                ans2.append(p)
        ans1.sort()
        ans2.sort()
        return [ans1, ans2]

               