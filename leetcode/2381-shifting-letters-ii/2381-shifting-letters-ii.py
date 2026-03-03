class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        count = []
        for char in s:
            count.append(ord(char) - ord('a'))
        diff = [0]*len(count)
        for shift in shifts:
            if shift[2] == 0:
                diff[shift[0]] -= 1
                if shift[1] < len(count)-1:
                    diff[shift[1]+1] += 1 
            else:
                diff[shift[0]] += 1
                if shift[1] < len(count)-1:
                    diff[shift[1]+1] -= 1 
        currSum = 0
        for i,d in enumerate(diff):
            currSum += d
            count[i] = (count[i] + currSum) % 26
        ans = ""
        for c in count:
            ans += chr(ord('a')+c)
        return ans
        