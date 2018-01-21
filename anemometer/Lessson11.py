import serial  # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt  # import matplotlib library
from drawnow import *

velocity = []
arduinoData = serial.Serial('com6', 9600)  # Creating our serial object named arduinoData
plt.ion()  # Tell matplotlib you want interactive mode to plot live data
cnt = 0


def makeFig():  # Create a function that makes our desired plot
    plt.ylim(0, 50)  # Set y min and max values
    plt.title('Wind Diagramm')  # Plot the title
    plt.grid(True)  # Turn the grid on
    plt.ylabel('Windgeschwindigkeit')  # Set ylabels
    plt.plot(velocity, 'ro-', label='km/h')  # plot the temperature
    plt.legend(loc='upper left')  # plot the legend


while True:  # While loop that loops forever
    while (arduinoData.inWaiting() == 0):  # Wait here until there is data
        pass  # do nothing
    arduinoString = arduinoData.readline()  # read the line of text from the serial port
    temp = float(arduinoString)  # Convert first element to floating number and put in temp
    velocity.append(temp)  # Build our tempF array by appending temp readings
    drawnow(makeFig)  # Call drawnow to update our live graph
    plt.pause(.000001)  # Pause Briefly. Important to keep drawnow from crashing
    cnt = cnt + 1
    if (cnt > 200):  # If you have 50 or more points, delete the first one from the array
        velocity.pop(0)  # This allows us to just see the last 50 data points