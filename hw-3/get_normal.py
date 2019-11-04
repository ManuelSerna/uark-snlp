#************************************************
'''
    SNLP Homework 3
    Manuel Serna-Aguilera
    
    Purpose: Calculate bigram probabilities using unigram and bigram counts.
'''
#************************************************

import collections
import json
import string

#------------------------------------------------
# Preprocess Shakespeare text.
#------------------------------------------------
file_name = 's.txt'
file_content = open(file_name, 'r')
text = file_content.read()
file_content.close()
formatted_text = text.lower().replace('&quot', '').translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans('', '', string.digits))
words = formatted_text.split()

#------------------------------------------------
'''
    Insert all i) unigrams and ii) bigrams into hashtables to count their frequencies.
'''
#------------------------------------------------
# Insert UNIGRAMS (key=unigram, value=frequency)
unigrams = {}
for w in words:
    try:
        unigrams[w] += 1
    except KeyError:
        unigrams[w] = 1

with open("unigrams.json", 'w') as file:
    file.write(json.dumps(unigrams, indent=4))

# Insert BIGRAMS (key=bigram, value=frequency)
bigrams = {}
for i in range(len(words)-1):
    bigram = words[i] + ' ' + words[i+1]
    try:
        bigrams[bigram] += 1
    except KeyError:
        bigrams[bigram] = 1

with open("bigrams.json", 'w') as file:
    file.write(json.dumps(bigrams, indent=4))

#------------------------------------------------
'''
    Normalize bigram counts by their unigram counts, store in a dict called "normal".

    Given bigram b = w1 + w2
    Max likelihood estimation m = freq(b)/freq(w1)
'''
#------------------------------------------------

normal = {}
for i in bigrams:
    bigram_str = i.split()    
    normal[i] = bigrams[i]/unigrams[bigram_str[0]]

with open("normal.json", 'w') as file:
    file.write(json.dumps(normal, indent=4))
