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
    
    teytageethi= {
                    "n_paadalu": 4,
                    "gana_kramam": ( surya_ganam, indra_ganam, indra_ganam, surya_ganam, surya_ganam ),
                    "yati_sthanam": (4, 1),
                 }

class Vruttamu:
    
    vutpalamaala= {
                    "n_paadalu": 4,
                    "n_aksharalu": 20,
                    "gana_kramam": (bha_ganam, ra_ganam, na_ganam, bha_ganam, bha_ganam, ra_ganam, va_ganam),
                    "yati_sthanam": 10,
                    "prasa": True
                }

    champakamaala= {
                    "n_paadalu": 4,
                    "n_aksharalu": 21,
                    "gana_kramam": (na_ganam, ja_ganam, bha_ganam, ja_ganam, ja_ganam, ja_ganam, ra_ganam),
                    "yati_sthanam": 11,
                    "prasa": True
                }

    saardulamu= {
                    "n_paadalu": 4,
                    "n_aksharalu": 19,
                    "gana_kramam": (ma_ganam, sa_ganam, ja_ganam, sa_ganam, ta_ganam, ta_ganam, ga_ganam),
                    "yati_sthanam": 13,
                    "prasa": True
                }

    mattebhamu= {
                    "n_paadalu": 4,
                    "n_aksharalu": 20,
                    "gana_kramam": (sa_ganam, bha_ganam, ra_ganam, na_ganam, ma_ganam, ya_ganam, va_ganam),
                    "yati_sthanam": 14,
                    "prasa": True
                }

    # mattakokila= {
    #                 "n_paadalu": 4,
    #                 "n_aksharalu": 18,
    #                 "gana_kramam": ('ర', 'స', 'జ', 'జ', 'భ', 'ర'),
    #                 "yati_sthanam": 11,
    #                 "prasa": True
    #             }