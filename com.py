import serial  # Import Serial Library

class COMPort():
    def __init__(self, port, bitrate):
        self.port = port
        self.bitrate = bitrate
        self.struct = serial.Serial(port, bitrate)


    def _serialGet(self):
        return self.struct

    def serialWrite(self, file, struct  ):
        """
        This def write packages to file
        :param file:
        :param struct:
        :return:
        """
        fout = open(file, "w")
        fout.write(struct)
        fout.close()

    def readBytes(self, count, array = False,write = False, filename = ""):
        """
        This def read com packages and print their
        :param count:
        :param array:
        :param write:
        :param filename:
        :return:
        """

        serial = self._serialGet() # получить данные из COMPORT в данный момент

        i = 0
        writeFile = ""

        while i < count + 18:
            if i <= 18:
                myData = serial.readline()
                i+=1
                continue
            if (serial.inWaiting() > 0):
                print(serial.readline())
                myData = serial.readline().decode("utf-8")
                print( [myData, self.getTupleValues(myData)][array] )
                writeFile += myData
                i += 1
        if write:
            self.serialWrite(filename, writeFile)

    def getTupleValues(self, bytes, sep  = ", " ):
        """
        This def return data packages in tuple-form
        :param bytes:
        :param sep:
        :return:
        """
        return list(bytes.strip().split(sep))
    def writeCoordinatesFromFile(self, fromf, to):

        f = open(fromf, "r")
        fz = open(to, "w")

        sep = ", "
        lst = 2

        a = [i.split(sep) for i in f.readlines()]

        i = 0

        for i in range(len(a)):
            if a[i][0] != "\n":
                b = a[i][1:4]
                for i in b:
                    fz.write(i + " ")
                fz.write("\n")

        f.close()
        fz.close()




if __name__ == "__main__":
    test = COMPort("com3", 9600)
    test.readBytes(100, False, True, "log.txt")
    test.writeCoordinatesFromFile("log.txt", "coord.txt")