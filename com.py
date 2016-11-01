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

        while i < count:
            if (serial.inWaiting() > 0):
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
        return tuple(bytes.strip().split(sep))



if __name__ == "__main__":
    pass

