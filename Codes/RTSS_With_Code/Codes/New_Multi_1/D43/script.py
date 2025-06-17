import sys
import os

for i in range(100):
    os.system("python ../SingleChannelRandom.py ../G3.txt Flow_set_1_" + str(i+1) + ".txt Sched_1_" + str(i+1) + ".txt R3/Entropy_Random_1_" + str(i+1) + ".txt R3/entropy_out_1_" + str(i+1) + ".txt")
    
