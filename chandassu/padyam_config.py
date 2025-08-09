"""
Module: padyam_config.py
Description: Contains pre-defined configurations for Padyams.
Author: Boddu Sri Pavan
License: MIT
"""

from .ganam import *

class Jaathi:
    pass

class VupaJaathi:
    
    aataveladi= {
                    "n_paadalu": 4,
                    "gana_kramam": ( ( surya_ganam, surya_ganam, surya_ganam, indra_ganam, indra_ganam ),
                                     ( surya_ganam, surya_ganam, surya_ganam, surya_ganam, surya_ganam ),
                                     ( surya_ganam, surya_ganam, surya_ganam, indra_ganam, indra_ganam ),
                                     ( surya_ganam, surya_ganam, surya_ganam, surya_ganam, surya_ganam )
                                    ),
                    "yati_sthanam": (4,1),
                    "only_generic_yati": False
                }

    teytageethi= {
                    "n_paadalu": 4,
                    "gana_kramam": ( ( surya_ganam, indra_ganam, indra_ganam, surya_ganam, surya_ganam ),
                                     ( surya_ganam, indra_ganam, indra_ganam, surya_ganam, surya_ganam ),
                                     ( surya_ganam, indra_ganam, indra_ganam, surya_ganam, surya_ganam ),
                                     ( surya_ganam, indra_ganam, indra_ganam, surya_ganam, surya_ganam )
                                    ),
                    "yati_sthanam": (4, 1),
                    "only_generic_yati": False
                 }

class Vruttamu:
    
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
                    "prasa": True,
                    "only_generic_yati": True
                }

    # mattakokila= {
    #                 "n_paadalu": 4,
    #                 "n_aksharalu": 18,
    #                 "gana_kramam": ('ర', 'స', 'జ', 'జ', 'భ', 'ర'),
    #                 "yati_sthanam": 11,
    #                 "prasa": True
    #             }