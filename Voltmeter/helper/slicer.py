class Slices:
    def __init__(self, slicesCount, begin, end):
        self.remainingSlicesCount = slicesCount
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

    @staticmethod
    def arrangeSlicesIntegerArray(slicesCount, begin, end):
        slicer = Slices(slicesCount, begin, end)
        results = []
        results.append(begin)
        hasNext = True

        while hasNext:
            begin, end, hasNext = slicer.nextInterval()
            results.append(end)

        return results