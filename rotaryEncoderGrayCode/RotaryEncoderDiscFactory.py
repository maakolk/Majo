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
        self.ring = n

    def nextRing(self):
        if self.tp == None:
            self.tp = Slices(2 ** self.n, 0, 360)
            self.begin, self.end, self.rpHasNext = self.rp.nextInterval()
            self.ring = self.ring - 1
            self.segment = -1

        theta1, theta2, hasNext = self.tp.nextInterval();
        if not hasNext:
            self.tp = None

        self.segment = self.segment + 1
        return self.begin, self.end, theta1, theta2, self.ring, self.segment, (hasNext | self.rpHasNext);


class WedgeProvider:

    def __init__(self, n, inner, outer):
        self.count = 0
        self.n = n
        self.rt = RingTraveller(n, inner, outer)

    def grayCode(self, segment):
        return segment ^ (segment >> 1)

    def colour(self, ring, segment):
        return (self.grayCode(segment) >> ring) & 1

    def nextWedge(self, ax):
        begin, end, theta1, theta2, ring, segment, next = self.rt.nextRing()

        self.count += 1

        colour = self.colour(ring, segment);
        invertedColour = int(not colour)


        print(begin, end, theta1, theta2, colour, ring, segment)
        ax.add_patch(Wedge((0, 0), end, theta1, theta2, width=end - begin, color=str(colour)))

        if ring > 0 and colour == self.colour(ring - 1, segment):
            ax.add_patch(Wedge((0, 0), end - SEPARATOR_WIDTH, theta1, theta2, width=SEPARATOR_WIDTH,
                               color=str(invertedColour)))
        if ring == 0 and not invertedColour:
            ax.add_patch(Wedge((0, 0), end - SEPARATOR_WIDTH, theta1, theta2, width=SEPARATOR_WIDTH,
                               color=str(invertedColour)))
        if ring == self.n -1 and not invertedColour:
            ax.add_patch(Wedge((0, 0), begin, theta1, theta2, width=SEPARATOR_WIDTH,
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

fig.savefig("Rotary.jpg", dpi=500)
plt.show()

# Documentation
# =============
# https://en.wikipedia.org/wiki/Rotary_encoder#Ways_of_encoding_shaft_position
# https://de.wikipedia.org/wiki/Gray-Code
# https://matplotlib.org/gallery/api/patch_collection.html#sphx-glr-gallery-api-patch-collection-py
