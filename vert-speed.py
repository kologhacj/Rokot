fin = open("log.txt", "r")

z,vS = list(), list()
dt = 1/6
inter = 3

for line in fin:
    array = int(line.split(", ")[inter])
    if array == "":
        continue
    z.append(array)


for i in range(1, len(z)):
    dV = (z[i] - z[i-1])/dt
    vS.append(int(dV))

print(vS)
