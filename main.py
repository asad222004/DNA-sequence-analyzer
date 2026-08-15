# main.py file
# accept the DNA sequence from the user and call the functions from analyzer.py to perform the analysis
from analyzer import  length
from analyzer import  AGCTcontent
from analyzer import  GCratio
from analyzer import  ATratio
from analyzer import  complt
from analyzer import  reverseCOMPLT
from analyzer import  RNA
from analyzer import  GCskew
from analyzer import  ATskew

seq = input("enter your DNA sequence here:\n ") 
# accept the DNA sequence from the user

seqNEW = seq.upper()
 # changes the sequence to uppercase to avoid errors in the analysis

Bases = ['A','G','C','T']
valid = False 

# flag to check if the sequence is valid
for base in seqNEW:
    if base in Bases:
        valid = True
if valid == True:
    seqLEN = length(seqNEW) 

    print("---------------------------------\n")
    print("    DNA Sequence Analysis")
    print("---------------------------------\n")
    #calling to different functions to perform the analysis and print the results
    print(f"The length of the sequence is:\n=> {seqLEN}\n")
    print("------------------------------------------\n")
    A,G,C,T= (AGCTcontent(seqNEW))
    print(f"Adenine is => {A}\nGuanine is => {G}\nCytosine is => {C}\nThymine is => {T}\n")
    print("------------------------------------------\n")
    GCratio = GCratio(G,C, seqLEN)
    print(f"The GC ratio is\n=> {GCratio}\n")
    print("------------------------------------------\n")
    GCskew =GCskew(G,C)
    print(f"The GC skew is\n=> {GCskew}\n")
    print("------------------------------------------\n")
    ATratio = ATratio(A,T, seqLEN)
    print(f"The AT ratio is\n=> {ATratio}\n")
    print("------------------------------------------\n")
    ATskew = ATskew(A, T)
    print(f"The AT skew is\n=> {ATskew}\n")
    print("------------------------------------------\n")
    complement=complt(seqNEW)
    print(f"The complement strand is\n=>{complement}\n")
    print("------------------------------------------\n")
    reverseComplement = reverseCOMPLT(seqNEW)
    print(f"The reverse complement is:\n=>{reverseComplement}\n")
    print("------------------------------------------\n")
    RNA = RNA(seqNEW)
    print(f"Its RNA strand is:\n=>{RNA}\n")
    print("------------------------------------------\n")

else:
    print("Invalid DNA sequence. Please enter a valid sequence containing only A, G, C, and T.")