import sys


xs = []
ys = []
zs = []

g = open("Data_3.txt","w")
for i in range(4):
    str1 = "../Codes/New_Multi_" + str(i+1)
    for j in range(4):
        str2 = str1 + "/D" + str(j+1) + "3/R3/"
        for k in range(100):
            str3 = str2 + "entropy_out_1_" + str(k+1) + ".txt"
            f = open(str3,"r")
            l = float(f.read())
            xs.append(i+1)
            ys.append(int(j+1)*10)
            zs.append(l)
            g.write(str(l))
            g.write("\n")
        g.write("%")
        g.write("\n")
