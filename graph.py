i = 0
xar = []
out_temp, altitude, acc_x, acc_y, acc_z, pressure = [], [], [], [], [],[]

class RokotGraph():
    def __init__(self, file):
        self.file = file
    def draw3dCoordGraphFromFile(self, view = (90,-90)):
        from mpl_toolkits.mplot3d import axes3d
        import numpy as np
        import matplotlib
        import matplotlib.pyplot as plt

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        fin = open(self.file, "r")
        x, y, z = list(), list(), list()

        for line in fin:
            array = line.split(", ")
            _x, _y, _z = float(array[1]), float(array[2]), float(array[3])
            x.append(_x)
            y.append(_y)
            z.append(_z)

        ax.plot(z, y, x, zdir='z', label='zs=0, zdir=z')
        ax.set_xlim3d(-50, 100)
        ax.set_ylim3d(-50, 100)
        ax.set_zlim3d(-20, 50)

        ax.view_init(view[0], view[1])
        plt.show()
    def drawOneGraph(self, need, title, minimal, maximum, ylabel, measure, color = 'ro-'):
        import matplotlib.pyplot as plt  # import matplotlib library
        from drawnow import drawnow

        tempF = []
        plt.ion()  # Tell matplotlib you want interactive mode to plot live data
        cnt = 0
        fin = open(self.file, "r")
        summ = sum(1 for i in open(self.file, "r")) // 2

        def makeFig():  # Create a function that makes our desired plot
            plt.ylim(minimal, maximum)
            plt.xlim(-2, summ + 2)
            plt.title(title)  # Plot the title
            plt.grid(True)  # Turn the grid on
            plt.ylabel(ylabel)  # Set ylabels
            plt.plot(tempF, color, label= measure)  # plot the temperature
            plt.legend(loc='upper left')

        for line in fin:
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

        """for stable viewing"""
        plt.pause(pow(10, 10))
    def drawAllGraphsFromFile(self, title, delay=1000):
        import matplotlib.pyplot as plt
        import matplotlib.animation as animation

        fig = plt.figure()
        fig.canvas.set_window_title(title)
        thread = open(self.file, 'r')

        def animate(self):
            global i, xar, out_temp, altitude, acc_x, acc_y, acc_z, pressure
            message = thread.readline()
            if len(message) > 5:
                l = message.split(", ")
                xyz = l[1:4]
                l.append(xyz)
                xar.append(int(i))
                altitude.append(float(l[5]))
                out_temp.append(float(l[0]))
                pressure.append(float(l[4]))
                acc_x.append(int(xyz[0]))
                acc_y.append(int(xyz[0]))
                acc_z.append(int(xyz[0]))
                i += 1
            else:
                thread.close()
                plt.pause(pow(10, 10))

            egrid = (12, 12)

            ax1 = plt.subplot2grid(egrid, (0, 0), colspan=4, rowspan=4)
            ax1.set_title("Accel X")
            plt.ylim(-30, 40)
            ax1.plot(xar, acc_x, 'bo-')

            ax2 = plt.subplot2grid(egrid, (0, 4), colspan=4, rowspan=4)
            ax2.set_title("Accel Y")
            plt.ylim(-100, 100)
            ax2.plot(xar, acc_y, 'yo-')

            ax3 = plt.subplot2grid(egrid, (0, 8), colspan=4, rowspan=4)
            ax3.set_title("Accel Z")
            plt.ylim(-30, 40)
            ax3.plot(xar, acc_z, 'go-')

            ax4 = plt.subplot2grid(egrid, (6, 0), colspan=4, rowspan=4)
            ax4.set_title("Temperature")
            plt.ylim(0, 40)
            ax4.plot(xar, out_temp, 'ro-')

            ax5 = plt.subplot2grid(egrid, (6, 4), colspan=4, rowspan=4)
            ax5.set_title("Pressure")
            plt.ylim(99800,100201)
            ax5.plot(xar, pressure, 'bo-')

            ax6 = plt.subplot2grid(egrid, (6, 8), colspan=4, rowspan=4)
            ax6.set_title("Altitude")
            plt.ylim(-80, 150)
            ax6.plot(xar, altitude, 'bo-')

            # TODO
            """Make all graphs"""
        ani = animation.FuncAnimation(fig, animate, interval=delay)
        plt.show()

if __name__ == "__main__":
    pass
