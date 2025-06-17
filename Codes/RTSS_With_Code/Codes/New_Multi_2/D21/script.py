import sys
import os

i = 9
while i < 100:
    os.system("python ../Multi_Channel_Random.py ../G1.txt Flow_set_1_" + str(i+1) + ".txt Sched_1_" + str(i+1) + ".txt R1/Entropy_Random_1_" + str(i+1) + ".txt R1/entropy_out_1_" + str(i+1) + ".txt")
    i = i + 1
