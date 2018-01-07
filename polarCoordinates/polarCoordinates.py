"""
https://matplotlib.org/examples/pylab_examples/polar_demo.html
Demo of a line plot on a polar axis.
"""
import numpy as np
import matplotlib.pyplot as plt


# r = np.arange(0, 2, 0.01)
# theta = 2 * np.pi * r

alpha = 30.0
alphaRad = 2 * np.pi * alpha / 360.

r = [0.0001, 2.0]
theta = [alphaRad, alphaRad]

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, color = "red")
ax.set_rmax(2)
ax.set_rticks([])  # less radial ticks
# ax.set_xticks(np.pi/180. * np.linspace(0,  360, 16, endpoint=False))
# ax.set_xticklabels(['E', '', 'N', '', 'W', '', 'S', ''])


xT=plt.xticks()[0]
xL=['0',r'$\frac{\pi}{4}$',r'$\frac{\pi}{2}$',r'$\frac{3\pi}{4}$',\
    r'$\pi$',r'$\frac{5\pi}{4}$',r'$\frac{3\pi}{2}$',r'$\frac{7\pi}{4}$']
plt.xticks(xT, xL)

ax.grid(True)

plt.show()