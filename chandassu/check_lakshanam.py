"""
Module: lakshanam.py
Description: Contains functions to check lakshanamulu (constraints/ features) of padyam
Author: Boddu Sri Pavan
License: MIT
"""

from .laghuvu_guruvu import LaghuvuGuruvu
from .nidhi import achhulu, yati
from .panimuttu import *
from .ganam import ganamulu

import math

def n_paadam( data, aksharam_per_paadam, clip= False, verbose= True ):
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

    n= len(data)/ aksharam_per_paadam

    if clip:
        if n-int(n) != 0:
            n= math.floor( n )
    if verbose:
        print("No.of paadams (lines) found: ", n)
        print()
        
    return n

def n_aksharam( data, verbose= True ):

    # Implements same functionality
    # n_letters= []
    # for i in p.split("\n"):
    #     lg= LaghuvuGuruvu( data= i.strip() )
    #     n_letters.append( len(lg.tokenize()) )
    # return n_letters

    n= len(data)

    if verbose:
        print("No.of aksharams (letters): ", n)
        print()

    return n

def check_yati( paadam, yati_sthanam, verbose= True ):

    if verbose:
        print( paadam )

    first_letter= paadam[0]
    yati_sthanam_letter= paadam[ yati_sthanam-1 ]

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
            if verbose:
                print( "Yati Matched !")
            return True

        else:
            return False
        
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

def check_prasa( padya_paadaalu, index= 2, verbose= True ):

    frequency= {}

    for i in padya_paadaalu:
        try:
            aksharam= remove_gunintha_chihnam( i[index-1] )
            frequency[aksharam]= frequency.get( aksharam , 0) + 1
        except:
            pass
    if verbose:
        print( "Frequency of second aksharam (letter): ", frequency )
        if len( frequency ) != 1:
            print("Prasa Mismatch Occurred : ", frequency)
            print()
        else:
            print("Prasa Matched Successfully !")
            print()
    
    return frequency
    
def check_vruttam_gana_kramam( paadam_data, lakshanam_config, verbose= True ):
    expected_match= 0
    total_match= 0

    for index in range(len(paadam_data)):

        if verbose:
            print(f"Paadam-{index+1}\n--------")

        lg= paadam_data[index]

        paada_gana_kramam= tuple()
        for g in lakshanam_config["gana_kramam"]:
            paada_gana_kramam += ganamulu[g]

        try:
            n_match= 0
            for i in range(len(paada_gana_kramam)):
                
                if paada_gana_kramam[i]== lg[i][1]:
                    n_match+= 1
                    continue
                
                if verbose:
                    print(f"Ganam mismatch occurred in at {i+1}th aksharam (letter); found {lg[i]}, expected {paada_gana_kramam[i]}")
        except:
            pass

        expected_match+= len(paada_gana_kramam)
        total_match+= n_match  

        if verbose:
            print(f"No.of matches in paadam-{index}: {n_match} (expected {lakshanam_config['n_aksharalu']})")
            print()
      
    return total_match, expected_match