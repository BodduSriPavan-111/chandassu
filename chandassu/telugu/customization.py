from .padya_bhedam import check_padyam


class Custom:
    """
    Define custom padyam (poem) type
    """
    

    def __init__(self, type, n_paadalu, n_aksharalu, gana_kramam, yati_sthanam, yati_paadalu, prasa, only_generic_yati, true_n_paadalu= -1):

        self.type= type
        self.config= {  
                        "true_n_paadalu": true_n_paadalu,
                        "n_paadalu": n_paadalu,
                        "n_aksharalu": n_aksharalu,
                        "gana_kramam": gana_kramam,
                        "yati_sthanam": yati_sthanam,
                        "yati_paadalu": yati_paadalu,
                        "prasa": prasa,
                        "only_generic_yati": only_generic_yati
                    }
    

    def check_padyam( self, lg_data, weights= None, return_micro_score= True, verbose= False ):
                        # custom_config= {}, 
        """
        ## Evaluates given Laghuvu-Guruvu data with given padyam type with confidence scores.
        Same as 'chandassu.telugu.padya_bhdeam.check_padyam()' function
        """
        
        return check_padyam(
                                lg_data, 
                                type= self.type, 
                                weights= weights,
                                return_micro_score= return_micro_score,  
                                custom_config= self.config,
                                verbose= verbose
                            )