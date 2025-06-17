import sys
import os

for i in range(3):
    for j in range(4):
        p = "D"+str(i+1) + str(j+1)
        os.system("mkdir D" + str(p))
        os.system("python Flow_Set_generator.py "+str(p) + + " " + str(i+1) + " " + str(j+1)) 
    
