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
# Return probabilities for each word "sense" for some pseudoword=word1+word2
#================================================
def wsd(word1, word2):
    # Preprocess text--remove punctuation, html residue, and digits
    file_name = 'amazon_reviews.txt'
    text = open(file_name, 'r')
    raw_text = text.read()
    text.close()
    formatted_text = raw_text.lower().replace('&quot', '').translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans('', '', string.digits))
    
    '''
    Variables
    '''
    words          = formatted_text.split() # all words from text file
    pseudoword     = word1+word2 # pseudoword that could be any of two senses
    r              = 10 # range r for all context windows
    windows        = {} # context windows for each "sense"
    windows[word1] = []
    windows[word2] = []
    
    uniquewc        = {} # counts of unique words across all documents for each sense
    uniquewc[word1] = {}
    uniquewc[word2] = {}
    
    num_vocab = 0 # number of unique words
    nv_helper = {} # helps count unique words (for num_vocab)
    
    '''
    Generate data
    '''
    for w in range(len(words)-1):
        # Get context windows and maintain uniquewc for each "sense"
        if words[w] == word1:
            c = words[w-r:w+r]
            c[10] = pseudoword
            windows[word1].append(c)
            # Update uniquewc for sense 1
            for i in c:
                if i not in uniquewc[word1]:
                    uniquewc[word1][i] = 1
                else:
                    uniquewc[word1][i] += 1
        if words[w] == word2:
            c = words[w-r:w+r]
            c[10] = pseudoword
            windows[word2].append(c)
            # Update uniquewc for sense 2
            for i in c:
                if i not in uniquewc[word2]:
                    uniquewc[word2][i] = 1
                else:
                    uniquewc[word2][i] += 1
        # Maintain encountered words dict
        if words[w] not in nv_helper:
            nv_helper[words[w]] = 1
            num_vocab += 1
    
    # Calculate conditional probabilities of all words given either sense 1 or sense 2
    # p = (xxx+1)/(+num_vocab)
    
    
    
    
    #    #    #print(words[w])
    #    #    uniquew.append(words[w])
    #    #print(words[w])
    #print(uniquew)
    #with open("uniquew.json", 'w') as file:
    #    file.write(json.dumps(uniquew, indent=4))
    with open("uniquewc.json", 'w') as file:
        file.write(json.dumps(uniquewc, indent=4))
    #print(num_vocab)
    '''
    For each word "sense", 
    '''
    #for w in 
    
    '''
    #Create dictionary to hold context windows for each word in the pair.
    #Write to a file so we can check our work.
    c_windows = {}
    c_windows[word1] = []
    c_windows[word2] = []
    
    #Dictionary that stores frequencies of each "sense" and pseudoword.
    pseudoword = word1+word2
    
    senses = {}
    senses[word1] = 0
    senses[word2] = 0
    senses[pseudoword] = 0

    
    #Generate list of documents "documents"
    #    - Store each unique word with its count for each context window c of +/- 10 words. Sense is key.
    #    Note: word sense will always be at index i=10.
    
    #Define num_vocab, counts number of unique words across all context windows.
    
    documents = []
    num_vocab = 0
    
    for i in range(len(words)-1):
        if words[i] == word1:
            c = words[i-10:i+10]
            
            # Count unique words
            d = {}
            for i in range(len(c)):
                if c[i] not in d:
                    d[c[i]] = 1
                else:
                    d[c[i]] += 1
            documents.append(d)
            
            # Create sentence string to later store in file
            c = ' '.join(c)
            c_windows[word1].append(c)
            
            # Add to counts
            senses[word1] += 1
            senses[pseudoword] += 1
        
        # Apply same logic to sense 2
        if words[i] == word2:
            c = words[i-10:i+10]
            d = {}
            for i in range(len(c)):
                if c[i] not in d:
                    d[c[i]] = 1
                else:
                    d[c[i]] += 1
            documents.append(d)
            c = ' '.join(c)
            c_windows[word2].append(c)
            senses[word2] += 1
            senses[pseudoword] += 1
    
    
    #Generate probabilities dictionary "probs" on 80% of the 
    #    - For each unique word, calculate probability of it appearing given one of the two sense. Sense is key, value is P(word(i) | sense).
    
    probs = []
    
    '''
    
    
    #for sense in c_windows:
    
    #print(senses)
    
    #Calculate the probabilities for each unique word in the documents
    
    #P(word_k | sense) = (n_k + 1)/(total_count_in_class + distinct_words) 
    #where
    
    #n_k                  := frequency of word across all documents under a certain sense
    #total_count_in_class := total counts of tat unique word
    #distinct_words       := number of all distinct words across all documents
    
    
    
    #with open("c_windows.json", 'w') as file:
    #    file.write(json.dumps(c_windows, indent=4))
    #with open("documents.json", 'w') as file:
    #    file.write(json.dumps(documents, indent=4))
    
    with open("windows.json", 'w') as file:
        file.write(json.dumps(windows, indent=4))
    

# Call method and take in words as arguments
wsd(sys.argv[1], sys.argv[2])
