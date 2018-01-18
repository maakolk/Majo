import math
import random

import patch as patch
import serial  # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt  # import matplotlib library
from drawnow import *
from matplotlib.animation import FuncAnimation

# https://stackoverflow.com/questions/5285912/how-can-i-create-a-frontend-for-matplotlib

X_LIMIT_MS = 2000.0
REPEAT_MS = 100.0
current_milli_time = lambda: int(round(serial.time.time() * 1000))

class ArduinoConnection:
    SINUS_LENGTH_FRAMES = 100
    arduinoConnection = None

    def __init__(self):
        self.count = -1
        self.arduinoConnection = None

    def getRealData(self):
        if (self.arduinoConnection == None):
            self.arduinoConnection = serial.Serial('com4', 9600)  # Creating our serial object named arduinoData
        while (self.arduinoConnection.inWaiting() == 0):  # Wait here until there is data
            pass  # do nothing
        return float(self.arduinoConnection.readline())  # read the line of text from the serial port

    def getSimulateData(self):
        self.count += 1
        return ((math.sin(2 * math.pi * self.count / self.SINUS_LENGTH_FRAMES) + 1) + (
                random.random() - 0.5) * 0.5 + 0.25) * 1024.0 / 2.5

analogInputArray = []
connection = ArduinoConnection()

def update(frame):
    xValues = []
    start = current_milli_time()
    if len(analogInputArray) == 0:
       end = start + X_LIMIT_MS
    else:
       end = start + REPEAT_MS
       del analogInputArray[:int(round(len(analogInputArray) * REPEAT_MS / X_LIMIT_MS))]
    while current_milli_time() < end:
         analog = connection.getSimulateData() / 1024.0 * 5.0
         print(analog)
         analogInputArray.append(analog)  # Norm to 5 V
    ax.clear()
    ax.grid(True)  # Turn the grid on
    ax.set_ylabel('Voltage in Volt')  # Set ylabels
    ax.set_xlabel('Time in Milli Seconds with ' + str(round(len(analogInputArray) / X_LIMIT_MS * 1000)) + ' Frames per Second')  # Set ylabels
    ax.set_ylim(0, 5)
    ax.set_xlim(0, X_LIMIT_MS)
    ax.plot(analogInputArray, 'r-', label='A0')
    ax.legend(loc='upper left')  # plot the legend


fig = plt.figure(figsize=(23, 10), dpi=80)
ax = fig.add_subplot(111)
animation = FuncAnimation(fig, update, interval=1, frames=10)
plt.show()
# animation.save('rain.gif', writer='imagemagick', fps=30, dpi=40)
