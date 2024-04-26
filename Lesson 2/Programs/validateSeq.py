Nucleotides = ["A", "C", "G", "T"]

# Check the Sequence to make sure it is a DNA String
def validateSeq(dna_seq):
  tmpseq = dna.seq.upper()
  for nuc in tmpseq:
    if nuc not in Nucleotides:
      return False
  return tmpseq
