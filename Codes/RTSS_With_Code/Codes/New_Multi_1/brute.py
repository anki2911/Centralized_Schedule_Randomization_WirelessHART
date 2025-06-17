import sys
import os

for i in range(100):
    os.system("python Brute_Force_Entropy.py D41/Flow_set_1_" + str(i+1) + ".txt D41/Sched_1_" + str(i+1) + ".txt D41/brute_1_" + str(i+1) + ".txt")
    os.system("python K_L_Divergence.py D41/R1/Entropy_Random_1_" + str(i+1) + ".txt D41/brute_1_" + str(i+1) + ".txt Divergence_41.txt")
    
