![plot](https://drive.google.com/uc?id=1izDz9LpCTmCMPUwNM7WMy4hTDNXgzrHF)

# Chandassu | తెలుగు చంధస్సు
Python library implementing "Chandassu", metrical poetry in Telugu Language (తెలుగు చంధస్సు).

## Benchmarks
**Performance evaluation across prosodic classes**
![plot](https://drive.google.com/uc?id=1ezFq499XMOb2VRgy_J5XIwbtqkndL3OG)
 
**Performance evaluation across padyam types**
![plot](https://drive.google.com/uc?id=1iwld2P1fQRijTmbYZHRbH7NkVX2GLKP0)

Our algorithm achieves **91.73% accuracy** on the proposed Chandassu Score.

## Usage
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
## Computational Architecture
![plot](https://drive.google.com/uc?id=1uC_zetHMhVozM6PNgW5J0Hd1V5_v_xRC)

- **nidhi.py:** Telugu alphabet classification with phonological categorizations </br>
- **panimuttu.py:** Vowel-consonant operations utility functions </br>
- **laghuvu_guruvu.py:** Prosodic analysis engine with tokenizer and syllabic weight classifier </br>
- **ganam.py:** Pattern repository mapping LaghuvuGuruvu sequences to metrical units </br>
- **padyam_config.py:** Configuration database for padyam type constraints and rules </br>
- **check_lakshanam.py:** Validation module for yati (caesura) and prasa (alliteration) </br>
- **padya_bhedam.py:** Main integration module for metrical assessment and evaluation </br>

## Notebooks:
1. web_scrapping.ipynb: Scraper scripts to collect data from andhrabharati.com
2. Data_Analysis.ipynb: Analyzes data using different visualizations
3. Chandassu_Generation.ipynb: Generates chandassu for the scraped data
4. Score_Generation.ipynb: Computes scores by after chandassu generation
5. Accuracy_Evaluation.ipynb: Benchmarking and accuracy (Chandassu Score) evaluation

## Eager to Contribute?
Any data, features, refactoring or **your innovative thought**, please check <a href= "https://github.com/BodduSriPavan-111/chandassu/blob/main/CONTRIBUTING.md">here</a>.


## Acknowledgements
Special thanks to Sesha Sai Vadapalli and Kalepu Nagabhushana Rao, maintainers of [andhrabharati.com.](https://andhrabharati.com/). </br>
Appana Mohan Naga Phani Kumar for proofreading our article. </br>
Sincere gratitude to our parents and family members for their continuous support throughout this work. </br>
This work was undertaken with the grace of Sri Ramalinga Chowdeswari Devi.

## Citation
Goes here

## Thank You !
