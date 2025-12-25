"""
Module: lakshanam.py
Description: Contains functions to check lakshanamulu (constraints/ features) of padyam.
Author: Boddu Sri Pavan
License: MIT
"""

from .laghuvu_guruvu import LaghuvuGuruvu
from .nidhi import achhulu, yati, hraswa_chihnam, deergha_chihnam
from .panimuttu import *
from .ganam import *

import math

def check_yati( yati_sthanam= None, paadam= None, first_letter= None, yati_sthanam_letter= None, verbose= True ):
    """
    ## Check whether Paadam (Padyam line) is satisfying Yati constraint.
    
    ## Parameters
    -------------
    1. yati_sthanam: int
        - Position of corresponding Yati (Natural Number as per Telugu literature).
    2. paadam: list
        - LaghuvuGuruvu data.
    3. first_letter: str
        - Aksharam Token at Yati position (Generally the first Aksharam Token in Padyam).
    4. yati_sthanam_letter: str
        - Corresponding position to Yati position as per Padyam configuration.
    5. verbose: bool
        - Prints the result of each step.
        - For traceability.
        - Default is set to 'False'.

    ## Returns
    ----------
    'True' is Yati constraint is satisfied else 'False'.
    """
    
    # Initialize 'first_letter' and 'yati_sthanam_letter' if not passed to the function
    if first_letter == None and yati_sthanam_letter == None :
        if verbose:
            print( paadam )

        first_letter= paadam[0]
        yati_sthanam_letter= paadam[ yati_sthanam-1 ]

    # Ignoring Visarga and PurnaBindu (As not mentioned in the reference book)
    first_letter= first_letter.replace('ం', "").replace('ః', "")
    first_letter= first_letter.replace("ಂ", "").replace( 'ః', "")
    yati_sthanam_letter= yati_sthanam_letter.replace('ం', "").replace('ః', "")
    yati_sthanam_letter= yati_sthanam_letter.replace("ಂ", "").replace('ః', "")

    if verbose:
        print("First aksharam (letter): ", first_letter)
        print("Yati sthana aksharam (letter): ", yati_sthanam_letter)

    # Check Samslistaaksharam (conjuct)
    samdit= False
    if len(extract_aksharam(first_letter))> 1:
        samdit= True

    if samdit or (not samdit):
        
        # Extract Gunintha Chihnam
        chihnam_a= extract_gunintha_chihnam( first_letter )
        chihnam_b= extract_gunintha_chihnam( yati_sthanam_letter )

        # Chihna Yati: Yati checking for vowel symbol
        chihna_yati= False
        for i in yati:

            if chihnam_a in i:

                if chihnam_b in i:
                    chihna_yati= True

                else:
                    if verbose:
                        print(f"Chihna yati mismatch occurred between '{chihnam_a}' in '{first_letter}'  and '{chihnam_b}' in '{yati_sthanam_letter}'")
                    return False

        # Akshara Yati: Yati check for other than vowel sound
        # సంయుక్తాక్షరాలు వచ్చిన చోట, యతి కోసం ఏ అక్షరాన్నైనా గణించవచ్చు. ఉదా: "క్రొ" మొదటి అక్షరం అనుకోండి. యతి మైత్రి కోసం దీన్ని "కొ"గా గానీ "రొ"గా గానీ భావించ వచ్చు. 
        akshara_yati= False
        for i in list(set(extract_aksharam(first_letter))):

            for j in yati:
                
                if i in j:
                    
                    for k in list(set(extract_aksharam(yati_sthanam_letter))):
                        
                        if k in j:

                            akshara_yati= True

                            if verbose:
                                print(i, j, k)

                            # Atleast one of samyukta dwitwa aksharam is enough for yati
                            break
                    
                    if akshara_yati == True:
                        break
        
        if not akshara_yati:

            if verbose:
                print(f"Yati mismatch occurred between '{i}' in '{first_letter}' and '{yati_sthanam_letter}'")

            return False


        if chihna_yati and akshara_yati:

            if verbose:
                print( "Yati Matched !")

            return True

        else:

            if verbose:
                print("Chihna Yati: ", chihna_yati)
                print("Akshara Yati: ", akshara_yati)

            return False
        
    # else:

    #     if len(first_letter)==1 and first_letter not in achhulu:
    #         first_letter= [first_letter]+[' ']

    #     if len(yati_sthanam_letter)==1 and first_letter not in achhulu:
    #         yati_sthanam_letter= [yati_sthanam_letter]+[" "]

    #     to_return= False
    #     temp= []
    #     for i in first_letter:

    #         for j in yati:

    #             if i in j:
                    
    #                 flag= False
    #                 for k in yati_sthanam_letter:
    #                     if k in j:
    #                         flag= True
    #                         break

    #                 if flag== True:
    #                     temp.append( True )
    #                 else:
    #                     temp.append( False )
    #                     # No break statement should be used here
    #                     # Because same aksharam could be present in multiple associations

    #                     if verbose:
    #                         print(f"Yati mismatch occurred between: '{i}' in '{first_letter}' and '{yati_sthanam_letter}'")
        
    #     if all( temp ):
    #         if verbose:
    #             print( "Yati Matched Successfully!" )
    #         to_return= True

        # return to_return

def check_prasa_yati( padamwise_ganam_data, type, config, only_generic_yati= False, verbose= True):
    """
    ## Check Prasa Yati for given Paadamwise Laghuvu-Guruvu data.
    
    ## Parameters
    -------------
    1. padamwise_ganam_data: list
        - List of Ganamwise LaghuvuGuruvu data with Matched/UnMatched flag.
    2. type: str
        - Type of Padyam.
    3. config: dict
        - Configuration of Padyam.
    4. only_generic_yati: bool
        - Flag to apply Prasa Yati.
        - Default is set to 'False'.
    5. verbose: bool
        - Prints the result of each step.
        - For traceability.
        - Default is set to 'False'.

    ## Returns
    ----------
    List of boolean values where index(i) corresponds to (i+1)th Paadam (Padyam Line) Yati match value.
    """
    
    if verbose:
        print( "Paadalu to follow Yati: ", config["yati_paadalu"] )
        print( "No.of paadalu to follow Yati: ", len(config["yati_paadalu"]))

    # Kanda Padyam Yati: 2,4 Paadalu only
    # Remaining Padyams all paadams are having Yati
    if type == "kandamu":
        padamwise_ganam_data= [ padamwise_ganam_data[i-1] for i in config["yati_paadalu"] ] 
    
    if verbose:
        print("Updated paadamwise_ganam_data: ")
        print( padamwise_ganam_data )
        
    yati_match= []

    # Iterate through each Paadam (Padyam line)
    for row in padamwise_ganam_data:
        
        if verbose:
            print(row)

        if (len(row[0][0]) > 1) and (len(row[ config["yati_sthanam"][0]-1 ][0]) > 1 ):

            # Extract Aksharam Token in Yati position
            first_letter= [a[0] for a in row[0][0]]

            # Extract Aksharam Token in corresponding position to Yati as per Padyam configuration
            yati_sthanam_letter= row[ config["yati_sthanam"][0]-1 ][0][ config["yati_sthanam"][1] ]
            
            # Check 'Generic Yati' (Not Prasa Yati)
            generic_yati= check_yati( first_letter= first_letter[0], yati_sthanam_letter= yati_sthanam_letter[0], verbose= verbose )
            
            # If 'Generic Yati' constraint is satisfied then no need to check 'Prasa Yati' (as per current Padyam types)
            if only_generic_yati:

                if verbose:
                    print( "Generic Yati: ", generic_yati )
                    print( first_letter, yati_sthanam_letter )

                yati_match.append( generic_yati )

                continue
            
            # This extracts two aksharas yati-sthanam letter and its succeeding (For Prasa Yati implementation)
            yati_sthanam_letter= [a[0] for a in row[ config["yati_sthanam"][0]-1 ][0]][:2]

            prasa_yati_match= False

            if generic_yati:
                if verbose:
                    print("Generic Yati Matched")
                yati_match.append( True )

            else:
                
                # Reference: https://te.wikipedia.org/wiki/%E0%B0%AA%E0%B1%8D%E0%B0%B0%E0%B0%BE%E0%B0%B8%E0%B0%AF%E0%B0%A4%E0%B0%BF

                # Yati Sthanam: Hraswa-Deergham Check
                hraswa_deergham_flag_1= " "

                if first_letter[0][-1] in gunintha_chihnam:
                    hraswa_deergham_flag_1= first_letter[0][-1]
                else:
                    hraswa_deergham_flag_1= " "

                hraswa_deergham_flag_2= ""

                if yati_sthanam_letter[0][-1] in gunintha_chihnam:
                    hraswa_deergham_flag_2= yati_sthanam_letter[0][-1]
                else:
                    hraswa_deergham_flag_2= " "


                # Prasa Sthanam: Prasa Check
                l1= remove_gunintha_chihnam( first_letter[1] )
                l2= remove_gunintha_chihnam( yati_sthanam_letter[1] )
                
                # Yati Sthanam
                if ( hraswa_deergham_flag_1 in hraswa_chihnam and hraswa_deergham_flag_2 in hraswa_chihnam ):
                    
                    if verbose:
                        print("Both Yati Sthanam aksharam: Hraswa")

                    # Prasa Sthanam
                    if  l1 == l2 :
                        prasa_yati_match= True
                        if verbose:
                            print("Both Yati Sthanam chihnam matched")
                    else:
                        if verbose:
                            print("Second Letter Mismatched: ", l1, "===", l2)

                elif ( hraswa_deergham_flag_1 in deergha_chihnam and hraswa_deergham_flag_2 in deergha_chihnam ):
                    
                    if verbose:
                        print("Both Yati Sthanam aksharam: Deergham ")

                    if l1 == l2:
                        prasa_yati_match= True
                        if verbose:
                            print("Both Yati Sthanam chihnam matched")
                    else:
                        if verbose:
                            print("Second Letter Mismatched: ", l1, "===", l2)

                else:
                    if verbose:
                        print("First Akshara Chihnam in Prasa Yati Mis-matched")
                        print("First Akshara Chihnam: ", hraswa_deergham_flag_1)
                        print("Prasa Yathi Akshara Chihnam: ", hraswa_deergham_flag_2)

                if prasa_yati_match:
                    yati_match.append( True )
                    
                    if verbose:
                        print("Prasa Yati Matched")

                else:

                    if verbose:
                        print("Prasa Yati Mis-matched")

            # If 'generic_yati' and  'prasa_yati_match' did not match
            if generic_yati == False and prasa_yati_match == False:
                yati_match.append( False )
                if verbose:
                    print("Both Yati and PrasaYati mis-matched")
        else:
            yati_match.append( False )
            
            if verbose:
                print("No paadam found")

    return yati_match





def n_aksharam( data, verbose= True ):
    """
    ## Counts no.of Aksharam Tokens from the given LaghuvuGuruvu data.

    ## Parameters
    -------------
    1. data: list
        - LaghuvuGuruvu data.
    2. verbose: bool
        - Prints the result of each step.
        - For traceability.
        - Default is set to 'False'.
    
    ## Note
    -------
    For future purpose.
    """
    
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

def n_paadam( data, aksharam_per_paadam, clip= False, verbose= True ):
    """
    ## Count no.of paadams (lines) in given padyam.
    
    ## Parameters
    -------------
    1. data: list
        - LaghuvuGuruvu data.
    2. aksharam_per_paadam: int
        - No.of Aksharam Tokens for Paadam (Padyam Line).
    3. clip: bool
        - To apply floor.
    4. verbose: str
        - Flag to print tracing steps.
    
    ## Returns
    ----------
    Count (int) of no.of paadams.

    ## Note
    -------
    For future purpose.
    """

    n= len(data)/ aksharam_per_paadam

    if clip:
        if n-int(n) != 0:
            n= math.floor( n )
    if verbose:
        print("No.of paadams (lines) found: ", n)
        print()
        
    return n