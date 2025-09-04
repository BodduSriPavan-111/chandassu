"""
Module: laghuvu_guruvu.py
Description: Contains Telugu aksharam tokenizer, and Laghuvu-Guruvu generator functions.
Author: Boddu Sri Pavan
License: MIT
"""

import regex as re
from collections import Counter

from .nidhi import lg_map, varnamala, hallulu

class LaghuvuGuruvu:
    """
    ## Contains Aksharam Tokenizer, Laghuvu-Guruvu Generator.

    ## Attributes
    -------------
    1. data: str
        - Input Telugu string to be processed.

    ## Methods
    -----------
    1. tokenize
        - Aksharam Tokenizer.
    2. generate
        - Laghuvu-Guruvu Generator.
    """
    
    def __init__(self, data):

        # Remove leading, trailing spaces, and some unwanted characters
        self.data= data.strip().replace('\u200c', "").replace('\u200d', "").replace("x", "") 


    def tokenize( self ):
        """
        ## Aksharam Tokenizer
        ### This function tokenizes the input Telugu string into 'Aksharam Tokens'.

        ## Attributes
        -------------
        1. text: list
            - Each element corresponds to one Akharam Token for generating Laghuvu-Guruvu.

        ## Returns
        ----------
        1. text: list
            - Each element corresponds to one Akharam Token for generating Laghuvu-Guruvu.
        """
        
        # Using regex to split the raw text
        temp_l= re.findall(r"\X", self.data)

        # Remove unwanted characters and symbols
        l= []
        for i in temp_l:
            if (not i in list("""` ~ ! @ # $ % ^ & * ( ) _ - + = { } [ ] \ | ; : ' " “ ” ‘ ’ , < > . / ? ఽ ।""")) and  (not i.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ") and (not i.isnumeric() ):
                l.append(i)

        index= 0
        text= []
        temp= ""

        for index in range(len(l) ):

            # Ignore "Ara Sunna" (Half Circle, often pronounced similar to 'Pollu Hallu')
            l[index]= l[index].strip("ఁ")

            # Pass to next character if current character is space
            if l[index].isspace(): #or l[index].isnumeric() or l[index].upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or l[index] in list("""` ~ ! @ # $ % ^ & * ( ) _ - + = { } [ ] \ | ; : ' " “ ” ‘ ’ , < > . / ? ఽ ।"""):
                # text.append( l[index] )
                pass

            # If current character is 'Pollu Hallu', 'temp' flag is empty, 'index' is less than second from last, and not last character is space
            # To capture 'Samlistaaksharam' (Conjuct) using 'temp' variable
            elif l[index].endswith('్') and temp == "" and index< len(l)-1 and not l[index+1].isspace():
                temp+= l[index]
        
            # If current character ends with 'Pollu Hallu', 'temp' is not empty and not last character is space
            # For 'Samlistaaksharam' (Conjuct) using 'temp' variable
            elif l[index].endswith('్') and temp != "" and not l[index+1].isspace():
                temp+= l[index]

            # For pollu hallu (at the end of word or at the end of the line/ sentence)
            elif l[index].endswith('్') and (index+1 == len(l) or l[index+1].isspace() ):
                text[-1]+= l[index]

            # If current character is not 'Pollu Hallu' and 'temp' flag is not empty
            # Indicates completition of 'Samlistaaksharam' (Conjuct)
            elif (not l[index].endswith('్')) and temp != "":
                text.append( temp+l[index] )
                temp= ""
            
            # If current character is not "Pollu Hallu" and 'temp' flag is empty
            elif (not l[index].endswith('్')) and temp == "":
                text.append( l[index] )
                temp= ""

            # Unknown case to handle (for future purpose)
            else:
                print("Unknown Case (for future purpose) !\n We welcome your valuable contributions to 'chandassu' !")

        self.text= text

        return self.text

    def generate( self ):
        """
        ## LaghuvuGuruvu Generator
        ### Generates Laghuvu-Guruvu for the tokenized Telugu string.

        ## Returns
        ----------
        Return a list of tuples
        where each tuple is in the format: (Aksharam Token, Laghuvu/ Guruvu)
        where 
        Aksharam Token: str
        Laghuvu/ Guruvu: str
        """

        l= self.tokenize()

        # Stores the corresponding Laghuvu-Guruvu of each generated token
        marking= []
        
        # Edge: 
        # l= ["గ","ర్భం"] #['చ', "ష్ణున్"] #['చ', 'క్రాన్'] #['వి', 'ష్ణున్']
        # re.findall(r"\X","విర్"), re.findall(r"\X", "ప్చర్"), re.findall( r"\X", "ప్చార్")

        # Iterate through the list of tokens
        for index in range( len(l) ):

            # If index upto last but one
            if index < len(l)-1 :
                
                # Split the succeeding Aksharam Token using regex
                x= re.findall(r"\X", l[index+1])

                # Check if the succeeding Aksharam Token ends with 'Pollu Hallu'
                if x[-1].endswith('్'):
                    x= "".join(x[:-1]) 
                
                else:
                    x= "".join(x)   # ["గ","ర్భం"]

                # Count the no.of occurrences of each character in the succeeding Aksharam Token
                d= Counter(x)

                # Ignore 'ర' as sometimes it is not considered in Samslistaaksharam for Guruvu Symbol
                del d["ర"]
                
                temp_count= 0
                for i in d:
                    if i in hallulu:

                        # Increment the count iff current character is "Hallu"
                        temp_count+= 1*d[i] # "పుత్త్రు"

                # 'ర' in succeeding Aksharam Token and 
                # either 'temp_count' is '0' or 'temp_count' is '1' and corresponding Aksharam Token does not start with 'ర'
                if 'ర' in l[index+1] and ((temp_count==0) or (temp_count == 1  and (not l[index+1].startswith('ర')))):
                    marking.append( lg_map[l[index][-1]] )
            
                else:

                    # Find count of varnamala characters in succeeding Aksharam Token
                    count= 0
                    for j in list(l[index+1]):
                        if j in varnamala:
                            count+= 1

                    # If 'count' is greater than '1' and succeeding Aksharam Token does not end with 'Pollu'
                    # then mark current Aksharam Token as 'U' (Guruvu)
                    if count > 1 and not l[index+1].endswith('్'):
                        marking.append( "U" )
                    
                    # If 'count' is greater than '1' and succeeding Aksharam Token ends with 'Pollu'
                    # then mark current Aksharam Token as 'U' (Guruvu)
                    elif count > 1 and l[index+1].endswith('్') and re.findall( r"\X", l[index+1])[0].endswith('్'):
                        marking.append( "U" )
                    
                    # If 'count' is greater than '1' and succeeding Aksharam Token ends with 'Pollu'
                    # then mark current Aksharam Token as per the last character in current Aksharam Token
                    elif count > 1 and l[index+1].endswith('్'):
                        marking.append( lg_map[l[index][-1]] )

                    # Mark current Aksharam Token as per the last character in current Aksharam Token
                    else:
                        marking.append( lg_map[l[index][-1]] )
            
            # Check the rightmost character in each Aksharam Token
            elif l[index][-1] in lg_map:
                marking.append( lg_map[l[index][-1]] )

            # Unknown case to handle (for future purpose)
            else:
                print("Unknown Case (for future purpose) !\n We welcome your valuable contributions to 'chandassu' !")

        # Return a list of tuples where each tuple is in the format: (Aksharam Token, Laghuvu/ Guruvu)
        # Not dict because dict donot allow multiple keys with same name
        return list(zip(l, marking))