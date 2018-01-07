import math
import random

import patch as patch
import serial  # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt  # import matplotlib library
from drawnow import *
from matplotlib.animation import FuncAnimation

X_LIMIT = 100

class ArduinoConnection:
    arduinoConnection = None

    def __init__(self):
        self.count = -1
        self.arduinoConnection = None

    def getRealData(self):
        if (self.arduinoConnection == None):
            self.arduinoConnection = serial.Serial('com6', 9600)  # Creating our serial object named arduinoData
        while (self.arduinoConnection.inWaiting() == 0):  # Wait here until there is data
            pass  # do nothing
        return int(self.arduinoConnection().readline())  # read the line of text from the serial port

    def getSimulateData(self):
        self.count += 1
        self.count = self.count % 40
        print(self.count)
        return self.count


connection = ArduinoConnection()

def update(frame):
    angle = connection.getSimulateData()  # change to:  .getRealData()
    alphaRad = 2 * numpy.pi * angle / 40.

    r = [0.0001, 1.9]
    theta = [alphaRad, alphaRad]

    ax = plt.subplot(111, )
    ax.clear()
    ax.plot(theta, r, color="red")
    ax.set_rmax(2)
    ax.set_rticks([])  # less radial ticks
    ax.set_xticklabels(['E', 'NE', 'N', 'NW', 'W', 'SW', 'S', 'SE'])

fig = plt.figure(figsize=(10, 10), dpi=80)
ax = fig.add_subplot(111, projection='polar')
animation = FuncAnimation(fig, update, interval=500, frames=10) # change to: interval=1
plt.show()