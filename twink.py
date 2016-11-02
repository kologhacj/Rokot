
f = open("log.txt", "r")
fz = open("coord.txt","w")

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
