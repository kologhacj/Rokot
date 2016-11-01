import serial  # Import Serial Library
import msvcrt

class COMPort():
    def __init__(self, port, bitrate):
        self.port = port
        self.bitrate = bitrate
        self.struct = serial.Serial(port, bitrate)

    def serialGet(self):
        return self.struct

    def serialWrite(self, file, struct  ):
        fout = open(file, "w")
        fout.write(struct)
        fout.close()

    def readBytes(self, count, write = False, filename = False):
        try:
            connect = COMPort("com3", 9600)
        except:
            return "Connection Error"

        serial = connect.serialGet() # получить данные из COMPORT в данный момент

        i = 0
        writeFile = ""

        while i <= count:
            if (serial.inWaiting() > 0):
                myData = serial.readline().decode("utf-8")
                print(myData)
                writeFile += myData
                i += 1
        if write:
            connect.serialWrite(filename, writeFile)

if  __name__ ==  "__main__" :
