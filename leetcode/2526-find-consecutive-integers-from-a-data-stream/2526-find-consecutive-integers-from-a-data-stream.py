class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = deque()
        self.val = value
        self.k = k
        self.count = 0

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        if num == self.val:
            self.count += 1
        while len(self.stream) > self.k:
            if self.stream.popleft() == self.val:
                self.count -= 1
        if self.count == self.k:
            return True
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)