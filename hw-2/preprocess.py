#************************************************
'''
SNLP Homework 2
Manuel Serna-Aguilera

Preprocess given corpus (before disambiguating word pairs).
Read each line and extract a 10-word window around the first instance of a target word in a sentence.
(Replace target words with pseudowords).

80% of the lines will be used for training.
20% of the lines will be used for testing.
'''
#************************************************

import string

# Take in each line from file as its own element in the list
raw_lines = [line.rstrip('\n') for line in open("amazon_reviews.txt")]

# Lower-case everything
for i in range(len(raw_lines)):
    #raw_lines[i] = raw_lines[i].replace('&quot', '').translate(str.maketrans('', '', string.punctuation)).lower()
    raw_lines[i] = raw_lines[i].replace('&quot', '').lower()

