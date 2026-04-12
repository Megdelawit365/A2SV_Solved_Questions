class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(string):
            count = 0
            for char in string:
                if char == "(":
                    count += 1
                elif char == ")":
                    if not count:
                        return False
                    count -= 1
            return count == 0

        q = deque([s])
        seen = {s}
        res = []
        flag = False

        while q:
            curr = q.popleft()
            if isValid(curr):
                res.append(curr)
                flag = True
            
            if flag:
                continue

            for i in range(len(curr)):
                if curr[i] != "(" and curr[i] != ")":
                    continue
                nxt = curr[:i] + curr[i+1:]
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)

        return res