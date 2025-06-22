from .check_lakshanam import *
from .padyam_config import *

def check_vruttam( padyam, type, weightage_factor= 1, verbose= True ):

    config= getattr(Vruttamu, type, False)

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
    count_paadam= n_paadam( padyam= padyam, verbose= verbose )

    # 2. Check no.of aksharams (letters)
    count_aksharam= n_aksharam( padyam= padyam, verbose= verbose )

    # paadam-aksharam
    pa_score= []
    for i in count_aksharam:
        pa_score.append( i/ config["n_aksharalu"] )

    # 3. Match gana kramam in each paadam
    match_gana_kramam= check_vruttam_gana_kramam( 
                                                    padyam= padyam, 
                                                    lakshanam_config= config,
                                                    verbose= verbose
                                                )
    
    # 4. Match yati in each paadam
    match_yati= []
    lines= [i.strip() for i in padyam.split("\n")]
    for i in lines:
        yati_value= check_yati( paadam= lines[0], yati_sthanam= config['yati_sthanam'], verbose= verbose )
        match_yati.append( yati_value )

    # 5. Match prasa in each paadam
    match_prasa= check_prasa( padyam= padyam, verbose= verbose )

    # 'weightage_factor' can be modified for more insights
    score["n_paadalu"]= weightage_factor*count_paadam/ config["n_paadalu"]
    score["n_aksharalu"]= weightage_factor*sum(pa_score)/ config["n_paadalu"]
    score["gana_kramam"]= weightage_factor*match_gana_kramam[0]/ match_gana_kramam[1]
    score["yati_sthanam"]= weightage_factor*sum(match_yati)/ config["n_paadalu"]
    score["prasa"]= weightage_factor*max( match_prasa.values() )/ config["n_paadalu"]

    overall_score= sum(score.values())/ len(score)

    if overall_score == 1:
        print("Padyam Detected: ", type.upper())
    
    else:
        print("Padyam not exactly matched with: ", type.upper())

    return {"score": sum(score.values())/ len(score), "per_score": score}
