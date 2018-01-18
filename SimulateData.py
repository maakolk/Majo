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
    SINUS_LENGTH = 50
    arduinoConnection = None

    def __init__(self):
        self.count = -1
        self.arduinoConnection = None

    def getRealData(self):
        if (self.arduinoConnection == None):
            self.arduinoConnection = serial.Serial('com6', 9600)  # Creating our serial object named arduinoData
        while (self.arduinoConnection.inWaiting() == 0):  # Wait here until there is data
            pass  # do nothing
        return float(self.arduinoConnection.readline())  # read the line of text from the serial port

    def getSimulateData(self):
        self.count += 1
        print(self.count)
        return ((math.sin(2 * math.pi * self.count / self.SINUS_LENGTH) + 1) + ( random.random() - 0.5 ) * 0.5 + 0.25) * 20


velocityArray = []
connection = ArduinoConnection()


def update(frame):
    velocity = connection.getSimulateData()
    velocityArray.append(velocity)  # Build our tempF array by appending temp readings
    if (len(velocityArray) > X_LIMIT + 1):  # If you have 50 or more points, delete the first one from the array
        velocityArray.pop(0)  # This allows us to just see the last 50 data points
    ax.clear()
    ax.grid(True)  # Turn the grid on
    ax.set_ylabel('Windgeschwindigkeit')  # Set ylabels
    ax.set_ylim(0, 50)
    ax.set_xlim(0, X_LIMIT)
    ax.plot(velocityArray, 'ro-', label='km/h')
    ax.legend(loc='upper left')  # plot the legend

fig = plt.figure(figsize=(23, 10), dpi=80)
ax = fig.add_subplot(111)
animation = FuncAnimation(fig, update, interval=1, frames=10)
plt.show()
# animation.save('rain.gif', writer='imagemagick', fps=30, dpi=40)
