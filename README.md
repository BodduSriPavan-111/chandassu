![plot](https://drive.google.com/uc?id=1izDz9LpCTmCMPUwNM7WMy4hTDNXgzrHF)

# chandassu
Open-source python library implementing Telugu Chandassu.

# Benchmarks
Our proposed algorithm achieved SOTA Chandassu Score of **91.22%**.

#### Usage
Install package using
```py
pip install chandassu
```

Check padyam
```py
from chandassu.laghuvu_guruvu import LaghuvuGuruvu
from chandassu.padya_bhedam import check_padyam

data= """తొండము నేక దంతమును తోరపు బొజ్జయు వామ హస్తమున్
మెండుగ మ్రోయు గజ్జెలును మెల్లని చూపులు మందహాసమున్
కొండొక గుజ్జు రూపమున కోరిన విద్యలకెల్ల నొజ్జవై
యుండెడి పార్వతీ తనయ యోయి గణాధిప నీకు మ్రొక్కెదన్"""

lg_data= LaghuvuGuruvu( data= data ).generate()

output= check_padyam( 
                        lg_data= lg_data ,
                        type= "vutpalamaala",
                        return_micro_score= True, 
                        verbose= True
                    )
```
