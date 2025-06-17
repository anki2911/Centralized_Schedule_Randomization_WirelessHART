import sys
import os

for i in range(100):
    os.system("python ../Multi_Channel_Random.py ../G2.txt Flow_set_1_" + str(i+1) + ".txt Sched_1_" + str(i+1) + ".txt R2/Entropy_Random_1_" + str(i+1) + ".txt R2/entropy_out_1_" + str(i+1) + ".txt")
    
