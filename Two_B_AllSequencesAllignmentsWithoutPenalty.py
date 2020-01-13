from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo as matlist

matrix = matlist.blosum62
alignments = pairwise2.align.globalxx("ACBAB", "AB")


for element in alignments:
    print(format_alignment(*element))