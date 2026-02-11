class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count_a = Counter(word1)
        count_b = Counter(word2)
        if count_a == count_b:
            return True
        if len(word1) != len(word2):
            return False
        if set(count_a.keys()) != set(count_b.keys()):
            return False
        return sorted(count_a.values()) == sorted(count_b.values())
        