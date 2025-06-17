import sys

D = []
for i in range(4):
    P = []
    D.append(P)
    for j in range(3):
        Q = []
        D[i].append(Q)
        #s1 = "Divergence_" + str(i+1) + str(j+1) + ".txt"
        s1 = "D" + str(i+1) + str(j+1) + "/R" + str(j+1) + "/entropy_out_1_"
        for k in range(100):
            s2 = s1 + str(k+1) + ".txt"
            g = open(str(s2),"r")
            for lines in g:
                lines = lines.strip()
                lines = lines.split()
                D[i][j].append(float(lines[0]))
        #g = open(str(s1),"r")
        #for lines in g:
        #    lines = lines.strip()
        #    lines = lines.split()
        #    D[i][j].append(float(lines[0]))
       
f = open("U_3.txt","r")
sum1 = 0
U1 = []
count = 0
for lines in f:
    lines = lines.strip()
    lines = lines.split()
    if lines[0] == "%":
        print sum1*1.0/count
        print count
        count = 0
        sum1 = 0        
    else:
        ind1 = int(lines[0][0])
        ind2 = int(lines[0][1])
        ind3 = int(lines[1])
        #print D[ind1-1][ind2-1][ind3 -1]
        sum1 = sum1 + D[ind1-1][ind2-1][ind3 -1]
        count += 1
     
        
        
