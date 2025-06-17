import sys

counter = []
for i in range(100):
    n = []
    counter.append(n)

count = 0
index = 0

f = open("./New_Multi_4/D43/Sched_1_100.txt","r")

for lines in f:
    lines = lines.strip()
    for words in lines:
        words = lines.split()
    if words[0] == "%":
        count += 1
        index = 0
    elif words[0] <> "-":
        index += 1
        n1 = int(words[0])
        n2 = int(words[1])
        #sender
        counter[n1-1].append((count,n2,index,1))
        #receiver
        counter[n2-1].append((count,n1,index,2))
#print counter
#print counter
l = 0
ind = -1
sum = 0
for i in range(len(counter)):
     if len(counter[i]) > l:
         l = len(counter[i])
         index = i
print l   
print index

num = 100
K = 10

for i in range(num):
    fname = "/home/ankita/contiki-3.0/examples/rime/temp/node_" + str(i+1) + ".c"
    g = open(fname,"w+")
    #h = open("contiki.txt","r")
    with open("contiki_1.txt") as h1:
        l = h1.readlines()
        g.writelines(l)
    s = len(counter[i])
    if s > 0:
        g.write("static schedule S["+str(K)+"]["+str(s)+"];" + "\n")   
        g.write("static int sched_length = " + str(s) + ";" + "\n")     
    with open("contiki_2.txt") as h2:
        l = h2.readlines()
        g.writelines(l)
    for k in range(K):
        for j in range(len(counter[i])):
            if counter[i][j][3] == 1:
                g.write("S[" +str(k) + "][" + str(j) + "].from_node = " + str(i+1) + ";" + "\n")
                g.write("S[" +str(k) + "][" + str(j) + "].to_node = " + str(counter[i][j][1]) + ";" + "\n")
            elif counter[i][j][3] == 2:
                g.write("S[" +str(k) + "][" + str(j) + "].from_node = " + str(counter[i][j][1]) + ";" + "\n")
                g.write("S[" +str(k) + "][" + str(j) + "].to_node = " + str(i+1) + ";" + "\n")
            g.write("S[" + str(k) + "][" + str(j) + "].time_slot = " + str(counter[i][j][0]) + ";" + "\n")
            g.write("S[" + str(k) + "][" + str(j) + "].chan = " + str(counter[i][j][2]) + ";" + "\n")
    if s > 0:
        with open("contiki_3.txt") as h3:
            l = h3.readlines()
            g.writelines(l)
    else:
        with open("contiki_4.txt") as h4:
            l = h4.readlines()
            g.writelines(l)
            
