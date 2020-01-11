#************************************************
'''
    SNLP Homework 3
    Manuel Serna-Aguilera
    
    Purpose: Predict the next 8 words given a starting bigram with the Shannon Visualization Game.
'''
#************************************************

import collections
import json
import math
import random
import string
import sys

# Get bigram from command line
bigram = sys.argv[1]

'''
Extract normalized bigram json as a dict.
'''
file_name = "normal.json"
text = open(file_name, 'r')
text_str = text.read()
normal = json.loads(text_str)
text.close()

normal = sorted(normal.items(), key=lambda kv: kv[1], reverse=True)
normal = collections.OrderedDict(normal)

'''
Get top 15 overall bigrams from sorted dict.
'''
top15 = list(normal.keys())[:15]

'''
Given a bigram, get 8 more random words
'''
latest_word = (bigram.split())[1]
sentence = bigram # start sentence with the given bigram
c = 1 # count up to 8

while c <= 8:
    p = [] # start with empty list
    
    # Get all bigrams with the last word in the current bigram, then pick a random word to add to the sequence
    for i in normal:
        j = i.split()
        if j[0] == latest_word:
            p.append(i)
    if len(p) != 0:
        selected = random.choice(p)
    else:
        selected = random.choice(top15)
    sentence += ' ' + selected.split()[1]
    latest_word = selected.split()[1] # pick next random word based on currently chosen random word
    c += 1

print(sentence)
