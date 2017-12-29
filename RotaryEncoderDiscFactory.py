class ThetaProvider:
    def __init__(self, n):
        self.divisor = 2 ** n
        self.theta1 = 0
        self.theta2 = 0
        self.remainder = 360

    def nextSector(self):
        self.theta1 = self.theta2
        delta = self.remainder / self.divisor
        self.remainder -= delta
        self.theta2 += delta
        self.divisor -= 1
        return self.theta1, self.theta2, self.divisor > 0


class RingProvider:
    def __init__(self, n):
        self.n = n
        self.i = 0
        self.tp = None

    def nextRing(self):
        if self.tp == None:
            self.i += 1
            self.tp = ThetaProvider(self.i)
        theta1, theta2, hasNext = self.tp.nextSector();
        if not hasNext:
            self.tp = None
        return self.i, theta1, theta2, (hasNext | (self.i < self.n));


next = True
rp = RingProvider(5)
while (next):
    i, theta1, theta2, next = rp.nextRing()
    print(i, theta1, theta2, next)
