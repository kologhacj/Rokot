from com import *
import matplotlib.pyplot as plt  # import matplotlib library
from drawnow import *

tempF = []
plt.ion()  # Tell matplotlib you want interactive mode to plot live data
cnt = 0
fin = open("log.txt", "r")
summ = sum(1 for i in open('log.txt', "r"))//2

matrix = (
(-30, 80, "Temperature"),
(-60000,50000,"Accel X",),
(-60000,50000,"Accel Y",),
(-60000,50000,"Accel Z",))

need = 1

test = COMPort("com3",9600)
test.readBytes(30,False,True,"log.txt")


def makeFig():  # Create a function that makes our desired plot
    plt.ylim(matrix[need][0] ,matrix[need][1] )
    plt.xlim(-2, summ+2)
    plt.title('Rokot')  # Plot the title
    plt.grid(True)  # Turn the grid on
    plt.ylabel(matrix[need][2])  # Set ylabels
    plt.plot(tempF, 'ro-', label='Degrees')  # plot the temperature
    plt.legend(loc='upper left')

for line in fin:  # While loop that loops forever
    #while (arduinoData.inWaiting()==0): #Wait here until there is data
    #   pass #do nothing
    # arduinoString = arduinoData.readline().decode("utf-8") #read the line of text from the serial port
    arduinoString = line.strip()

    if arduinoString == "":
        continue

    dataArray = [float(i) for i in arduinoString.split(', ')]
    temp = dataArray[need]
    tempF.append(temp)
    drawnow(makeFig)

    plt.pause(.0000001)

    cnt = cnt + 1
    if (cnt > 50):
        tempF.pop(0)

plt.pause(pow(10,10))


class DrawGraphics():
    def __init__(self):
        pass
    def drawGraphFromFile(self, filename):
        pass