# main.py file
# accept the sequence
from analyzer import  length
from analyzer import  AGCTcontent
from analyzer import  GCratio
from analyzer import  ATratio
from analyzer import  complt
from analyzer import  reverseCOMPLT
from analyzer import  RNA
seq = input("enter your DNA sequence here: ")
seqNEW = seq.upper()

Bases = ['A','G','C','T']
valid = False
for base in seqNEW:
    if base in Bases:
        valid = True
if valid == True:
    seqLEN = length(seqNEW) 
    print(f"The length of the sequence is: {seqLEN}")
    A,G,C,T= (AGCTcontent(seqNEW))
    print(f"Adenine is: {A}\nGuanine is: {G}\nCytosine is: {C}\nThymine is: {T}")
    GCratio = GCratio(G,C, seqLEN)
    print(f"The GC ratio is: {GCratio}")
    ATratio=ATratio(A, T, seqLEN)
    print(f"The ATratio is :{ATratio}")
    complement=complt(seqNEW)
    print(f"The complement strand is:\n{complement}")
    reverseComplement = reverseCOMPLT(seqNEW)
    print(f"The reverse complement is:\n{reverseComplement}")
    RNA = RNA(seqNEW)
    print(f"Its RNA strand is:\n{RNA}")

else:
    print("Invalid DNA sequence. Please enter a valid sequence containing only A, G, C, and T.")