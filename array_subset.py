# User function Template for python3

class Solution:
    # Function to check if a is a subset of b.
    def isSubset(self, a, b):
        freq = {}
        for num in a:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        for num in b:
            if num not in freq or freq[num] == 0:
                return False
            freq[num] -= 1
        return True
