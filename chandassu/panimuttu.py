"""
Module: panimuttu.py
Description: Contains utility functions
Author: Boddu Sri Pavan
License: MIT
"""

from .nidhi import gunintha_chihnam, varnamala

def remove_gunintha_chihnam( x ):
    """Remove all the Gunintha Chihnams from the input text."""
    
    l= ""
    for i in x:
        if i not in gunintha_chihnam:
            l+= i
    return l

def extract_gunintha_chihnam( x ):
    """Extract Gunintha Chihnam from the given Aksharam Token."""
    
    l= ""
    for i in gunintha_chihnam:
        if i in x:
            l= i
    
    # For vowel sound: 'అ'
    if l== "":
        l= " "
        
    return l

def extract_aksharam( x ):
    """Extracts all varnamala letters into a list."""
    
    l= []
    for i in x:
        if i in varnamala:
            l.append(i)
    return l

def extract_paadam( padyam ):
    """Extracts paadams (lines) from given padyam based on newline separator (for future purpose)."""
    
    l= []
    for i in padyam.split("\n"):
        
        i= i.strip()
        if len(i) > 0:      # Assume atleast one letter present in the padyam
            l.append(i) 

    return l