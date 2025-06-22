"""
Module: lakshanam.py
Description: Contains functions to check lakshanamulu (constraints/ features) of padyam
Author: Boddu Sri Pavan
Date: 22-06-2025
License: MIT
"""

from .laghuvu_guruvu import LaghuvuGuruvu
from .nidhi import achhulu, yati
from .panimuttu import *
from .ganam import ganamulu

def n_paadam( padyam, verbose= True ):
    """
    Count no.of paadams (lines) in given padyam.
    
    Attributes
    ----------
    padyam (str): Input padyam
    verbose (str): Flag to print tracing steps
    
    Return
    ------
    n (int): Count of no.of paadams
    """
    
    split_data= padyam.split("\n")
    n= len(split_data)

    if verbose:
        print("No.of paadams (lines) found: ", n)
        print("Paadams (lines)\n---------------\n", split_data)
        
    return n

def n_aksharam( padyam, verbose= True ):

    # Implements same functionality
    # n_letters= []
    # for i in p.split("\n"):
    #     lg= LaghuvuGuruvu( data= i.strip() )
    #     n_letters.append( len(lg.split_by_letter()) )
    # return n_letters

    n= [ len(LaghuvuGuruvu(data= i.strip()).split_by_letter()) for i in padyam.split("\n")]

    if verbose:
        print("No.of aksharams (letters) in each paadam (line):")
        for i in range(len(n)):
            print("Paadam-",i, " :", n[i])

    return n

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

    if verbose:
        print("First aksharam (letter): ", first_letter)
        print("Yati sthana aksharam (letter): ", yati_sthanam_letter)

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
                    if verbose:
                        print(f"Chihna yati mismatch occurred between '{chihnam_a}' in '{first_letter}'  and '{chihnam_b}' in '{yati_sthanam_letter}'")
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
                    
                    if not flag and verbose:
                        print(f"Yati mismatch occurred between '{i}' in '{first_letter}' and '{yati_sthanam_letter}'")

        if chihna_yati and flag:
            print( "Yati Matched !")
            return True
        
    else:
        if len(first_letter)==1 and first_letter not in achhulu:
            first_letter= [first_letter]+[' ']

        if len(yati_sthanam_letter)==1 and first_letter not in achhulu:
            yati_sthanam_letter= [yati_sthanam_letter]+[" "]

        to_return= False
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
                        # No break statement should be used here
                        # Because same aksharam could be present in multiple associations

                        if verbose:
                            print(f"Yati mismatch occurred between: '{i}' in '{first_letter}' and '{yati_sthanam_letter}'")
        
        if all( temp ):
            if verbose:
                print( "Yati Matched Successfully!" )
            to_return= True

        return to_return

def check_prasa( padyam, index= 1, verbose= True ):

    padya_paadaalu= padyam.split("\n")

    frequency= {}

    for i in padya_paadaalu:
        aksharam= remove_gunintha_chihnam( LaghuvuGuruvu( data= i ).split_by_letter()[index] )
        frequency[aksharam]= frequency.get( aksharam , 0) + 1

    if verbose:
        print( "Frequency of second aksharam (letter): ", frequency )
        if len( frequency ) != 1:
            print("Prasa Mismatch Occurred !")
        else:
            print("Prasa Matched Successfully !")
    
    return frequency
    
def check_vruttam_gana_kramam( padyam, lakshanam_config, verbose= True ):
    expected_match= 0
    total_match= 0

    paadam_data= extract_paadam( padyam= padyam )

    for index in range(len(paadam_data)):

        if verbose:
            print(f"Paadam-{index+1}\n--------")

        paadam= paadam_data[index]
        lg= LaghuvuGuruvu( data= paadam ).generate()

        paada_gana_kramam= tuple()
        for g in lakshanam_config["gana_kramam"]:
            paada_gana_kramam += ganamulu[g]

        n_match= 0
        for i in range(len(paada_gana_kramam)):
            
            if paada_gana_kramam[i]== lg[i][1]:
                n_match+= 1
                continue
            
            if verbose:
                print(f"Ganam mismatch occurred in at {i+1}th aksharam (letter); found {lg[i]}, expected {paada_gana_kramam[i]}")

        expected_match+= len(paada_gana_kramam)
        total_match+= n_match  

        if verbose:
            print(f"No.of matches in paadam-{index}: {n_match} (expected {lakshanam_config['n_aksharalu']})")
      
    return total_match, expected_match