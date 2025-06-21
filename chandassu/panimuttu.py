from .nidhi import gunintha_chihnam, varnamala

def remove_gunintha_chihnam( x ):
    l= ""
    for i in x:
        if i not in gunintha_chihnam:
            l+= i
    return l

def extract_gunintha_chihnam( x ):
    l= ""
    for i in gunintha_chihnam:
        if i in x:
            l= i
    
    if l== "":
        l= " "
        
    return l

def extract_aksharam( x ):
    l= []
    for i in x:
        if i in varnamala:
            l.append(i)
    return l