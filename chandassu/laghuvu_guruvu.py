import regex as re
from .nidhi import lg_map, varnamala, gunintha_chihnam

class LaghuvuGuruvu:

    def __init__(self, data):

        self.data= data


    def split_by_letter( self ):

        l= re.findall(r"\X", self.data)

        index= 0
        text= []
        temp= ""

        for index in range( len(l) ):

            if l[index].isspace() or l[index] in list("""` ~ ! @ # $ % ^ & * ( ) _ - + = { } [ ] \ | ; : ' " , < > . / ?"""):
                # text.append( l[index] )
                pass

            elif l[index].endswith('్') and temp == "" and index< len(l)-1 and not l[index+1].isspace():
                temp+= l[index]

            elif (not l[index].endswith('్')) and temp != "":
                text.append( temp+l[index] )
                temp= ""
            
            elif (not l[index].endswith('్')) and temp == "":
                text.append( l[index] )
                temp= ""
            
            elif l[index].endswith('్') and (index+1 == len(l) or l[index+1].isspace() ):
                text[-1]+= l[index]

            else:
                print("Unknown Case (for future purpose) !")

        self.text= text
        return self.text

    def generate( self ):

        l= self.split_by_letter()
        print(l)

        marking= []

        for index in range( len(l) ):

            if index < len(l)-1 :

                if 'ద' in l[index+1] and 'ర' in l[index+1]:
                    marking.append( lg_map[l[index][-1]] )

                else:
                    count= 0
                    for j in list(l[index+1]):
                        if j in varnamala:
                            count+= 1

                    if count > 1 and not l[index+1].endswith('్'):
                        marking.append( "U" )
                    
                    elif count > 1 and l[index+1].endswith('్'):
                        marking.append( lg_map[l[index][-1]] )

                    else:
                        marking.append( lg_map[l[index][-1]] )
            
            elif l[index][-1] in lg_map:
                marking.append( lg_map[l[index][-1]] )

            else:
                print("Unhandled Condition")
        
        # Not dict because dict donot allow multiple keys with same name
        return list(zip(l, marking))
