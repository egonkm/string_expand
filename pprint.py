#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 18:54:35 2024

@author: egon
"""


NULL = "NULL"
MAX_GROUP_SIZE = 20 # ignore small groups 
MAXCOLS = 250
SEPARATORS = ["|"]

SPECIAL = { "{" : "}", 
             "(" : ")"}

ESCAPE_SEQS = ["\(", "\)", "\|", "\{", "\}"]
ESCAPE_CHAR = "\\"


 
def find_group_size(string, car_ptr):
    
    queue = [ SPECIAL[string[car_ptr]]]
    start_position = car_ptr
    car_ptr += 1
    
    while (car_ptr<len(string)) and queue:

        if string[car_ptr] in SPECIAL.keys():
            queue.append(SPECIAL[string[car_ptr]])
            
        if string[car_ptr] in SPECIAL.values():
            
            if string[car_ptr] != queue[-1]:
                print("***Error: GROUP mismatch, expected ", 
                      queue[-1]," found ", string[car_ptr],
                      " at col ", car_ptr+1)
                return -1
            
            queue.pop()
            
        car_ptr += 1
        
    if queue:
        print("***Error: premature end of line, queue not empty:", queue)
        return -1
    
    return car_ptr - start_position

 
def _pprintit(string, car_ptr=0, line_len=0, tabs=0,
             queue=[], divide=[]):
       
    if car_ptr >= len(string):
        
        if queue:
            print("***Error: queue not empty", queue)
            return False
        
        print("\n", end="")          
        return True
    
    car = string[car_ptr]
    print_car = True
    long_group=False
    
    if car in list(SPECIAL.values()):
        
        if divide[-1]:
                print("\n", (len(queue)-1)*"\t", end="")
                
        if tabs>0: tabs -= 1
        
        if not queue:
            print("***Error: Queue is empty, got: ", car)
            return False
        
        matching_car = queue.pop()
        divide.pop()
        
        if matching_car != car:
            print("***Error: car mismatch, got ", car," expected ", matching_car)
            return False
            
    if car in SPECIAL.keys():
        
        long_group = find_group_size(string, car_ptr)>MAX_GROUP_SIZE            
        divide.append(long_group)
        queue.append(SPECIAL[car])
        
    if car in SEPARATORS:
        
        if divide and divide[-1]: 
            print("|\n", (len(queue)-0)*"\t", end="")
            print_car = False
              
    car_ptr += 1
    
    if long_group: print("\n", (len(queue)-1)*"\t", end="")
    
    if print_car: print(car, end="")
    
    if long_group: print( "\n", len(queue)*"\t", end="")
    
    line_len += 1
    
    if line_len>=MAXCOLS:
        line_len = 0
        print( "\n", tabs*"\t", end="")
        
     
    _pprintit(string, car_ptr, line_len, tabs, queue, divide) # recursive call
       
   
def pprintit(string):
    
    for escape in ESCAPE_SEQS:
        string = string.replace(escape, escape[1:])    
        
    _pprintit(string)
    
if __name__=="__main__":
    
    string = """
     Oh{, thank you so much|, God bless you|, I can't \{believe\} it}! 
 This is{ way} better than I (expected|needed|asked for).
     """
     
    print("String:", string)
    
    pprintit(string.strip())