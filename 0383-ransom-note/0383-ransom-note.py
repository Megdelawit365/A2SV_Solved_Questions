class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count1 = Counter(ransomNote)
        count2 = Counter(magazine)
        for char in ransomNote:
            if count1[char] > count2[char]:
                return False
        return True