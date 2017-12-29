import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Wedge
from rotaryEncoder.helper.slicer import Slices

SEPARATOR_WIDTH = 0.0001


class RingTraveller:
    def __init__(self, n, begin, end):
        self.n = n
        self.tp = None
        self.rp = Slices(n, begin, end)
        self.begin = 0
        self.end = 0
        self.rpHasNext = False
        self.i = 0

    def nextRing(self):
        if self.tp == None:
            self.i += 1
            self.tp = Slices(2 ** self.i, 0, 360)
            self.begin, self.end, self.rpHasNext = self.rp.nextInterval()

        theta1, theta2, hasNext = self.tp.nextInterval();
        if not hasNext:
            self.tp = None

        return self.begin, self.end, theta1, theta2, (hasNext | self.rpHasNext);


class WedgeProvider:

    def __init__(self, n, inner, outer):
        self.count = 0
        self.rt = RingTraveller(n,inner, outer)

    def nextWedge(self, ax):
        begin, end, theta1, theta2, next = self.rt.nextRing()

        colour = self.count % 2
        invertedColour = int(not colour)

        self.count += 1

        print(begin, end, theta1, theta2, colour)
        ax.add_patch(Wedge((0, 0), end, theta1, theta2, width=end-begin, color=str(colour)))

        ax.add_patch(Wedge((0, 0), end, theta1, theta2, width=SEPARATOR_WIDTH, color=str(invertedColour)))
        if self.count == 1 or self.count == 2:
            ax.add_patch(Wedge((0, 0), begin - SEPARATOR_WIDTH, theta1, theta2, width=SEPARATOR_WIDTH,
                               color=str(invertedColour)))

        return next

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
