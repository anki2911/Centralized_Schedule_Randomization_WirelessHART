import sys
import library_functions
import library_multi_channel
import random
from igraph import *
from tqdm import tqdm
import math


f2 = open("../F_7_1.txt","r")
FLOW = []

i = 0
for l in f2:
    l = l.strip()
    for words in l:
        words = l.split()
    if words[0][0] == "F":
        FLOW.append(library_functions.Flow(0,[],0))

f2.close()
