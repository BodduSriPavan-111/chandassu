"""
Module: padyam_config.py
Description: Contains pre-defined configurations for each type of Padyam.
Author: Boddu Sri Pavan
License: MIT
"""

from .ganam import *

class Jaathi:
    """
    ## Configurations for 'Jaathi' class of padyams.
    
    ## Attributes (Type of Padyam)
    ------------------------------
    1. kandamu: కందము
    """

    kandamu= {
                "n_paadalu": 4,
                "gana_kramam": ( ( kandam_odd, kandam_all, kandam_odd ),
                                 ( kandam_all, kandam_odd, kandam_6, kandam_odd, kandam_2_4_last ),
                                 ( kandam_odd, kandam_all, kandam_odd ),
                                 ( kandam_all, kandam_odd, kandam_6, kandam_odd, kandam_2_4_last )
                                ),
                # Here (x,y)= x is the ganam number in human notation, and y is the computer index (can be '0' zero)
                "yati_sthanam": (4, 0),   ### Logic update for configuration
                
                # Here, paadam numbers are in human notation 
                # Therefore in the Yati calculation, to get computer index, '1' will be subtracted
                "yati_paadalu": (2,4),
                "prasa": True,
                "only_generic_yati": True
            }

class VupaJaathi:
    """
    ## Configurations for 'VupaJaathi' class of padyams.
    
    ## Attributes (Type of Padyam)
    ------------------------------
    1. aataveladi: ఆటవెలది 
    2. teytageethi: తేటగీతి 
    3. seesamu: సీసము
    """
    
    aataveladi= {
                    "n_paadalu": 4,
                    "gana_kramam": ( ( surya_ganam, surya_ganam, surya_ganam, indra_ganam, indra_ganam ),
                                     ( surya_ganam, surya_ganam, surya_ganam, surya_ganam, surya_ganam ),
                                     ( surya_ganam, surya_ganam, surya_ganam, indra_ganam, indra_ganam ),
                                     ( surya_ganam, surya_ganam, surya_ganam, surya_ganam, surya_ganam )
                                    ),

                    "yati_sthanam": (4,0), # 1
                    "yati_paadalu": (1,2,3,4),
                    "only_generic_yati": False
                }

    teytageethi= {
                    "n_paadalu": 4,
                    "gana_kramam": ( ( surya_ganam, indra_ganam, indra_ganam, surya_ganam, surya_ganam ),
                                     ( surya_ganam, indra_ganam, indra_ganam, surya_ganam, surya_ganam ),
                                     ( surya_ganam, indra_ganam, indra_ganam, surya_ganam, surya_ganam ),
                                     ( surya_ganam, indra_ganam, indra_ganam, surya_ganam, surya_ganam )
                                    ),
                    "yati_sthanam": (4, 0), # 1
                    "yati_paadalu": (1,2,3,4),
                    "only_generic_yati": False
                 }
    
    seesamu= {
                "true_n_paadalu": 4,
                "n_paadalu": 8,
                "gana_kramam": (
                                    ( indra_ganam, indra_ganam, indra_ganam, indra_ganam ),
                                    ( indra_ganam, indra_ganam, surya_ganam, surya_ganam ),

                                    ( indra_ganam, indra_ganam, indra_ganam, indra_ganam ),
                                    ( indra_ganam, indra_ganam, surya_ganam, surya_ganam ),

                                    ( indra_ganam, indra_ganam, indra_ganam, indra_ganam ),
                                    ( indra_ganam, indra_ganam, surya_ganam, surya_ganam ),

                                    ( indra_ganam, indra_ganam, indra_ganam, indra_ganam ),
                                    ( indra_ganam, indra_ganam, surya_ganam, surya_ganam ),
                                ),

                "yati_sthanam": (3, 0), # 1
                "yati_paadalu": (1,2,3,4,5,6,7,8),
                "only_generic_yati": False
                # PRasa is optional
                # Therefore ignored here (for score calculation)
            }

class Vruttamu:
    """
    ## Configurations for 'Vruttamu' class of padyams.
    
    ## Attributes (Type of Padyam)
    ------------------------------
    1. vutpalamaala: ఉత్పలమాల 
    2. champakamaala: చంపకమాల
    3. saardulamu: శార్దూలము
    4. mattebhamu: మత్తేభము
    """
    
    vutpalamaala= {
                    "n_paadalu": 4,
                    "n_aksharalu": 20,
                    "gana_kramam": ( (bha_ganam, ra_ganam, na_ganam, bha_ganam, bha_ganam, ra_ganam, va_ganam),
                                     (bha_ganam, ra_ganam, na_ganam, bha_ganam, bha_ganam, ra_ganam, va_ganam),
                                     (bha_ganam, ra_ganam, na_ganam, bha_ganam, bha_ganam, ra_ganam, va_ganam),
                                     (bha_ganam, ra_ganam, na_ganam, bha_ganam, bha_ganam, ra_ganam, va_ganam),
                                    ),

                    # Here (x,y)= x is the ganam number in human notation, and y is the computer index (can be '0' zero)
                    "yati_sthanam": (4,0), # Each ganam contains 3 aksharaas. 3X3 + 1= 10 
                    "yati_paadalu": (1,2,3,4),
                    "prasa": True,
                    "only_generic_yati": True
                }

    champakamaala= {
                    "n_paadalu": 4,
                    "n_aksharalu": 21,
                    "gana_kramam": ( (na_ganam, ja_ganam, bha_ganam, ja_ganam, ja_ganam, ja_ganam, ra_ganam),
                                     (na_ganam, ja_ganam, bha_ganam, ja_ganam, ja_ganam, ja_ganam, ra_ganam),
                                     (na_ganam, ja_ganam, bha_ganam, ja_ganam, ja_ganam, ja_ganam, ra_ganam),
                                     (na_ganam, ja_ganam, bha_ganam, ja_ganam, ja_ganam, ja_ganam, ra_ganam)
                                    ),
                    
                    # Here (x,y)= x is the ganam number in human notation, and y is the computer index (can be '0' zero)
                    "yati_sthanam": (4, 1), # 11 = 3X3 + 2+1
                    "yati_paadalu": (1,2,3,4),
                    "prasa": True,
                    "only_generic_yati": True
                }


    saardulamu= {
                    "n_paadalu": 4,
                    "n_aksharalu": 19,
                    "gana_kramam": ( (ma_ganam, sa_ganam, ja_ganam, sa_ganam, ta_ganam, ta_ganam, ga_ganam),
                                     (ma_ganam, sa_ganam, ja_ganam, sa_ganam, ta_ganam, ta_ganam, ga_ganam),
                                     (ma_ganam, sa_ganam, ja_ganam, sa_ganam, ta_ganam, ta_ganam, ga_ganam),
                                     (ma_ganam, sa_ganam, ja_ganam, sa_ganam, ta_ganam, ta_ganam, ga_ganam)
                                    ),

                    # Here (x,y)= x is the ganam number in human notation, and y is the computer index (can be '0' zero)
                    "yati_sthanam": (5, 0), #13,
                    "yati_paadalu": (1,2,3,4),
                    "prasa": True,
                    "only_generic_yati": True
                }

    mattebhamu= {
                    "n_paadalu": 4,
                    "n_aksharalu": 20,
                    "gana_kramam": ( (sa_ganam, bha_ganam, ra_ganam, na_ganam, ma_ganam, ya_ganam, va_ganam),
                                     (sa_ganam, bha_ganam, ra_ganam, na_ganam, ma_ganam, ya_ganam, va_ganam),
                                     (sa_ganam, bha_ganam, ra_ganam, na_ganam, ma_ganam, ya_ganam, va_ganam),
                                     (sa_ganam, bha_ganam, ra_ganam, na_ganam, ma_ganam, ya_ganam, va_ganam)
                                    ),
                    
                    # Here (x,y)= x is the ganam number in human notation, and y is the computer index (can be '0' zero)
                    "yati_sthanam": (5, 1), #14,
                    "yati_paadalu": (1,2,3,4),
                    "prasa": True,
                    "only_generic_yati": True
                }

    # Future Implementation
    # mattakokila= {
    #                 "n_paadalu": 4,
    #                 "n_aksharalu": 18,
    #                 "gana_kramam": ('ర', 'స', 'జ', 'జ', 'భ', 'ర'),
    #                 "yati_sthanam": 11,
    #                 "prasa": True
    #             }