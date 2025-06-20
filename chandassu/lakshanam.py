from .laghuvu_guruvu import LaghuvuGuruvu

def n_paadam( padyam ):

    return len(padyam.split("\n"))

def n_aksharam( padyam ):

    # n_letters= []
    # for i in p.split("\n"):
    #     lg= LaghuvuGuruvu( data= i.strip() )
    #     n_letters.append( len(lg.split_by_letter()) )
    # return n_letters

    return [ len(LaghuvuGuruvu(data= i.strip()).split_by_letter()) for i in padyam.split("\n")]