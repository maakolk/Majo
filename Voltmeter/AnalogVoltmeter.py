import math
import random

import serial  # import Serial Library
import numpy  # Import numpy
from drawnow import *
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import FormatStrFormatter

from rotaryEncoder.helper.slicer import Slices

# https://stackoverflow.com/questions/5285912/how-can-i-create-a-frontend-for-matplotlib

FREQUENCIES_SHOW = True
FREQUENCIES_LOG = True

REFRESH_MS = 100
X_LIMIT_MS = 1000
X_TICKS_COUNT = 20

Y_LIMIT_VOLT = 5
Y_CHANNELS = None
Y_TICK_COUNTS = 5

current_milli_time = lambda: int(round(serial.time.time() * 100))

class ArduinoConnection:
    SINUS_LENGTH_FRAMES = 650
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
            for i in range(5):
                self.arduinoConnection.readline()
        return float(self.arduinoConnection.readline())  # read the line of text from the serial port

    def getSimulateData(self):
        self.count += 1
        return ((math.sin(2 * math.pi * self.count / self.SINUS_LENGTH_FRAMES) + 1) + (
                random.random() - 0.5) * 0.5 + 0.25) * 1024.0 / 2.5

    def getData(self):
        return self.getRealData()


timeValues = []
connection = ArduinoConnection()
xTickNames = numpy.linspace(0, X_LIMIT_MS, X_TICKS_COUNT + 1, endpoint=True)
if Y_CHANNELS != None:
    yTickPositions = numpy.linspace(0, Y_CHANNELS, Y_TICK_COUNTS + 1, endpoint=True)
yTickNames = numpy.linspace(0, Y_LIMIT_VOLT, Y_TICK_COUNTS + 1, endpoint=True)
refresh_ms = min(REFRESH_MS, X_LIMIT_MS)


def update(frame):
    start = current_milli_time()
    if len(timeValues) == 0:
        end = start + X_LIMIT_MS
    else:
        end = start + refresh_ms
        skip = int(round(len(timeValues) * refresh_ms / X_LIMIT_MS))
        del timeValues[:skip]
    while current_milli_time() < end:
        analog = connection.getData()
        timeValues.append(analog)
        # print(analog)

    if len(timeValues) < 2:
        return

    makeTimePlot(axt, timeValues)

    if not FREQUENCIES_SHOW:
        return

    hann = numpy.hanning(len(timeValues))
    frequencyValues = numpy.fft.fft(timeValues * hann)
    N = int(len(timeValues) / 2 + 1)
    frequencyValues = numpy.abs(frequencyValues[:N])
    if FREQUENCIES_LOG:
        frequencyValues = numpy.log(frequencyValues + 0.001)

    makeFrequencyPlot(axf, frequencyValues, len(timeValues))


def makeTimePlot(ax, yValues):
    ax.clear()
    ax.grid(True)  # Turn the grid on
    ax.set_ylabel('Voltage in Volt')  # Set ylabels
    ax.set_xlabel('Time in Milli Seconds with ' + str(
        round(len(yValues) / X_LIMIT_MS * 1000)) + ' Data Samples per Second')  # Set ylabels
    if Y_CHANNELS != None:  # Set to None for AutoScale
        ax.set_ylim(0, Y_CHANNELS)
        ax.set_yticks(yTickPositions)
        ax.yaxis.set_ticklabels(yTickNames)
    ax.set_xlim(0, len(yValues) - 1)
    if len(yValues) > 0:  # Avoid divisions by zero
        # xTickPositions = Slices.arrangeSlicesIntegerArray(X_TICKS_COUNT, 0, len(yValues) - 1)
        xTickPositions = numpy.linspace(0, len(yValues) - 1, X_TICKS_COUNT + 1, endpoint=True)
        ax.set_xticks(xTickPositions)
    ax.xaxis.set_ticklabels(xTickNames)
    ax.plot(yValues, 'r-', label='A0')
    ax.legend(loc='upper left')  # plot the legend


def makeFrequencyPlot(ax, yValues, samples):
    ax.clear()
    ax.grid(True)  # Turn the grid on
    ax.set_ylabel('Amplitude')  # Set ylabels
    ax.set_xlabel('Frequency in Kiloherz with ' + str(samples) + ' Samples')

    ax.set_xlim(0, len(yValues) - 1)
    if len(yValues) > 0:  # Avoid divisions by zero
        # xTickPositions = Slices.arrangeSlicesIntegerArray(X_TICKS_COUNT, 0, len(yValues) - 1)
        xTickPositions = numpy.linspace(0, len(yValues) - 1, X_TICKS_COUNT + 1, endpoint=True)
        ax.set_xticks(xTickPositions)
    fMax = 0.5 * samples / X_LIMIT_MS
    xTickNamesF = numpy.linspace(0, fMax, X_TICKS_COUNT + 1, endpoint=True)
    for i in range(0, len(xTickNamesF)):
        xTickNamesF[i] = round(xTickNamesF[i] * 1000) / 1000
    ax.xaxis.set_ticklabels(xTickNamesF)

    for i in range(0, 2):
        yValues[i] = 0
    ax.plot(yValues, 'g-', label='A0')
    ax.legend(loc='upper left')  # plot the legend


fig = plt.figure(figsize=(23, 12), dpi=80)

if not FREQUENCIES_SHOW:
    axt = fig.add_subplot(111)
else:
    axt = fig.add_subplot(211)
    axf = fig.add_subplot(212)

animation = FuncAnimation(fig, update, interval=1, frames=10)
plt.show()
