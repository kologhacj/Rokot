import serial #Import Serial Library
 
arduinoSerialData = serial.Serial('com3',9600)
 
 
while True:
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline()
        print(myData.decode("utf-8"))
        #Привет2
