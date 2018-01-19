import math
import random

import serial  # import Serial Library
import numpy  # Import numpy
from drawnow import *
from matplotlib.animation import FuncAnimation
from Voltmeter.helper.slicer import Slices

# https://stackoverflow.com/questions/5285912/how-can-i-create-a-frontend-for-matplotlib

X_LIMIT_MS = 2000.0
Y_LIMIT_VOLT = 5
X_TICKS_COUNT = 20
REFRESH_MS = 100.0
current_milli_time = lambda: int(round(serial.time.time() * 1000))


class ArduinoConnection:
    SINUS_LENGTH_FRAMES = 100
    arduinoConnection = None

    def __init__(self):
        self.count = -1
        self.arduinoConnection = None

    def getRealData(self):
        first = False
        if (self.arduinoConnection == None):
            self.arduinoConnection = serial.Serial('com4', 9600)  # Creating our serial object named arduinoData
            first = True
        while (self.arduinoConnection.inWaiting() == 0):  # Wait here until there is data
            pass  # do nothing
        if first:
            for i in range(50):
                self.arduinoConnection.readline()
        return float(self.arduinoConnection.readline())  # read the line of text from the serial port

    def getSimulateData(self):
        self.count += 1
        return ((math.sin(2 * math.pi * self.count / self.SINUS_LENGTH_FRAMES) + 1) + (
                random.random() - 0.5) * 0.5 + 0.25) * 1023.0 / 2.5

    def getData(self):
        return self.getRealData()


analogInputArray = []
connection = ArduinoConnection()
xTickNames = numpy.arange(0, X_LIMIT_MS, X_LIMIT_MS / X_TICKS_COUNT)


def update(frame):
    start = current_milli_time()
    if len(analogInputArray) == 0:
        end = start + X_LIMIT_MS
    else:
        end = start + REFRESH_MS
        skip = int(round(len(analogInputArray) * REFRESH_MS / X_LIMIT_MS))
        del analogInputArray[:skip]
    currentTime = 0
    while currentTime < end:
        analog = connection.getData() / 1023.0 * 5.0  # Norm to 5 V
        print(analog)
        analogInputArray.append(analog)
        currentTime = current_milli_time()

    ax.clear()
    ax.grid(True)  # Turn the grid on
    ax.set_ylabel('Voltage in Volt')  # Set ylabels
    ax.set_xlabel('Time in Milli Seconds with ' + str(
        round(len(analogInputArray) / X_LIMIT_MS * 1000)) + ' Data Samples per Second')  # Set ylabels
    if Y_LIMIT_VOLT != None:
        ax.set_ylim(0, 5)  # Comment out for AutoScale
    ax.set_xlim(0, len(analogInputArray) - 1)
    if len(analogInputArray) > 0:
        xTickPositions = Slices.arrangeSlicesIntegerArray(X_TICKS_COUNT, 0, len(analogInputArray) - 1)
        ax.set_xticks(xTickPositions)
    ax.xaxis.set_ticklabels(xTickNames)
    ax.plot(analogInputArray, 'r-', label='A0')
    ax.legend(loc='upper left')  # plot the legend


fig = plt.figure(figsize=(23, 10), dpi=80)
ax = fig.add_subplot(111)
animation = FuncAnimation(fig, update, interval=1, frames=10)
plt.show()
