class RandomizedSet:

    def __init__(self):
        self.randomSet  = set()

    def insert(self, val: int) -> bool:
        exists = True
        if val in self.randomSet:
            exists = False
        self.randomSet.add(val)
        return exists

    def remove(self, val: int) -> bool:
        exists = True if val in self.randomSet else False
        self.randomSet.discard(val)
        return exists

    def getRandom(self) -> int:
        return random.choice(list(self.randomSet))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()