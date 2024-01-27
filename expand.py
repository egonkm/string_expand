#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 18:25:51 2024

@author: egon
"""

OPEN = "({"
CLOSE = ")}"

ESCAPE_SEQS = ["\(", "\)", "\|", "\{", "\}"]
ESCAPE_CHAR = "\\"


def find_end(string, ptr, close):

  # find the last character of a group
  # close : list of ending chars

  while close:

    ptr += 1
    
    if ptr>=len(s): return -1, None # end of s reached without closing char
    
    c = string[ptr]

    if c == close[-1]: # found a matching end group char

      close.pop()
      continue

    if c in OPEN: # add an open group char

      close.append(CLOSE[OPEN.find(c)])
      continue

    if c in CLOSE:
      return -1, ptr  # closing char mismatch

  return ptr+1, None # returns the position of the end of the group

def split(string, sep="|"):
  # split a group in its elements
  # sep: separator char

  queue = []
  ptr = 0
  start = 0
  res = []

  while ptr<len(string):
      
    c = string[ptr]
        
    if c==ESCAPE_CHAR:
 
        ptr += 2
        continue

    if c in OPEN:
      queue.append(CLOSE[OPEN.find(c)])

    if c==sep and not queue:

      res.append(string[start:ptr])
      start = ptr+1

    if c in CLOSE:

      if c==queue[-1]:
        queue.pop()
      else:
        print("Mismatch: ", queue)
        return None

    ptr += 1

  res.append(string[start:ptr]) # adds the last element of the group

  return res

def expand_it(string, l_expansions, ptr_char):
    
    while ptr_char<len(string):

      char = string[ptr_char]

      if char in OPEN: # group oppening found

        end_car = CLOSE[ OPEN.find(char)]
        cont, end = find_end(string, 
                             ptr_char, 
                             [end_car] ) # get the last char of the group

        if cont==-1: # not found ending char

          if end:
              
            print("Error in col ", end+1, 
                  "looking for ", end_car, "found ", s[end], "instead.")
            return None

          print("Error: reached end of str without closing char ", end_car,".")
          
          return None

        before = string[0:ptr_char]
        group = string[ptr_char+1:cont-1]
        after = string[cont:]
        elements = split(group, "|")

        if char == "{": elements.append("") # expand without anything inside optional group
 
        for posibility in elements:

          if not expand_it(before+posibility+after, 
                           l_expansions, 
                           ptr_char): return None

        return True

      if char in CLOSE:
          
        print("Closing ",char," without pair, col:", ptr_char+1)
        return False

      ptr_char += 1

    for escape in ESCAPE_SEQS:
        string = string.replace(escape, escape[1:])

    l_expansions.append(string)

    return True
        

def expand(string, variables=None):
    
    string = string.strip()

    if not string: return []
  
    result = []
    
    if variables:
        
        strings = []
    
        for slot, vals in variables.items():
        
            if "$"+slot in string:
    
                for val in vals:                    
                    strings.append(string.replace("$"+slot, val))

    else:
        strings = [string]
    
    for string in strings:
        if not expand_it(string, result, 0): return None   
   
    return result 


if __name__=="__main__":
    
    s = """
    Oh{, thank you so much|, God \|bless you|, I can't believe it}! 
This is{ way} better than I (expected|needed|asked for).
    """
    s = s.replace("\n", "").strip()
    
    print("Expanding: ", s)
    
    results = expand(s) 
    if results:
      for result in results: print(result)
      
      
    v = { "hello" : ["Hello", "Hi there", "Morning"],
           "thanks" : ["Thank you!", "Thanks!", "Thanks a lot."] 
           }
           
    
    print("\nWith variables:\n")
    
    for res in expand("$hello! Please follow the procedure. $thanks",
                      v):
        print(res)
  
  