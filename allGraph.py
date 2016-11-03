import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
fig.canvas.set_window_title('ROKOT DATA')

thread = open("log.txt",'r')
i = 0
xar = []
out_temp, altitude, acc_x, acc_y, acc_z = [], [], [], [], []

def animate(self):
    global i, xar, out_temp, altitude, acc_x, acc_y, acc_z
    message = thread.readline()
    if len(message)>5:
        l = message.split(", ")
        xyz = l[1:4]
        l.append(xyz)
        xar.append(int(i))
        altitude.append(float(l[4]))
        out_temp.append(float(l[0]))
        acc_x.append(int(xyz[0]))
        acc_y.append(int(xyz[0]))
        acc_z.append(int(xyz[0]))
        i += 1
    else:
        thread.close()
        plt.pause(pow(10, 10))

    egrid = (12, 12)
    ax1 = plt.subplot2grid(egrid, (0, 0), colspan=4,rowspan=4)
    ax1.set_title("Accel X")
    plt.ylim(-30,40)
    ax1.plot(xar,acc_x,'bo-')

    ax2 = plt.subplot2grid(egrid, (0, 4), colspan=4, rowspan=4)
    ax2.set_title("Accel Y")
    plt.ylim(-100, 100)
    ax2.plot(xar, acc_y, 'yo-')

    ax3 = plt.subplot2grid(egrid, (0, 8), colspan=4, rowspan=4)
    ax3.set_title("Accel Z")
    plt.ylim(-30, 40)
    ax3.plot(xar, acc_z, 'ro-')


ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()