import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Wedge

SEPARATOR_WIDTH = 0.0001


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


class WedgeProvider:
    def __init__(self, n, inner, outer):
        self.n = n
        self.inner = inner
        self.rp = None
        self.width = (outer - self.inner) / n
        self.count = 0

    def nextWedge(self, ax):
        if self.rp == None:
            self.rp = RingProvider(self.n)

        i, theta1, theta2, next = self.rp.nextRing()

        colour = self.count % 2
        invertedColour = int(not colour)

        self.count += 1

        r = self.inner + self.width * i

        print(r, theta1, theta2, self.width, colour)
        ax.add_patch(Wedge((0, 0), r, theta1, theta2, width=self.width, color=str(colour)))

        ax.add_patch(Wedge((0, 0), r, theta1, theta2, width=SEPARATOR_WIDTH, color=str(invertedColour)))
        if i == 1:
            ax.add_patch(Wedge((0, 0), self.inner - SEPARATOR_WIDTH, theta1, theta2, width=SEPARATOR_WIDTH, color=str(invertedColour)))

        return next


# Test1
# next = True
# rp = RingProvider(5)
# while (next):
#     i, theta1, theta2, next = rp.nextRing()
#     print(i, theta1, theta2, next)

# Test2
# fig = plt.figure(figsize=(12, 12), dpi=80)
# ax = fig.add_subplot(111)
# ax.set_xlim(-1,1)
# ax.set_ylim(-1,1)
#
# ax.add_patch(Wedge((0, 0), 1, 0, 360, width=0.1, color='0'))
# ax.add_patch(Wedge((0, 0), 0.9, 0, 360, width=0.1, color='0.2'))
#
# plt.show()

fig = plt.figure(figsize=(12, 12), dpi=80)
ax = fig.add_subplot(111)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

next = True
wp = WedgeProvider(5, 0.2, 1.0)
while (next):
    next = wp.nextWedge(ax)

plt.show()

# Documentation
# =============
# https://en.wikipedia.org/wiki/Rotary_encoder#Ways_of_encoding_shaft_position
# https://matplotlib.org/gallery/api/patch_collection.html#sphx-glr-gallery-api-patch-collection-py