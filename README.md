<h1>Rokot</h1>

Hello, you are on a Rokot Project page

This project was created for the contest Can Sat 2017 in Russia.

<h1>Documentation</h1>

The computer part is written in Python

<b>Used Python libraries:</b>

Numpy

PySerial

Matplotlib

Drawnow

<b>Used Arduino IDE library:</b>

GY-86

HMC5883L

MS5611

....

<h1>Classes:</h1>

COMport - class for receiving and primary data from COM ports

The methods of this class:

<b>def __init __ (self, port, bitrate):</b><br>
        This def initialize an instance<br>
        : Param port: port to which you want to connect, for example, com4, tty5<br>
        : Return self.struct<br>
        
<b>def _serialGet (self):</b>
        This def return serial data in this moment<br>
        : Return: str<br>
        : Return self.struct<br>

<b>def serialWrite (self, file, struct):</b>
        This def write packages to file
        : Param file: file, which is to record
        : Param struct: the package that you want to record
        : Return: void
        
        
<b>def readBytes (self, count, array = False, write = False, filename = ""):</b>
        This def read com packages and print their
        : Param count: the number of packets that need to be read
        : Param array: the output as an array
        : Param write: write to the file
        : Param filename: name of the file where to write the packets
        : Return: void
        
<b>def getTupleValues (self, bytes, sep = ","):</b>
        This def return data packages in tuple-form
        : Param bytes: string in which one packet is recorded
        : Param sep: separator in a package
        : Return: tuple
        
<b>def writeCoordinatesFromFile (self, fromf, to):</b>
        This def get limited packages from file, filter it and write coordinates in
        another file
        : Param fromf: the file where data will be taken
        : Param to: file, which will be recorded the coordinates
        : Return: void
