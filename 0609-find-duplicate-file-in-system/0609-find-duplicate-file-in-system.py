class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = {}
        for p in paths:
            directory = p[0:4]
            j = 4
            while j < len(p):
                if p[j] == "/":
                    directory += p[j]
                    directory += p[j+1]
                elif p[j] == " ":
                    break
                j+=2
            i = j+1
            Open = False
            name = ""
            while i < len(p):
                content = ""
                if i+1 < len(p) and p[i+1:i+5] == ".txt":
                    num = name + p[i]
                    name = ""
                    i+=6
                    while p[i] != ")":
                        content += p[i]
                        i+=1
                    path = f"{directory}/{num}.txt"
                    if content in hashmap:
                        hashmap[content].append(path)
                    else:
                        hashmap[content] = [path]
                    i+=1
                else:
                    if p[i] != " ":
                        name+=p[i]
                    i+=1
        ans = []
        for k,v in hashmap.items():
            if len(v) > 1:
                ans.append(v)
        return ans

