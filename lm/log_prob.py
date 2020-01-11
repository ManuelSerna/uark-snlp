#************************************************
'''
    SNLP Homework 3
    Manuel Serna-Aguilera
    
    Purpose: Calculate and output the log probability p of a given sentence.
'''
#************************************************

import collections
import json
import math
import string
import sys

# Get sentence from command line, split into list of words
raw = sys.argv[1]
words = raw.split()

'''
Extract normalized bigram json as a dict.
'''
file_name = "normal.json"
text = open(file_name, 'r')
text_str = text.read()
normal = json.loads(text_str)
text.close()

# Get total count of unigrams
file_name = "unigrams.json"
text = open(file_name, 'r')
text_str = text.read()
unigrams = json.loads(text_str)
text.close()
unigram_tot = 0
for u in unigrams:
    unigram_tot += unigrams[u]

# Calculate the log probability of a given sentence
base = 10 # math.log(100, base)
p = 0
for w in range(len(words)-1):
    bigram = words[w] + ' ' + words[w+1]
    if bigram in normal:
        p += math.log(normal[bigram], base)
    else:
        p += (math.log(1/unigram_tot, base)-1)

# Output log prob (undo log using base ** x)
print('\tLog probability: ', 10 ** p)
