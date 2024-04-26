# To generate a random DNA Sequence

Nucleotides = ["A","G","C","T"]

import random
def randDNAstr(len):
  randDNAstr = ''.join([random.choice(Nucleotides) for nuc in range(len)])
  return randDNAstr
