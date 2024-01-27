#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 18:25:51 2024

@author: egon
"""

OPEN = "({"
CLOSE = ")}"


def expand(string):
    
    
    return []


if __name__=="__main__":
    
    s = """
    Oh, {thank you so much!|God bless you!|I can't believe it!}. 
This is {way} better than I (expected|needed|asked for).
    """
    s = s.replace("\n", "").strip()
    
    print("Expanding: ", s)
    
    results = expand(s) 
    if results:
      for result in results: print(result)