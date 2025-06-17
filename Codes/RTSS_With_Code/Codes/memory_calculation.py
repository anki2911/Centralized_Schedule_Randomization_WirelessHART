import sys
import os

dir_path = "/home/ankita/contiki-3.0/examples/rime/temp"
total_ram = 0
total_flash = 0
for root, dirs, files in os.walk(dir_path): 
    for file in files:  
        if file.endswith('.sky'): 
            os.system("size " + str(root) + "/" + str(file) + "> mem_temp.txt")
            with open("mem_temp.txt") as f:
                l1 = f.readline()
                l2 = f.readline()
                for words in l2:
                    words = l2.split()
                total_ram = total_ram + int(words[1]) + int(words[2])
                #print str(words[1]) + str(words[2])
                total_flash = total_flash + int(words[0]) + int(words[1])
                
print "Total RAM " + str(total_ram*0.01)

print "Total Flash " + str(total_flash*0.01)

            
