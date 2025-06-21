from .laghuvu_guruvu import LaghuvuGuruvu
from .nidhi import varnamala, gunintha_chihnam, yati

def n_paadam( padyam ):

    return len(padyam.split("\n"))

def n_aksharam( padyam ):

    # n_letters= []
    # for i in p.split("\n"):
    #     lg= LaghuvuGuruvu( data= i.strip() )
    #     n_letters.append( len(lg.split_by_letter()) )
    # return n_letters

    return [ len(LaghuvuGuruvu(data= i.strip()).split_by_letter()) for i in padyam.split("\n")]

def check_yati( paadam, yati_sthanam, verbose= True ):

    letters= LaghuvuGuruvu( data= paadam ).split_by_letter()

    if verbose:
        print( letters)

    first_letter= letters[0]
    yati_sthanam_letter= letters[ yati_sthanam-1 ]

    first_letter= first_letter.replace('ం', "")
    first_letter= first_letter.replace("ಂ", "")
    yati_sthanam_letter= yati_sthanam_letter.replace('ం', "")
    yati_sthanam_letter= yati_sthanam_letter.replace("ಂ", "")

    samdit= False
    if len(extract_aksharam(first_letter))> 1:
        samdit= True

    if samdit:
        chihnam_a= extract_gunintha_chihnam( first_letter )
        chihnam_b= extract_gunintha_chihnam( yati_sthanam_letter )

        chihna_yati= False

        for i in yati:

            if chihnam_a in i:

                if chihnam_b in i:
                    chihna_yati= True

                else:
                    print("Chihna Yathi Unmatched !", chihnam_a)
                    return False

        flag= False

        for i in list(set(extract_aksharam(first_letter))):
            print(i)
            for j in yati:

                if i in j:

                    flag= False
                    for k in list(set(extract_aksharam(yati_sthanam_letter))):
                        
                        if k in j:
                            flag= True
                            break
        
        if chihna_yati and flag:
            print( "Yathi Matched !")
            return True


    else:
        if len(first_letter)==1:
            first_letter= [first_letter]+[' ']

        if len(yati_sthanam_letter)==1:
            yati_sthanam_letter= [yati_sthanam_letter]+[" "]

        temp= []
        for i in first_letter:

            for j in yati:

                if i in j:
                    
                    flag= False
                    for k in yati_sthanam_letter:
                        if k in j:
                            flag= True
                            break

                    if flag== True:
                        temp.append( True )
                    else:
                        temp.append( False )
                        print("Yathi Unmatched !", i)
                        return False
        
        if all( temp ):
            print( "YAthi MAtched !" )
            return True

def check_prasa( padyam, index= 1 ):

    padya_paadaalu= padyam.split("\n")

    frequency= {}

    for i in padya_paadaalu:
        aksharam= remove_gunintha_chihnam( LaghuvuGuruvu( data= i ).split_by_letter()[index] )
        frequency[aksharam]= frequency.get( aksharam , 0) + 1

    print( frequency )
    if len( frequency ) != 1:
        print("Prasa Mismatch occurred !")
        return None
    else:
        print("Prasa Matched Successfully !")
        return frequency