"""
Module: ganam.py
Description: Contains configurations for each "Ganam"
Author: Boddu Sri Pavan
Date: 21-06-2025
License: MIT
"""

# Ganams are divided into 4 types based on the no.of aksharams present.

# No.of aksharams: 1
eka= {
    ("U",): 'గ',
    ("|",): 'ల',
    "U": 'గ',
    "|": 'ల',
}
r_eka= {
    'గ': ("U",),
    'ల': ("|",)
}

# No.of aksharams: 2
dwi= {
    ("|", "|"): 'లా',
    ("|", "U"): 'వ',
    ("U", "|"): 'హ',
    ("U", "U"): 'గా'
}
r_dwi= {
    'లా': ("|", "|"),
    'వ': ("|", "U"),
    'హ': ("U", "|"),
    'గా': ("U", "U")
}


# No.of aksharams: 3
tria= {
    ("|", "|", "|"): 'న',
    ("|", "|", "U"): 'స',
    ("|", "U", "|"): 'జ',
    ("|", "U", "U"): 'య',
    ("U", "|", "|"): 'భ',
    ("U", "|", "U"): 'ర',
    ("U", "U", "|"): 'త',
    ("U", "U", "U"): 'మ'
}
r_tria= {
    'న': ("|", "|", "|"),
    'స': ("|", "|", "U"),
    'జ': ("|", "U", "|"),
    'య': ("|", "U", "U"),
    'భ': ("U", "|", "|"),
    'ర': ("U", "|", "U"),
    'త': ("U", "U", "|"),
    'మ': ("U", "U", "U")
}

# No.of aksharams: 4
chatura= {
    ("|", "|", "|", "|"): 'నల',
    ("|", "|", "|", "U"): 'నగ',
    ("|", "|", "U", "|"): 'సల'
}
r_chatura= {
    'నల': ("|", "|", "|", "|"),
    'నగ': ("|", "|", "|", "U"),
    'సల': ("|", "|", "U", "|")
}

# There are 2 types of gana swarupamulu
# Indra Ganaalu
indra_ganam= [ 'నల', 'నగ', 'సల', 'భ', 'ర', 'త' ]
r_indra_ganam= [("|", "|", "|", "|"), ("|", "|", "|", "U"), ("|", "|", "U", "|"), 
                ("U", "|", "|"), ("U", "|", "U"), ("U", "U", "|")]

# Surya Ganaalu
surya_ganam= [ 'న', 'హ' ]
r_surya_ganam= [("|", "|", "|"), ("U", "|")]