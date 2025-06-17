import sys

def main ():
    f1 = open("Sched_1.txt","r")
    count = 0
    Sched = []
    f2 = open("File_operation.txt","w")
    for lines in f1:
        l = lines.strip("\n")
        words = l.split(" ")    
        #print words[1]
        if words[0] == "-":
            f2.write("sched["+str(count)+"].sender=0"+";\n")
            f2.write("sched["+str(count)+"].receiver=0"+";\n")
        else:
            S1 = "sched["+str(count)+"].sender="+words[0]+";\n"
            S2 = "sched["+str(count)+"].receiver="+words[1]+";\n"
            f2.write(S1)
            f2.write(S2)
        count += 1
        
    
    
        
if __name__=='__main__':
    main()
