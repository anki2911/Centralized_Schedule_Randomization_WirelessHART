import sys
import library_functions
import library_multi_channel
import random
from igraph import *
from tqdm import tqdm
import math

num_of_chan = 4
num_of_tasks = 40

f2 = open("../F_7_3.txt","r")
FLOW = []

i = 0
for l in f2:
    l = l.strip()
    for words in l:
        words = l.split()
    if words[0][0] == "F":
        FLOW.append(library_functions.Flow(0,[],0))
i = -1
f3 = open("../F_7_3.txt","r")
for lines in f3:
    lines = lines.strip()
    #print counter
    if lines[0][0] == "F":
        fid = lines
        counter = 0
        i += 1
    elif counter == 1:
        deadline = int(lines)
        FLOW[i].deadline = deadline
    else:
        lines = lines.split(" ")
        FLOW[i].flow.append((int(lines[0]),int(lines[1])))
    counter += 1   

flow_set = []

periods = [256,512,1024]
hyperperiod = max(periods)
for i in range(100):
    t = []
    
    flow_set.append([])

for i in range(100):    
    f = open("D43/Flow_set_1_" + str(i+1) + ".txt","w+")
    p = []
    for j in range(num_of_tasks):
        q = random.randint(0,len(periods)-1)
        p.append(periods[q])
        r = random.randint(1,80)
        flow_set[i].append((r,periods[q]))
    flow_set[i].sort(key=lambda tup: tup[1])
    p.sort()
    for j in range(num_of_tasks):
        f.write("F"+str(j+1)+"\n")
        f.write(str(p[j]) + "\n")
        for k in range(len(FLOW[flow_set[i][j][0]-1].flow)):
            f.write(str(FLOW[flow_set[i][j][0]-1].flow[k][0]) + " " + str(FLOW[flow_set[i][j][0]-1].flow[k][1]) + " " + str(j+1) + "\n")        
    
    g = open("D43/Sched_1_" + str(i+1) + ".txt","w+")
    available = []
    T = []
    for s in range(hyperperiod):
        available.append(0)
        T.append("- - -")
    k = 1
    while k <= hyperperiod:
        for j in range(len(flow_set[i])):
            if (k%flow_set[i][j][1] == 0):
                inst = k/flow_set[i][j][1]
                #print inst
                l = flow_set[i][j][0]
                jumps = len(FLOW[l-1].flow)
                lb = (inst-1)*flow_set[i][j][1]
                ub = k-1
                start = lb
                m = 0
                #print jumps
                
                while start <= ub:
                    if available[start] == 0:
                        available[start] = l
                        T[start] = str(FLOW[l-1].flow[m][0]) + " " + str(FLOW[l-1].flow[m][1]) + " " + str(j+1)
                        m = m + 1
                    if m == jumps:
                        start = ub + 1
                    if m < jumps and start == ub:
                        print "Unschedulable" 
                    start = start + 1
        k = k + 1
    for i in range(hyperperiod):
        g.write(str(T[i]) + "\n")
        for j in range(num_of_chan-1):
            g.write("- - -\n")            
        g.write("%\n")
    
            
            
        
    
       
#print flow_set 
       
f2.close()
