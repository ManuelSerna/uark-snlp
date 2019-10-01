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
import json

#================================================
# Disambiguate word senses using word pairs (word1, word2)
# Return probabilities for each word in the pair.
#================================================
def wsd(word1, word2):
    # Preprocess text--remove punctuation, 
    file_name = 'amazon_reviews.txt'
    text = open(file_name, 'r')
    raw_text = text.read()
    text.close()
    #formatted_text = raw_text.lower().replace('&quot', '').translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans('', '', string.digits))
    formatted_text = raw_text.lower().replace('&quot', '').translate(str.maketrans('', '', string.punctuation))
    words = formatted_text.split() # list of all words from text
    
    '''
    Create dictionary to hold context windows for each word in the pair.
        - These context windows are entire strings.
    '''
    c_windows = {}
    c_windows[word1] = []
    c_windows[word2] = []
    
    '''
    Store counts for each word appearing in each context window from the above list. 
    Indices under each key will correspond to the same context window.
    '''
    c_word_counts = {}
    c_word_counts[word1] = []
    c_word_counts[word2] = []
    
    '''
    Dictionaries that store frequencies of each "sense"
    '''
    senses = {}
    senses[word1] = 0
    senses[word2] = 0
    
    # Create pseudoword
    pseudoword = word1+word2

    '''
    Get context windows (+/- 10 words) if any words in a word pair are found.
    '''
    for i in range(len(words)-1):
        if words[i] == word1:
            # Get context window c
            c = words[i-10:i+10]
            
            # Count how many times each word in each context window appears
            
            '''
            counts = {}
            for i in range(len(c)):
                if c[i] not in counts:
                    counts[i] = 1
                else:
                    counts[i] += 1
            '''
            
            # Replace word with pseudoword (og word remains as key in dict)
            c[10] = pseudoword
            c = ' '.join(c)
            c_windows[word1].append(c)
            
            # Increase count
            senses[word1] += 1
        
        if words[i] == word2:
            # Get context window c
            c = words[i-10:i+10]
            
            # Count how many times each word in c appears
            '''
            counts = {}
            for i in range(len(c)):
                if c[i] not in counts:
                    counts[i] = 1
                else:
                    counts[i] += 1
            '''
            
            # Replace word with pseudoword (og word remains as key in dict)
            c[10] = pseudoword
            c = ' '.join(c)
            c_windows[word2].append(c)
            
            # Increase count
            senses[word2] += 1
    
    # output context windows to better visualize data
    with open("c_windows.json", 'w') as file:
        file.write(json.dumps(c_windows, indent=4))
    # output context window word counts dict
    with open("c_word_counts.json", 'w') as file:
        file.write(json.dumps(c_word_counts, indent=4))
    

# Call method and take in words as arguments
wsd(sys.argv[1], sys.argv[2])
