import regex as re
from .dictionary import lg_map, varnamala, gunintha_chihnam

class LaghuvuGuruvu:

    def __init__(self, data):

        self.data= data


    def split_by_letter( self ):

        l= re.findall(r"\X", self.data)

        index= 0
        text= []
        temp= ""

        for index in range( len(l) ):

            if l[index].endswith('్') and temp == "":
                temp+= l[index]

            elif (not l[index].endswith('్')) and temp != "":
                text.append( temp+l[index] )
                temp= ""
            
            elif (not l[index].endswith('్')) and temp == "":
                text.append( l[index] )
                temp= ""
            
            else:
                print("Unknown Case (for future purpose) !")

        self.text= text
        return self.text

    def generate( self ):

        l= list( self.split_by_letter() )

        marking= []

        for i in range( len(l) ):

            if l[i].isspace():
                marking.append( l[i] )

            if i < len(l)-1 :
                if 'ద' in l[i+1] and 'ర' in l[i+1]:
                    marking.append( "|" )
                    continue
                else:
                    count= 0
                    for j in list(l[i+1]):
                        if j in varnamala:
                            count+= 1

                    if count > 1:
                        marking.append( "U" )
                        continue
            
            if l[i][-1] in gunintha_chihnam:
                marking.append( lg_map[l[i][-1]] )

            elif l[i][-1] not in gunintha_chihnam and l[i][-1] in varnamala:
                marking.append( lg_map[l[i][-1]] )
            
            elif l[i] in varnamala:
                marking.append( lg_map[l[i]] )
            
        return dict(zip(l, marking))
