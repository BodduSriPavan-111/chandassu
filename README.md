![plot](https://drive.google.com/uc?id=1izDz9LpCTmCMPUwNM7WMy4hTDNXgzrHF)

# chandassu
Open-source python library implementing Telugu Chandassu.


## Usage
Install using 
```py
pip install chandassu
```

```py
from chandassu.laghuvu_guruvu import LaghuvuGuruvu
from chandassu.padya_bhedam import check_padyam

data= """తొండము నేక దంతమును తోరపు బొజ్జయు వామ హస్తమున్
మెండుగ మ్రోయు గజ్జెలును మెల్లని చూపులు మందహాసమున్
కొండొక గుజ్జు రూపమున కోరిన విద్యలకెల్ల నొజ్జవై
యుండెడి పార్వతీ తనయ యోయి గణాధిప నీకు మ్రొక్కెదన్"""

# Generate LaghuvuGuruvu Sequence
lg_data= LaghuvuGuruvu(data= data).generate()

score= check_padyam( 
                        lg_data= lg_data ,
                        type= "vutpalamaala",
                        return_micro_score= True, 
                        verbose= False
                    )

print(scores)
```

## Notebooks:
1. web_scrapping.ipynb: Scraper scripts to collect data from andhrabharati.com
2. Data_Analysis.ipynb: Analyzes data using different visualizations
3. Chandassu_Generation.ipynb: Generates chandassu for the scraped data
4. Score_Generation.ipynb: Computes scores by after chandassu generation
5. Accuracy_Evaluation.ipynb: Benchmarking and accuracy (Chandassu Score) evaluation

## Acknowledgements
Special thanks to Sesha Sai Vadapalli and Kalepu Nagabhushana Rao, maintainers of andhrabharati.com.

## Citation
Goes here
