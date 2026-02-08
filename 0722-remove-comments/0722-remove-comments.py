class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        # [
        # "/*Test program */", 
        # "int main()", 
        # "{ ", 
        # "  // variable declaration ",
        #  "int a, b, c;", 
        #"/* This is a test",
        #   "   multiline  ",
        #    "   comment for ",
        #     "   testing */",
        #      "a = b + c;",
        #       "}"
        #       ]
        ans = []
        closed = True
        multiline = ""
        for s in source:
            line = ""
            if "/*" in s:
                if "*/" in s:
                    continue
                else:
                    closed = False
                    index = s.index("/*")
                    multiline += s[0:index]
            elif closed == True:
                if "//" in s:
                    index = s.index("//")
                    line += s[0:index]
                else:
                    line += s
            elif "*/" in s and closed == False:
                index = s.index("*/")
                multiline += s[index+2:]
                line = multiline
                multiline = ""
                closed = True
            if line != "":
                ans.append(line)
        return ans
