def countNucFrequency(seq):
  tmpFreqDict = {"A" : 0, "C" : 0, "G" : 0, "T" : 0}
  for nuc in seq:
    tmpfreqDict[nuc] +=1
    return tmpFreqDict

# Instead of writing the function on our own we can use collections from python modules
# import colllections
#return dict(collections.Counter(seq)) -> Here we have passed the seq to the collection which is passed to dictionary that will return a dictionary with the count values of character.
