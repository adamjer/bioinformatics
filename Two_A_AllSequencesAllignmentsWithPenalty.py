from Bio import pairwise2
from Bio.pairwise2 import format_alignment

print("<<<<< Start of global allignments >>>>>")

alignments = pairwise2.align.globalms("AXXXBXCD", "ABCD", 2, -1, -4, -3)

for element in alignments:
    print(format_alignment(*element))

print("<<<<< End of global allignments >>>>>")
print("<<<<< Start of local allignments >>>>>")

localAlignments = pairwise2.align.localxs("ACBACCB", "AB",-1, -1)
#for element in localAlignments:
#    print(format_alignment(*element))

print("<<<<< End of local allignments >>>>>")

from math import log
def gap_function(x, y):  # x is gap position in seq, y is gap length
     if y == 0:  # No gap
         return 0
     elif y == 1:  # Gap open penalty
         return -2
     return - (2 + y/4.0 + log(y)/2.0)

alignment = pairwise2.align.globalmc("ACCCCCGT", "ACG", 5, -4, gap_function, gap_function)
for element in alignment:
    print(format_alignment(*element))