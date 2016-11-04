import serial  # Import Serial Library


class COMPort():

    def __init__(self, port: object, baudrate: object) -> object:
        self.port = port
        self.bitrate = baudrate
        self.struct = serial.Serial(port, baudrate)

    def _serialGet(self):
        return self.struct

    def serialWrite(self, file: object, struct: object ):
        import os

        fout = open("temp.log", "w")
        fout.write(struct)
        fout.close()

        fin = open("temp.log", "r")
        fout = open(file, "w")

        for line in fin:
            if len(line) < 5:
                continue
            else:
                fout.write(line)

        fin.close()
        fout.close()

        os.remove("temp.log")

    def readBytes(self, count: object, array: object = False, write: object = False, filename: object = ""):
        serial = self._serialGet()  # получить данные из COMPORT в данный момент

        i = 0
        writeFile = ""

        while i < count + 18:
            if i <= 18:
                myData = serial.readline()
                i += 1
                continue
            if (serial.inWaiting() > 0):
                print(serial.readline())
                myData = serial.readline().decode("utf-8")
                if len(myData) < 5:
                    continue
                print([myData, self.getTupleValues(myData)][array])
                writeFile += myData
                i += 1
        if write:
            self.serialWrite(filename, writeFile)

    def getTupleValues(self, bytes : object, sep=", "):
        return tuple(bytes.strip().split(sep))

    def writeCoordinatesFromFile(fromf, to: object, sep: object = ", ") -> object:
        f = open(fromf, "r")
        fz = open(to, "w")

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
    pass
