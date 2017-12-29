class Slices:
    def __init__(self, slicescount, begin, end):
        self.remainingSlicesCount = slicescount
        self.begin = begin
        self.end = begin
        self.remainder = end - begin

    def nextInterval(self):
        self.begin = self.end
        delta = self.remainder / self.remainingSlicesCount
        self.remainder -= delta
        self.end += delta
        self.remainingSlicesCount -= 1
        return self.begin, self.end, self.remainingSlicesCount > 0