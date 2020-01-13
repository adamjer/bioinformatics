from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo as matlist
import time
import math

def readFromFile(fileName):
    file = open(fileName, "r")
    return file.read()

def gap_function(x, y):  # x is gap position in seq, y is gap length
    if y == 0:  # No gap
         return 0
    elif y == 1:  # Gap open penalty
         return -2
    return - (2 + y/4.0 + math.log(y)/2.0)

sequences = [ readFromFile("100.seq"), readFromFile("1000.seq"), readFromFile("10000.seq"), readFromFile("100000.seq"), readFromFile("1000000.seq") ]
matrix = matlist.blosum62

start = time.time()
alignments = pairwise2.align.globalxx(sequences[2], sequences[0])
print(f"Execution time is { time.time() - start } seconds.")
print(f"Formatted alignmet[0] {format_alignment(*alignments[0])}")

start = time.time()
alignments = pairwise2.align.globalmx(sequences[2], sequences[0], 2, -1)
print(f"Execution time is { time.time() - start } seconds.")
print(f"Formatted alignmet[0] {format_alignment(*alignments[0])}")

start = time.time()
#alignments = pairwise2.align.globaldx("GSDDJDGKL", "ABGHTS", matrix, score_only = True)
print(f"Execution time is { time.time() - start } seconds.")
#print(f"Formatted alignmet[0] {format_alignment(*alignments[0])}")

start = time.time()
alignment = pairwise2.align.globalmc(sequences[1], sequences[0], 5, -4, gap_function, gap_function)
print(f"Execution time is { time.time() - start } seconds.")
print(f"Formatted alignmet[0] {format_alignment(*alignments[0])}")