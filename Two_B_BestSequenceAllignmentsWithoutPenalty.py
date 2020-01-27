from Bio import pairwise2
from Bio.pairwise2 import format_alignment

alignments = pairwise2.align.globalxx("ACBAB", "AB", score_only = True)
print(alignments)

localAlignments = pairwise2.align.localxx("ACBAB", "AB", score_only = True)
print(localAlignments)