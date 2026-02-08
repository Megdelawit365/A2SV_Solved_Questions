class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = {}
        for d in cpdomains:
            splitted = d.split(" ")
            count = int(splitted[0])
            temp = "".join(splitted[1:])
            domains = temp.split(".")
            subdomains = []
            string = ""
            for dom in reversed(domains):
                string = dom + string
                subdomains.append(string)
                string = "." + string
            for s in subdomains:
                if s not in hashmap:
                    hashmap[s] = count
                else:
                    hashmap[s] += count
        ans = []
        for k,v in hashmap.items():
            ans.append(f"{v} {k}")
        return ans
