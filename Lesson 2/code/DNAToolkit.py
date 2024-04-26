# import colllections
Nucleotides = ["A", "C", "G", "T"]

# To generate a random DNA Sequence
import random
def randDNAstr(len):
  randDNAstr = ''.join([random.choice(Nucleotides) for nuc in range(len)])
  return randDNAstr

# Check the Sequence to make sure it is a DNA String
def validateSeq(dna_seq):
  tmpseq = dna.seq.upper()
  for nuc in tmpseq:
    if nuc not in Nucleotides:
      return False
  return tmpseq
# Check the Sequence to count the characters
def countNucFrequency(seq):
  tmpFreqDict = {"A" : 0, "C" : 0, "G" : 0, "T" : 0}
  for nuc in seq:
    tmpfreqDict[nuc] +=1
    return tmpFreqDict

# Instead of writing the function on our own we can use collections from python modules
#return dict(collections.Counter(seq)) -> Here we have passed the seq to the collection which is passed to dictionary that will return a dictionary with the count values of character.
