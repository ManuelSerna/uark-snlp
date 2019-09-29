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

import sys
import string

#================================================
# Disambiguate word senses using word pairs (word1, word2)
# Return probabilities for each word in the pair.
#================================================
def wsd(word1, word2):
    # Preprocess text--remove punctuation, 
    file_name = 'amazon_reviews.txt'
    text = open(file_name, 'r')
    raw_text = text.read()
    #formatted_text = raw_text.lower().replace('&quot', '').translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans('', '', string.digits))
    formatted_text = raw_text.lower().replace('&quot', '').translate(str.maketrans('', '', string.punctuation))
    words = formatted_text.split() # list of all words from text
    
    # Create dictionary to hold context windows for each word in the pair.
    # These context windows are entire strings.
    instances = {}
    instances[word1] = []
    instances[word2] = []
    
    # Get total counts for the individual words
    word_counts = {}
    word_counts[word1] = 0
    word_counts[word2] = 0
    
    # Create pseudoword
    pseudoword = word1+word2

    # Get context windows (+/- 10 words) if any words in a word pair are found.
    for i in range(len(words)-1):
        if words[i] == word1:
            instance = words[i-10:i+10]
            
            # Replace word with pseudoword (og word remains as key in dict)
            instance[10] = pseudoword
            instances[word1].append(' '.join(instance))
            
            # Increase count
            word_counts[word1] += 1
        
        if words[i] == word2:
            instance = words[i-10:i+10]
            
            # Replace word with pseudoword (og word remains as key in dict)
            instance[10] = pseudoword
            instances[word2].append(' '.join(instance))
            
            # Increase count
            word_counts[word2] += 1
    
    print(word_counts)


# Call method and take in words as arguments
wsd(sys.argv[1], sys.argv[2])
