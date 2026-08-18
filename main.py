# main.py file
# accept the DNA sequence from the user and call the functions from analyzer.py to perform the analysis

from analyzer import  call_analysis
seq = input("enter your DNA sequence here:\n ") 

call_analysis(seq)