fin = open("log.txt","r")
fout = open("log2.txt","w")

for line in fin:
    if len(line)<5:
        continue
    else:
        fout.write(line)
fin.close()
fout.close()
