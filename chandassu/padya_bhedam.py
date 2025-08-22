"""
Module: padya_bhedam.py
Description: Contains functions to check type of Padyam.
Author: Boddu Sri Pavan
License: MIT
"""

from .check_lakshanam import *
from .padyam_config import *

TYPE_TO_BHEDAM_MAP= {
                        'kandamu': Jaathi,

                        'aataveladi': VupaJaathi, 
                        'teytageethi': VupaJaathi, 
                        'seesamu': VupaJaathi,

                        'vutpalamaala': Vruttamu, 
                        'champakamaala': Vruttamu,
                        'mattebhamu': Vruttamu,
                        'saardulamu': Vruttamu
                    }

VRUTTAMU= ["vutpalamaala", "champakamaala", "mattebhamu", "saardulamu"]

def check_padyam( lg_data, type= "aataveladi", return_micro_score= True, verbose= False):
    """
    ## Evaluates given Laghuvu-Guruvu data with given padyam type with confidence scores.
    
    ## Parameters
    -------------
    1. lg_data: list
        - Laghuvu-Guruvu data generated using laghuvu_guruvu.LaghuvuGuruvu.generate()
    2. type: str
        - Type of padyam
        - Supported types: 'kandamu', 'aataveladi', 'teytageethi', 'seesamu', 'vutpalamaala',
                            'champakamaala', 'mattebhamu', 'saardulamu'
    3. return_micro_score: bool
        - Set to 'True' to returns lakshanamwise scores (micro scores).
        - Default is set to 'True'.
    4. verbose: bool
        - Prints the result of each step.
        - For traceability.
        - Default is set to 'False'.

    ## Returns
    ----------
    Dictionary of scores (Chandassu Score and Micro Score).
    """
    
    bhedam= TYPE_TO_BHEDAM_MAP[type]

    if verbose:
        print("Type: ", type)
        print("Bhedam: ", bhedam)

    config= getattr(bhedam, type, False)
    
    # Holds Laghuvu-Guruvu data for each Paadam (Padyam line)
    # Data Format
    # -----------
    # padamwise_ganam_data= [ paadam_1, paadam_2, paadam_3, ..., paadam_n ]
    # paadam_n= [ ganam_match_1, ganam_match_2, ganam_match_3, ..., ganam_match_n ]
    # ganam_match_n= [ LaghuvuGuruvu_data, Matched/ UnMatched flag]
    padamwise_ganam_data= []

    gana_kramam_score= 0
    end= 0
    paadam_count= 0

    # Parse with respect to each line of padyam (Paadam)
    for line in range( len( config["gana_kramam"] ) ):

        ganam_data= []

        for j in range( len(config["gana_kramam"][line]) ):

            ganam_match_flag= False
            
            if verbose:
                print( config["gana_kramam"][line][j])

            for i in config["gana_kramam"][line][j]:

                # Take legth of corresponding ganam
                ganam= tuple([k[1] for k in lg_data[end: end+len(ganamulu[i]) ]])
                
                if verbose:
                    print("Ganam : ", ganam)

                try:
                    # If matched
                    if r_ganamulu[ ganam ] == i:
                        
                        ganam_data.append( [lg_data[end: end+len(ganamulu[i])], r_ganamulu[ganam]] )

                        # Increment 'Gana Kramam Score'
                        gana_kramam_score+= 1
                        
                        if verbose:
                            print( [lg_data[end: end+len(ganamulu[i])], r_ganamulu[ganam]] )

                        ganam_match_flag= True

                        break
                
                except KeyError as e:

                    if verbose:
                        print( "Key Not Found: ", ganam )
                        print( "Exception: ", str(e) )

                except Exception as e:
                    print(e)
                    pass
            
            # If ganam not matched then unmatched tracing
            if ganam_match_flag == False:
                ganam_data.append( [lg_data[end: end+len(ganamulu[i])], "UnMatched"] )
            
            # Increment with the last ganam length (maximum)
            end+= len(ganamulu[i])

        if verbose:
            print( line, end, len(lg_data), ganam_data )
        
        # Consider atleast one character to consider new line as paadam
        if len(ganam_data[0][0]) > 1:
            paadam_count+= 1

        padamwise_ganam_data.append( ganam_data )
        
        if end == len(lg_data):
            if verbose:
                print("Paadam wise split completed")
            break
    
    # Check Yati/ Prasa Yati as per Padyam configuration
    prasa_yati_match= check_prasa_yati( padamwise_ganam_data= padamwise_ganam_data, type= type, config= config, verbose= verbose, only_generic_yati= config["only_generic_yati"])

    if verbose:
        print("Paadam Count: ", paadam_count)
        print("Ganam Kramam Score: ", gana_kramam_score)
        print("Paadam-wise Yati: ", prasa_yati_match)


    N_PAADALU= config.get("true_n_paadalu", -1)
    if N_PAADALU == -1: # Not Present
        N_PAADALU= config["n_paadalu"]

        if verbose:
            print("true_n_paadalu parameter found in config", N_PAADALU)

    total_yati_paadalu= len(config["yati_paadalu"])

    # Seesamu padyam, for convineience considered pseudo paadam count as 8
    # Therefore, halving it
    if type== "seesamu":
        paadam_count= paadam_count/2
    
    # Calculate lakshanamwise scores (micro scores)
    score= {
                'n_paadalu':  paadam_count/ N_PAADALU,
                'gana_kramam': gana_kramam_score/ sum([len(i) for i in config["gana_kramam"]]),
                'yati_sthanam': sum(prasa_yati_match)/ total_yati_paadalu
            }

    # This conditions becomes True only for Vruttamu
    if config.get("n_aksharalu", False):

        # Aksharam Count Score
        aksharam_count= 0

        # Iterate through each Paadam (Padyam Line)
        for i in padamwise_ganam_data:
            
            if verbose:
                print(i)

            for j in i:

                if verbose:   
                    print(j[0], len(j[0]))

                aksharam_count+= len(j[0])

        # This is to quantify the overflow as unexpected
        # This will activate only when No.of aksharams in given > No.of aksharams in expected
        # Else: 0
        subtract_factor= len(lg_data) - aksharam_count

        score["n_aksharalu"]= (aksharam_count-subtract_factor)/ (N_PAADALU*config["n_aksharalu"])

    # This conditions becomes True only for Vruttamu and Jaathi
    if config.get("prasa", False):

        # Prasa Score
        index= 2    # Second letter

        frequency= {}

        # Iterate through each Paadam (Padyam Line)
        for i in padamwise_ganam_data:

            try:
                aksharam= remove_gunintha_chihnam(i[0][0][ index-1 ][0])
                frequency[aksharam]= frequency.get( aksharam , 0) + 1
                
                if verbose:
                    print(aksharam)
            except:
                pass

        if verbose:
            print( "Frequency of second aksharam (letter): ", frequency )
            if len( frequency ) != 1:
                print("Prasa Mismatch Occurred : ", frequency )
                print()

            elif (len(frequency) == 1) and (max(frequency.values()) == config["n_paadalu"]): # As 'seesamu' has no necessary condition to check prasa, can be ignored
                print("Prasa Matched Successfully !")
                print()

            else:
                print("Prasa Mismatch Occurred : ", frequency )
                print()

        score["prasa"]= max( frequency.values() )/ N_PAADALU

    # Calculate 'Chandassu Score': Average of all lakshanamwise scores for given Padyam type
    overall_score= sum(score.values()) / len(score)

    if return_micro_score:
            return {"chandassu_score": overall_score, "micro_score": score}

    return {"chandassu_score": overall_score}




# def check_teytageethi( lg_data, type= "teytageethi", verbose= True, weightage_normalization= True,
#                         weightage_factor= {"n_paadalu": 1, "gana_kramam": 1, "yati_sthanam": 1}, return_micro_score= True
#                     ):

#     try:

#         # Weightage factor parameter check
#         for i in ["n_paadalu", "gana_kramam", "yati_sthanam"]:
#             if i not in weightage_factor:
#                 print( "Not present in 'weightage_factor': ", i )
#                 return False

#         if weightage_normalization:

#             total= sum(weightage_factor.values())

#             weightage_factor= {i:j/total for i, j in weightage_factor.items()}

#         config= getattr(VupaJaathi, type, False)

#         padamwise_ganam_data= []

#         gana_kramam_score= 0
#         end= 0
#         paadam_count= 0

#         while end< len(lg_data):

#             ganam_data= []

#             for j in range( len(config["gana_kramam"]) ):

#                 for i in config["gana_kramam"][j]:

#                     # Take legth of corresponding ganam
#                     ganam= tuple([k[1] for k in lg_data[end: end+len(ganamulu[i]) ]])

#                     if verbose:
#                         print("Ganam : ", ganam)

#                     try:
#                         if r_ganamulu[ ganam ] == i:
                            
#                             ganam_data.append( [lg_data[end: end+len(ganamulu[i])], r_ganamulu[ganam]] )

#                             gana_kramam_score+= 1
                            
#                             if verbose:
#                                 print( [lg_data[end: end+len(ganamulu[i])], r_ganamulu[ganam]] )

#                             break
                
#                     except Exception as e:
#                         print(e)
#                         pass

#                 # Increment with the last ganam length (maximum)
#                 end+= len(ganamulu[i])
            
#             paadam_count+= 1
#             padamwise_ganam_data.append( ganam_data )

#             if verbose:
#                 print( ganam_data )

#         match_yati= []
#         for line in padamwise_ganam_data:

#             if verbose:
#                 print(line)
            
#             yati_value= check_yati(     
#                                         yati_sthanam= True,
#                                         paadam= line, 
#                                         first_letter= line[0][0][0][0], 
#                                         yati_sthanam_letter= line[config["yati_sthanam"][0]-1][0][0][0], 
#                                         verbose= verbose 
#                                     )
            
#             match_yati.append(yati_value)

#             if verbose:
#                 print( yati_value )
    

#         score= {
#                     'n_paadalu': weightage_factor['n_paadalu']* paadam_count/ config["n_paadalu"],
#                     'gana_kramam': weightage_factor['gana_kramam']* gana_kramam_score/ (config["n_paadalu"]*len(config["gana_kramam"])),
#                     'yati_sthanam': weightage_factor['yati_sthanam']* sum(match_yati)/ config["n_paadalu"],
#                 }
        
#         overall_score= sum(score.values())

#         if overall_score == 1:
#             print("Padyam Detected: ", type.upper())
        
#         else:
#             print("Padyam not exactly matched with: ", type.upper())

#         for i in score:
#             score[i]= (score[i], weightage_factor[i])
        
#         if return_micro_score:
#             return {"chandassu_score": overall_score, "micro_score": score}
        
#         return {"chandassu_score": overall_score}
    
#     except Exception as e:
#         print( "Exception Occurred: ", str(e) )

# def check_vruttam( 
#                     lg_data, type, verbose= True, weightage_normalization= True,
#                     weightage_factor= {"n_paadalu": 1, "n_aksharalu": 1, "gana_kramam": 1, "yati_sthanam": 1, "prasa": 1},
#                     return_micro_score= True                  
#                 ):

#     try:

#         # Weightage factor parameter check
#         for i in ["n_paadalu", "n_aksharalu", "gana_kramam", "yati_sthanam", "prasa"]:
#             if i not in weightage_factor:
#                 print( "Not present in 'weightage_factor': ", i )
#                 return False
            
#         if weightage_normalization:

#             total= sum(weightage_factor.values())

#             weightage_factor= {i:j/total for i, j in weightage_factor.items()}
            

#         config= getattr(Vruttamu, type, False)

#         if verbose:
#             print(config)

#         # There are 5 lakshanams (constraints/ rules) for a Vrutta padyam to be satisfied.
#         # Following Macro technique as each one is given equal weightage.
#         # Therefore, multiply each one with 1/5 = 0.2
#         score= {
#                     'n_paadalu': 0,
#                     'n_aksharalu': 0,
#                     'gana_kramam': 0,
#                     'yati_sthanam': 0,
#                     'prasa': 0
#                 }
        
#         # 1. Check no.of paadams (lines)
#         count_paadam= n_paadam( data= lg_data, aksharam_per_paadam= 20, clip= True, verbose= verbose )

#         # 2. Check no.of aksharams (letters)
#         count_aksharam= n_aksharam( data= lg_data, verbose= verbose )
        
#         aksharam_per_paadam= config["n_aksharalu"]

#         paadam_lg= [ lg_data[i*aksharam_per_paadam: (i+1)*aksharam_per_paadam] for i in range(4)]


#         # 3. Match gana kramam in each paadam
#         _, gana_kramam_score= check_vruttam_gana_kramam( lg_data, config, verbose= verbose )

#         if verbose:
#             print()

#         # 4. Match yati in each paadam
#         match_yati= []
#         for i in range(len(paadam_lg)): #lines:
#             line= [j[0] for j in paadam_lg[i]]

#             try:
#                 yati_value= check_yati( paadam= line, yati_sthanam= config['yati_sthanam'], verbose= verbose )
#                 match_yati.append( yati_value )
#             except:
#                 # Condition where no.of letters in a paadam are lesser than the yat number
#                 match_yati.append( False )

#         try:
#             o= [[paadam_lg[a][b][0] for b in range(len(paadam_lg[a]))] for a in range(len(paadam_lg))]
#         except Exception as e:
#             print(">>>>>", e)

#         # 5. Match prasa in each paadam
#         match_prasa= check_prasa( padya_paadaalu= [[paadam_lg[a][b][0] for b in range(len(paadam_lg[a]))] for a in range(len(paadam_lg))], 
#                                 index= 2, 
#                                 verbose= verbose
#                                 )

#         # 'weightage_factor' can be modified for more insights
#         score["n_paadalu"]= weightage_factor["n_paadalu"]*count_paadam/ config["n_paadalu"]
#         score["n_aksharalu"]= weightage_factor["n_aksharalu"]* count_aksharam/ (config["n_paadalu"]*config["n_aksharalu"])
#         score["gana_kramam"]= weightage_factor["gana_kramam"]* gana_kramam_score/ (config["n_paadalu"]*len(config["gana_kramam"]))
#         score["yati_sthanam"]= weightage_factor["yati_sthanam"]*sum(match_yati)/ config["n_paadalu"]
#         score["prasa"]= weightage_factor["prasa"]*max( match_prasa.values() )/ config["n_paadalu"]

#         for sub_score in ["n_paadalu", "n_aksharalu", "gana_kramam", "yati_sthanam", "prasa"]:

#             # Implementing compliment to avoid overflow
#             if score[ sub_score ] > 1:
#                 score[sub_score]= 1- score[sub_score]

#         overall_score= sum(score.values())

#         if overall_score == 1:
#             print("Padyam Detected: ", type.upper())
        
#         else:
#             print("Padyam not exactly matched with: ", type.upper())

#         for i in score:
#             score[i]= (score[i], weightage_factor[i])

#         if return_micro_score:
#             return {"chandassu_score": overall_score, "micro_score": score}

#         return {"chandassu_score": overall_score}

#     except Exception as e:
#         print("==========================================")
#         print( "Given Padyam is not detected as: ", type )
#         print( "Exception Occurred: ", str(e))
 