class FrequencyTracker:

    def __init__(self):
        self.array = []

    def add(self, number: int) -> None:
        self.array.append(number)

    def deleteOne(self, number: int) -> None:
        copy = []
        flag = True
        for a in self.array:
            if a == number and flag:
                flag = False
                continue
            copy.append(a)
        self.array = copy
    def hasFrequency(self, frequency: int) -> bool:
        count = Counter(self.array)
        for k,v in count.items():
            if v == frequency:
                return True
        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)