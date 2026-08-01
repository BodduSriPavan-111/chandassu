from .padyam_config import *
from .ganam import *

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def padyam_plot( 
                    gana_kramam,
                    figsize= (6, 6),
                    yati_sthanam= (4, 0),
                    prasa= True,
                    include_indra_surya= False



):

    fig, ax = plt.subplots( figsize= figsize )

    patches= []

    # Find maximum length of AksharamTokens for each paadam
    max_each_paadam= [ max( [ len(list(i.values())[0]) for i in gana_kramam[j] ] )    for j in range(len(gana_kramam)) ]

    for k in range(len(gana_kramam)):

        each_paadam= gana_kramam[k]

        sequence= [ list(i.values())[0] for i in each_paadam]
        # print( sequence )

        count= 1

        for i in range(len(sequence)):

            each_ganam= sequence[i]

            linewidth= 1
            linestyle= "-"

            if include_indra_surya:

                if each_ganam in r_surya_ganam:
                    linewidth= 3

                if each_ganam in r_indra_ganam:
                    linestyle= "--"

            for j in range(len(each_ganam)):

                lg= each_ganam[j]
                
                color= "palegreen" if lg == 'U' else "white"

                # j is the vertical shift for each Aksharam Token within each paadam
                # len(gana_kramam) - k is the shift for each paadam

                temp= Rectangle( 
                                    (i, sum(max_each_paadam) + len(gana_kramam) -1 -  sum(max_each_paadam[:(k+1)]) - k +j ),   
                                    width= 1, 
                                    height= 1, 
                                    facecolor=color,
                                    edgecolor= "black",
                                    linewidth= linewidth,
                                    linestyle= linestyle,
                                    hatch= "---" if ((i==0 and j==0 ) or (i== yati_sthanam[0] - 1 and j== yati_sthanam[1])) else "|||" if (i==0 and j==1 and prasa== True) else ""
                                )

                patches.append( temp )

                count+= 1

    for each_patch in patches:
        ax.add_patch( each_patch )

    ax.relim()
    ax.autoscale_view()

    return fig, ax