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
        
<b>def _serialGet (self):</b><br>
        This def return serial data in this moment<br>
        : Return: str<br>
        : Return self.struct<br>

<b>def serialWrite (self, file, struct):</b>
        This def write packages to file<br>
        : Param file: file, which is to record<br>
        : Param struct: the package that you want to record<br>
        : Return: void<br>
        
        
<b>def readBytes (self, count, array = False, write = False, filename = ""):</b><br>
        This def read com packages and print their<br>
        : Param count: the number of packets that need to be read<br>
        : Param array: the output as an array<br>
        : Param write: write to the file<br>
        : Param filename: name of the file where to write the packets<br>
        : Return: void<br>
        
<b>def getTupleValues (self, bytes, sep = ","):</b><br>
        This def return data packages in tuple-form<br>
        : Param bytes: string in which one packet is recorded<br>
        : Param sep: separator in a package<br>
        : Return: tuple<br>
        
<b>def writeCoordinatesFromFile (self, fromf, to):</b><br>
        This def get limited packages from file, filter it and write coordinates in another file<br>
        : Param fromf: the file where data will be taken<br>
        : Param to: file, which will be recorded the coordinates<br>
        : Return: void<br>
