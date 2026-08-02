from .padyam_config import *
from .ganam import *

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch


def padyam_plot( 
                    gana_kramam,
                    figsize= (6, 6),
                    yati_sthanam= (4, 0),
                    yati_paadaalu= (1,2,3,4),
                    only_generic_yati= True,
                    prasa= True,
                    include_indra_surya= False,
                    title= "Aataveladi",
                    legend= True
):

    fig, ax = plt.subplots( figsize= figsize )

    patches= []

    # Find maximum length of AksharamTokens for each paadam
    max_each_paadam= [ max( [ len(list(i.values())[0]) for i in gana_kramam[j] ] )    for j in range(len(gana_kramam)) ]

    y_tick_index= []

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


                hatch= ""
                condition_1= (k+1 in yati_paadaalu and ((i==0 and j==0 ) or (i== yati_sthanam[0] - 1 and j== yati_sthanam[1])))
                condition_2= (i==0 and j==1 and prasa== True)
                condition_3= only_generic_yati== False

                if condition_3 and condition_1:
                    hatch= "///"
                elif condition_1:
                    hatch= "---"
                
                if condition_2:
                    hatch= "|||"

                if condition_1 and condition_2:
                    hatch= "-|-|-|"
                
                # j is the vertical shift for each Aksharam Token within each paadam
                # sum(max_each_paadam) + len(gana_kramam) -1 -  sum(max_each_paadam[:(k+1)]) - k is shift for each paadam
            
                temp= Rectangle( 
                                    (i, sum(max_each_paadam) + len(gana_kramam) -1 -  sum(max_each_paadam[:(k+1)]) - k +j ),   
                                    width= 1, 
                                    height= 1, 
                                    facecolor=color,
                                    edgecolor= "black",
                                    linewidth= linewidth,
                                    linestyle= linestyle,
                                    hatch= hatch
                                )

                patches.append( temp )

                count+= 1

        y_tick_index.append( sum(max_each_paadam) + len(gana_kramam) -1 -  sum(max_each_paadam[:(k+1)]) - k + max_each_paadam[k]/2 )

    for each_patch in patches:
        ax.add_patch( each_patch )

    ax.relim()
    ax.autoscale_view()

    plt.title( "PadyamPlot: "+ title)

    if legend:

        legend_elements = [
                            Patch( facecolor='white', edgecolor= "black", linewidth= 0.5, label='Laghuvu-|'),
                            Patch(facecolor='palegreen', edgecolor= "black", linewidth= 0.5, label='Guruvu-U'),

                            Patch(facecolor='white', edgecolor= "black", linewidth= 0.5, hatch= "|||", label='Prasa (Laghuvu)'),
                            Patch(facecolor='palegreen', edgecolor= "black", linewidth= 0.5, hatch= "|||", label='Prasa (Guruvu)'),

                            Patch(facecolor='white', edgecolor= "black", linewidth= 0.5, hatch= "---", label='Yati (Laghuvu)'),
                            Patch(facecolor='palegreen', edgecolor= "black", linewidth= 0.5, hatch= "---", label='Yati (Guruvu)'),

                            Patch(facecolor='white', edgecolor= "black", linewidth= 0.5, hatch= "///", label='Prasa Yati (Laghuvu)'),
                            Patch(facecolor='palegreen', edgecolor= "black", linewidth= 0.5, hatch= "///", label='Prasa Yati (Guruvu)'),

                            Patch(facecolor='palegreen', edgecolor= "black", linewidth= 1.5, label='Surya Ganam (Guruvu)'),
                            Patch(facecolor='white', edgecolor= "black", linewidth= 1.5, label='Surya Ganam (Laghuvu)')
                        ]

        ax.legend(handles=legend_elements, bbox_to_anchor= (1.005, 1.01), title= "Cell Description")

    max_ganams= max([len(i) for i in gana_kramam])

    plt.xticks( 
                    [i+0.5 for i in range( max_ganams )],
                    [str(i+1) for i in range( max_ganams )]
            )

    plt.yticks(
                    y_tick_index,
                    [str(i+1) for i in range( len(y_tick_index) )]
            )

    plt.xlabel("Ganam")
    plt.ylabel("Paadam")

    return fig, ax