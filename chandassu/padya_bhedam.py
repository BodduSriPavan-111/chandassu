"""
Module: padya_bhedam.py
Description: Contains functions to check type of Padyam.
Author: Boddu Sri Pavan
License: MIT
"""

from .check_lakshanam import *
from .padyam_config import *

def check_teytageethi( lg_data, type= "teytageethi", weightage_factor= 1, verbose= True ):

    try:
        config= getattr(VupaJaathi, type, False)

        padamwise_ganam_data= []

        gana_kramam_score= 0
        end= 0
        paadam_count= 0

        while end< len(lg_data):

            ganam_data= []

            for j in range( len(config["gana_kramam"]) ):

                for i in config["gana_kramam"][j]:

                    # Take legth of corresponding ganam
                    ganam= tuple([k[1] for k in lg_data[end: end+len(ganamulu[i]) ]])

                    if verbose:
                        print("Ganam : ", ganam)

                    try:
                        if r_ganamulu[ ganam ] == i:
                            
                            ganam_data.append( [lg_data[end: end+len(ganamulu[i])], r_ganamulu[ganam]] )

                            gana_kramam_score+= 1
                            
                            if verbose:
                                print( [lg_data[end: end+len(ganamulu[i])], r_ganamulu[ganam]] )

                            break
                
                    except Exception as e:
                        print(e)
                        pass

                # Increment with the last ganam length (maximum)
                end+= len(ganamulu[i])
            
            paadam_count+= 1
            padamwise_ganam_data.append( ganam_data )

            if verbose:
                print( ganam_data )

        match_yati= []
        for line in padamwise_ganam_data:

            if verbose:
                print(line)
            
            yati_value= check_yati(     
                                        yati_sthanam= True,
                                        paadam= line, 
                                        first_letter= line[0][0][0][0], 
                                        yati_sthanam_letter= line[config["yati_sthanam"][0]-1][0][0][0], 
                                        verbose= True 
                                    )
            
            match_yati.append(yati_value)

            if verbose:
                print( yati_value )
    

        score= {
                    'n_paadalu': weightage_factor* paadam_count/ config["n_paadalu"],
                    'gana_kramam': weightage_factor* gana_kramam_score/ (config["n_paadalu"]*len(config["gana_kramam"])),
                    'yati_sthanam': weightage_factor* sum(match_yati)/ config["n_paadalu"],
                }
        
        overall_score= sum(score.values())/ len(score)

        if overall_score == 1:
            print("Padyam Detected: ", type.upper())
        
        else:
            print("Padyam not exactly matched with: ", type.upper())

        return {"chandassu_score": overall_score, "micro_score": score}
        
    except Exception as e:
        print( "Exception Occurred: ", str(e) )


def check_vruttam( 
                    lg_data, type, verbose= True, weightage_normalization= True,
                    weightage_factor= {"n_paadalu": 1, "n_aksharalu": 1, "gana_kramam": 1, "yati_sthanam": 1, "prasa": 1}                  
                ):

    try:
        if weightage_normalization:

            total= sum(weightage_factor.values())

            weightage_factor= {i:j/total for i, j in weightage_factor.items()}
            

        config= getattr(Vruttamu, type, False)

        if verbose:
            print(config)

        # There are 5 lakshanams (constraints/ rules) for a Vrutta padyam to be satisfied.
        # Following Macro technique as each one is given equal weightage.
        # Therefore, multiply each one with 1/5 = 0.2
        score= {
                    'n_paadalu': 0,
                    'n_aksharalu': 0,
                    'gana_kramam': 0,
                    'yati_sthanam': 0,
                    'prasa': 0
                }
        
        # 1. Check no.of paadams (lines)
        count_paadam= n_paadam( data= lg_data, aksharam_per_paadam= 20, clip= True, verbose= verbose )

        # 2. Check no.of aksharams (letters)
        count_aksharam= n_aksharam( data= lg_data, verbose= verbose )
        
        aksharam_per_paadam= config["n_aksharalu"]

        paadam_lg= [ lg_data[i*aksharam_per_paadam: (i+1)*aksharam_per_paadam] for i in range(4)]


        # 3. Match gana kramam in each paadam
        _, gana_kramam_score= check_vruttam_gana_kramam( lg_data, config, verbose= verbose )

        if verbose:
            print()

        # 4. Match yati in each paadam
        match_yati= []
        for i in range(len(paadam_lg)): #lines:
            line= [j[0] for j in paadam_lg[i]]

            try:
                yati_value= check_yati( paadam= line, yati_sthanam= config['yati_sthanam'], verbose= verbose )
                match_yati.append( yati_value )
            except:
                # Condition where no.of letters in a paadam are lesser than the yat number
                match_yati.append( False )

        try:
            o= [[paadam_lg[a][b][0] for b in range(len(paadam_lg[a]))] for a in range(len(paadam_lg))]
        except Exception as e:
            print(">>>>>", e)

        # 5. Match prasa in each paadam
        match_prasa= check_prasa( padya_paadaalu= [[paadam_lg[a][b][0] for b in range(len(paadam_lg[a]))] for a in range(len(paadam_lg))], 
                                index= 2, 
                                verbose= verbose
                                )

        # 'weightage_factor' can be modified for more insights
        score["n_paadalu"]= weightage_factor["n_paadalu"]*count_paadam/ config["n_paadalu"]
        score["n_aksharalu"]= weightage_factor["n_aksharalu"]* count_aksharam/ (config["n_paadalu"]*config["n_aksharalu"])
        score["gana_kramam"]= weightage_factor["gana_kramam"]* gana_kramam_score/ (config["n_paadalu"]*len(config["gana_kramam"]))
        score["yati_sthanam"]= weightage_factor["yati_sthanam"]*sum(match_yati)/ config["n_paadalu"]
        score["prasa"]= weightage_factor["prasa"]*max( match_prasa.values() )/ config["n_paadalu"]

        for sub_score in ["n_paadalu", "n_aksharalu", "gana_kramam", "yati_sthanam", "prasa"]:

            # Implementing compliment to avoid overflow
            if score[ sub_score ] > 1:
                score[sub_score]= 1- score[sub_score]

        overall_score= sum(score.values())/ len(score)

        if overall_score == 1:
            print("Padyam Detected: ", type.upper())
        
        else:
            print("Padyam not exactly matched with: ", type.upper())

        return {"chandassu_score": overall_score, "micro_score": score}
    
    except Exception as e:
        print("==========================================")
        print( "Given Padyam is not detected as: ", type )
        print( "Exception Occurred: ", str(e))
