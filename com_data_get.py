import serial  # Import Serial Library
import msvcrt

class COMPort():
    def __init__(self, port, bitrate):
        self.port = port
        self.bitrate = bitrate
        try:
            self.struct = serial.Serial(port, bitrate)
        except:
            raise("Connection error")

    def serialGet(self):
        return self.struct

    def serialWrite(self, file, struct  ):
        fout = open(file, "w")
        fout.write(struct)
        fout.close()

    def readBytes(self, count, write = False, filename = ""):
        serial = self.serialGet() # получить данные из COMPORT в данный момент

        i = 0
        writeFile = ""

        while i < count:
            if (serial.inWaiting() > 0):
                myData = serial.readline().decode("utf-8")
                print(myData)
                writeFile += myData
                i += 1
        if write:
            self.serialWrite(filename, writeFile)


if __name__ == "__main__":
    test = COMPort("com3", 9600)
    test.readBytes(5, True, "log1.txt")
