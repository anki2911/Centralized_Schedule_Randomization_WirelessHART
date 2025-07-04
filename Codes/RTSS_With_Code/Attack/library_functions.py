import sys
import matplotlib
import random


class Flow:
    def __init__(self,deadline,flow,exec_time):
        self.deadline = deadline
        self.flow = flow
        self.exec_time = exec_time
        
 
def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
      
def find_LCM(FLOW):
    """Compute the lowest common multiple of a and b"""
    i = 1
    a = FLOW[i-1].deadline
    while (i < len(FLOW)):
        b = FLOW[i].deadline
        c = a * b / gcd(a,b)   
        a = c 
        i += 1
    return c        

#returns slots of a particular flow that are to be shuffled
def find_shuffling_slots(curr_flow,F_Seq,lb,ub,Shuffle_slots):
    i = lb
    while i <= ub:
        if F_Seq[i] <> "-":
            if int(F_Seq[i]) == curr_flow:
                Shuffle_slots.append(i)
        i += 1
    return Shuffle_slots 

#returns the list of available slots
def find_available_slots(index,pos,lb,ub,F_Seq,available_slots):
    i = lb
    while i <= ub:
        if F_Seq[i] == "-":
            available_slots.append(i)
        #elif i <> pos:
        #    available_slots.append(i)#Changed
        elif i <> pos and (int(F_Seq[i])-1) <> index:
            available_slots.append(i)
        available_slos.append(pos)
        i += 1
    #print available_slots
    return available_slots 

#check whether available slot can be shuffled
def check_available(FLOW,curr_slot,slot_to_be_swapped,F_Seq,available_slots,lb,ub):
    #print pos
    flow_id = F_Seq[slot_to_be_swapped]
    curr_flow = F_Seq[curr_slot]
    if flow_id == "-":
        return 1
    #elif flow_id == curr_flow:
    #    return 0
    else:
        flow_index = int(F_Seq[slot_to_be_swapped]) - 1
        thres = curr_slot/FLOW[flow_index].deadline
        rem = slot_to_be_swapped/FLOW[flow_index].deadline
        if thres == rem:
            #print "Yes"
            return 1
        else:
            #print "No"
            return 0             

#Shuffles the slots
def Shuffler(curr_slot,slot_to_be_swapped,S,F_Seq):
    S = list(S)
    #print S[cur_slot]
    #print S[pos]
    temp = S[curr_slot]
    S[curr_slot] = S[slot_to_be_swapped]
    S[slot_to_be_swapped] = temp
    #print S[cur_slot]
    #print S[pos]
    S = tuple(S)
    #print F_Seq[cur_slot]
    #print F_Seq[pos]
    temp_flow = F_Seq[curr_slot]
    F_Seq[curr_slot] = F_Seq[slot_to_be_swapped]
    F_Seq[slot_to_be_swapped] = temp_flow
    #print F_Seq[cur_slot]
    #print F_Seq[pos]
    #print S,F_Seq
    return S,F_Seq

#order the list of tuples
def Order_list(num_of_flows,lb,ub,S,F_Seq,flow_ordering):
    S = list(S)
    counter = []
    for i in range(num_of_flows):
        counter.append(0)
    #print flow_ordering   
    for i in range(num_of_flows):
        t = lb
        while t <= ub:
            #print F_Seq[t]
            p = i+1
            if F_Seq[t] <> "-":
                if int(F_Seq[t]) == p:
                    #print S[t] 
                    S[t] = flow_ordering[i][counter[i]]
                    #print S[t] 
                    counter[i] += 1
                    #print counter[i]
            t += 1
    S = tuple(S)
    return S,F_Seq
            
