"""
Module: laghuvu_guruvu.py
Description: Contains Telugu aksharam tokenizer, and Laghuvu-Guruvu generator functions.
Author: Boddu Sri Pavan
License: MIT
"""

import regex as re
from collections import Counter

from .nidhi import lg_map, varnamala, hallulu, gunintha_chihnam

class LaghuvuGuruvu:

    def __init__(self, data):

        # Remove leading and trailing spaces
        self.data= data.strip().replace('\u200c', "").replace('\u200d', "").replace("x", "") 


    def tokenize( self ):

        temp_l= re.findall(r"\X", self.data)

        l= []
        for i in temp_l:
            if (not i in list("""` ~ ! @ # $ % ^ & * ( ) _ - + = { } [ ] \ | ; : ' " “ ” ‘ ’ , < > . / ? ఽ ।""")) and  (not i.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ") and (not i.isnumeric() ):
                l.append(i)

        index= 0
        text= []
        temp= ""

        for index in range(len(l) ):

            l[index]= l[index].strip("ఁ")

            if l[index].isspace(): #or l[index].isnumeric() or l[index].upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or l[index] in list("""` ~ ! @ # $ % ^ & * ( ) _ - + = { } [ ] \ | ; : ' " “ ” ‘ ’ , < > . / ? ఽ ।"""):
                # text.append( l[index] )
                pass

            elif l[index].endswith('్') and temp == "" and index< len(l)-1 and not l[index+1].isspace():
                temp+= l[index]
        
            # For Samlistaaksharams with no.of letters>2
            elif l[index].endswith('్') and temp != "" and not l[index+1].isspace():
                temp+= l[index]

            # For pollu hallu (at the end or at the end of the line)
            elif l[index].endswith('్') and (index+1 == len(l) or l[index+1].isspace() ):
                text[-1]+= l[index]

            elif (not l[index].endswith('్')) and temp != "":
                text.append( temp+l[index] )
                temp= ""
            
            elif (not l[index].endswith('్')) and temp == "":
                text.append( l[index] )
                temp= ""

            else:
                print("Unknown Case (for future purpose) !\n We welcome your valuable contributions to 'chandassu' !")

        self.text= text
        return self.text

    def generate( self ):

        l= self.tokenize()

        # print(l)
        marking= []
        
        # Edge: 
        # l= ["గ","ర్భం"] #['చ', "ష్ణున్"] #['చ', 'క్రాన్'] #['వి', 'ష్ణున్']
        # re.findall(r"\X","విర్"), re.findall(r"\X", "ప్చర్"), re.findall( r"\X", "ప్చార్")

        for index in range( len(l) ):

            if index < len(l)-1 :

                x= re.findall(r"\X", l[index+1])

                if x[-1].endswith('్'):
                    x= "".join(x[:-1])
                else:
                    x= "".join(x)   # ["గ","ర్భం"]

                d= Counter(x)
                del d["ర"]
                
                temp_count= 0
                for i in d:
                    if i in hallulu:
                        temp_count+= 1*d[i] # "పుత్త్రు"

                if 'ర' in l[index+1] and ((temp_count==0) or (temp_count == 1  and (not l[index+1].startswith('ర')))):
                    marking.append( lg_map[l[index][-1]] )
            

                else:
                    count= 0
                    for j in list(l[index+1]):
                        if j in varnamala:
                            count+= 1

                    if count > 1 and not l[index+1].endswith('్'):
                        marking.append( "U" )
                    
                    elif count > 1 and l[index+1].endswith('్') and re.findall( r"\X", l[index+1])[0].endswith('్'):
                        marking.append( "U" )
                    
                    elif count > 1 and l[index+1].endswith('్'):
                        marking.append( lg_map[l[index][-1]] )

                    else:
                        marking.append( lg_map[l[index][-1]] )
            
            elif l[index][-1] in lg_map:
                marking.append( lg_map[l[index][-1]] )

            else:
                print("Unknown Case (for future purpose) !\n We welcome your valuable contributions to 'chandassu' !")


        
        # Not dict because dict donot allow multiple keys with same name
        return list(zip(l, marking))