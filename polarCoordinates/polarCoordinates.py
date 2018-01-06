"""
https://matplotlib.org/examples/pylab_examples/polar_demo.html
Demo of a line plot on a polar axis.
"""
import numpy as np
import matplotlib.pyplot as plt


# r = np.arange(0, 2, 0.01)
# theta = 2 * np.pi * r

alpha = 30.0
r = [0.0001, 2.0]
theta = [ 2 * np.pi * alpha / 360., 2 * np.pi * alpha / 360.]

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, color = "red")
ax.set_rmax(2)
ax.set_rticks([])  # less radial ticks
# ax.set_xticks(np.pi/180. * np.linspace(0,  360, 16, endpoint=False))
ax.set_xticklabels(['E', '', 'N', '', 'W', '', 'S', ''])
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()