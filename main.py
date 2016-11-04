from com import COMPort
from graph import RokotGraph


#test = COMPort("com3", 9600)
#test.readBytes(70, False, True, "log.txt")

graphics = RokotGraph("log.txt")

graphics.draw3dCoordGraphFromFile("g")
#

"""Simple examples
graphics.drawAllGraphsFromFile("Rokot Data")
graphics.drawOneGraph(0,"Rokot data", 0, 50, "Temperature", "Degrees")
graphics.draw3dCoordGraphFromFile("")
"""