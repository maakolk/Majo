import math
import random
import serial  # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt  # import matplotlib library
from drawnow import *

X_LIMIT = 50


def makeFig():  # Create a function that makes our desired plot
    plt.ylim(0, 50)  # Set y min and max values
    plt.xlim(0, X_LIMIT)  # Set x min and max values
    plt.title('Wind Diagramm')  # Plot the title
    plt.grid(True)  # Turn the grid on
    plt.ylabel('Windgeschwindigkeit')  # Set ylabels
    plt.plot(velocityArray, 'ro-', label='km/h')  # plot the temperature
    plt.legend(loc='upper left')  # plot the legend

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
        return float(self.arduinoConnection().readline())  # read the line of text from the serial port

    def getSimulateData(self):
        self.count += 1
        return ((math.sin(2 * math.pi * self.count / self.SINUS_LENGTH) + 1) + random.random() * 0.5) * 20

plt.ion()  # Tell matplotlib you want interactive mode to plot live data
plt.figure(figsize=(18, 6), dpi=80)

connection = ArduinoConnection()

velocityArray = []
while True:  # While loop that loops forever
    velocity = connection.getSimulateData()
    velocityArray.append(velocity)  # Build our tempF array by appending temp readings
    if (len(velocityArray) > X_LIMIT + 1 ):  # If you have 50 or more points, delete the first one from the array
        velocityArray.pop(0)  # This allows us to just see the last 50 data points
    drawnow(makeFig)  # Call drawnow to update our live graph
    plt.pause(.000001)  # Pause Briefly. Important to keep drawnow from crashing




