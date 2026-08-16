#cleaning the seqeuence to remove any invalid characters
def clean(seqNEW):
    cleaned_seq = ''
    for base in seqNEW:
        if base in ['A', 'G', 'C', 'T']:
            cleaned_seq += base
    return cleaned_seq

# A function which calculates the content of A, G, C and T in a DNA sequence
def AGCTcontent(seqNEW):
    A = 0
    T = 0
    G = 0
    C = 0
    for base in seqNEW:
        if base =='A':
            A+=1
        elif base =='G':
            G+=1
        elif base =='C':
            C+=1
        elif base =='T':
            T+=1
    return A,G,C,T         

# function for length of the sequence
def length(seqNEW):
    seqLEN = len(seqNEW)
    return seqLEN 

# Function for GC ratio calculation
def GCratio( G,C, seqLEN):
    GCratio = (( G + C) /seqLEN)*100
    return GCratio

# Function to check AT ratio
def ATratio(A,T, seqLEN):
    ATratio = ((A+T)/seqLEN)*100
    return ATratio

# Function for making complement
def complt(seqNEW):
    complement = ""
    for base in seqNEW:
        if base=='A':
            complement +='T'
        elif base == 'G':
            complement+='C'
        elif base =='T':
            complement+='A'
        elif base =='C':
            complement+='G'
    return complement

# function for converting to RNA
def RNA(seqNEW):
    RNA = seqNEW.replace('T' , 'U')
    return RNA

# Function for reverse complement 
def reverseCOMPLT(seqNEW):
    newCOMPLT =seqNEW[::-1]    #this reverses the sequence
    reverseComplement= ""
    for base in newCOMPLT:
        if base=='A':
            reverseComplement +='T'
        elif base == 'G':
            reverseComplement+='C'
        elif base =='T':
            reverseComplement+='A'
        elif base =='C':
            reverseComplement+='G'       
    return reverseComplement

# Function for GC skew calculation
def GCskew(G,C):
    if G + C == 0:
        return 0
    return (G-C)/(G+C)

# Function for AT skew calculation
def ATskew(A,T):
    if A + T == 0:
        return 0
    return (A-T)/(A+T)
