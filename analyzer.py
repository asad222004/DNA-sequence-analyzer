import matplotlib.pyplot as plt

#cleaning the seqeuence to remove any invalid characters
def clean(seqNEW):
    cleanSEQ = ''
    for base in seqNEW:
        if base in ['A', 'G', 'C', 'T']:
            cleanSEQ += base
    return cleanSEQ

# A function which calculates the content of A, G, C and T in a DNA sequence
def AGCTcontent(cleanSEQ):
    A = 0
    T = 0
    G = 0
    C = 0
    for base in cleanSEQ:
        if base =='A':
            A+=1
        elif base =='G':
            G+=1
        elif base =='C':
            C+=1
        elif base =='T':
            T+=1
    return A,G,C,T         

# function to make the graph of AGCT content
def graph_AGCT(A, G, C, T):
    X =['A','G','C','T']
    Y =[A, G, C, T]
    plt.bar(X,Y)
    plt.xlabel("Nucleotides")
    plt.ylabel("Content")
    plt.title("AGCT content Graph")
    plt.grid()
    plt.show()

# function for length of the sequence
def length(cleanSEQ):
    seqLEN = len(cleanSEQ)
    return seqLEN 

# Function for GC ratio calculation
def GCratio( G,C, seqLEN):
    GC_ratio = (( G + C) /seqLEN)*100
    return GC_ratio

# Function to check AT ratio
def ATratio(A,T, seqLEN):
    AT_ratio = ((A+T)/seqLEN)*100
    return AT_ratio

# Function to make the chart of AT and GC ratio
def graph_AT_GC_content(AT_ratio, GC_ratio):
    X = ["ATratio", "GCratio"]
    Y = [AT_ratio, GC_ratio]
    plt.bar(X,Y)
    plt.xlabel("ATratio")
    plt.ylabel("GCratio")
    plt.title("ratios graph")
    plt.grid()
    plt.show()


# Function for making complement
def complt(cleanSEQ):
    complement = ""
    for base in cleanSEQ:
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
def RNA(cleanSEQ):
    RNA = cleanSEQ.replace('T' , 'U')
    return RNA

# Function for reverse complement 
def reverseCOMPLT(cleanSEQ):
    newCOMPLT =cleanSEQ[::-1]    #this reverses the sequence
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

#function to call after entering the sequence
def call_analysis(seq):
    print("---------------------------------\n")
    print("    DNA Sequence Analysis")
    print("---------------------------------\n")
    seqNEW = seq.upper()
    cleanSEQ = clean(seqNEW)
    print(f"The cleaned sequence is:\n=> {cleanSEQ}\n")
    print("------------------------------------------\n")
    #calling to different functions to perform the analysis and print the results
    seqLEN = length(cleanSEQ) 
    print(f"The length of the sequence is:\n=> {seqLEN}\n")
    print("------------------------------------------\n")
    A,G,C,T= (AGCTcontent(cleanSEQ))
    print(f"Adenine is => {A}\nGuanine is => {G}\nCytosine is => {C}\nThymine is => {T}\n")
    print("------------------------------------------\n")
    
    print("------------------------------------------\n")



    GC_ratio = GCratio(G,C, seqLEN)
    print(f"The GC ratio is\n=> {GC_ratio}\n")
    print("------------------------------------------\n")
    GC_skew =GCskew(G,C)
    print(f"The GC skew is\n=> {GC_skew}\n")
    print("------------------------------------------\n")
    AT_ratio = ATratio(A,T, seqLEN)
    print(f"The AT ratio is\n=> {AT_ratio}\n")
    
    print("------------------------------------------\n")
    AT_skew = ATskew(A, T)
    print(f"The AT skew is\n=> {AT_skew}\n")
    print("-------------------------------------------\n")
   
    print("------------------------------------------\n")
    complement=complt(cleanSEQ)
    print(f"The complement strand is\n=>{complement}\n")
    print("------------------------------------------\n")
    reverseComplement = reverseCOMPLT(cleanSEQ)
    print(f"The reverse complement is:\n=>{reverseComplement}\n")
    print("------------------------------------------\n")
    RNAseq = RNA(cleanSEQ)
    print(f"Its RNA strand is:\n=>{RNAseq}\n")
    print("------------------------------------------\n")
    graph_AT_GC_content(AT_ratio, GC_ratio)
    graph_AGCT(A,G,C,T)