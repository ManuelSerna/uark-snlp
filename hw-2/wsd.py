#************************************************
# SNLP Homework 2
# Manuel Serna-Aguilera
#
# Disambiguate word sense given a pseudoword (two different words with two different meanings concatenated together)
#************************************************

import sys
import string
import json

#================================================
# Disambiguate word senses using a word pair (word1, word2)
# Print probabilities for each word "sense" for some pseudoword=word1+word2
#================================================
def wsd(word1, word2):
    # Preprocess text--remove punctuation, html residue, and digits
    text = open('amazon_reviews.txt', 'r')
    raw_text = text.read()
    text.close()
    formatted_text = raw_text.lower().replace('&quot', '').translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans('', '', string.digits))
    
    
    #--------------------------------------------
    # Variables
    #--------------------------------------------
    # Adjustable range r for all context windows
    r = 10
    
    words = formatted_text.split() # all words from text file, disregard after getting context windows
    pseudoword = word1+word2 # pseudoword that could mean any of two senses
    
    # All context windows for each sense
    windows = {}
    windows[word1] = []
    windows[word2] = []
    
    # Training data dict
    trainw = {}
    trainw[word1] = []
    trainw[word2] = []
    
    
    # Test context windows
    testw = []
    actual = {} # holds context windows with actual "sense", output to a file for easy verification by the user
    
    # Keep track of each unique word count (wc) across all documents for each sense (need these number to calculate probabilities)
    uniquewc = {} # counts of unique words across all documents for each sense
    uniquewc[word1] = {}
    uniquewc[word2] = {}
    
    # Probability-related
    n1        = 0 # sum of frequencies for all words under sense 1
    n2        = 0 # sum of frequencies for all words under sense 2
    num_vocab = 0 # number of unique words (independent of documents and senses)
    nv_helper = {} # helps count unique words (for num_vocab)
    
    
    #--------------------------------------------
    # Extract context windows
    #--------------------------------------------
    for w in range(len(words)-1):
        if words[w] == word1:
            c = words[w-r:w+r] # get context window c according to some range
            original = c[10] # store original window to calculate accuracy
            c[10] = pseudoword # replace "sense"
            windows[word1].append(c) # store c in a dictionary
            actual[' '.join(c)] = original # store context window with original window for manual verification
        if words[w] == word2:
            c = words[w-r:w+r]
            original = c[10]
            c[10] = pseudoword
            windows[word2].append(c)
            actual[' '.join(c)] = original
    
    
    #--------------------------------------------
    # Extract training (80%) and testing (20%) data for both senses
    # Get number of documents as well
    #--------------------------------------------
    size1 = len(windows[word1])
    trainw[word1] = windows[word1][:int(size1*0.8)] # first 80% of windows
    num_doc1 = len(trainw[word1]) # get number of documents for sense 1
    for l in windows[word1][int(size1*0.8):]: # last 20% of windows
        testw.append(l)
    
    size2 = len(windows[word2])
    trainw[word2] = windows[word2][:int(size2*0.8)]
    num_doc2 = len(trainw[word2])
    for l in windows[word2][int(size2*0.8):]:
        testw.append(l)
    
    tot_docs = num_doc1 + num_doc2 # ge total to calculate probability of either sense P(word(i))
    
    #--------------------------------------------
    # Get data needed to calculate probabilities from training set
    #--------------------------------------------
    for s in trainw: # only 2 senses
        for j in trainw[s]: # n
            for i in j: # 21 elements in n lists
                # Add word counts to either sense 1 or 2
                if s == word1:
                    if i not in uniquewc[word1]:
                        uniquewc[word1][i] = 1
                        n1 += 1
                    else:
                        uniquewc[word1][i] += 1
                        n1 += 1
                if s == word2:
                    if i not in uniquewc[word2]:
                        uniquewc[word2][i] = 1
                        n2 += 1
                    else:
                        uniquewc[word2][i] += 1
                        n2 += 1
                # Maintain encountered words dict
                if i not in nv_helper:
                    nv_helper[i] = 1
                    num_vocab += 1
    
    
    #--------------------------------------------
    '''
    Calculate conditional probabilities of all words given either sense 1 or sense 2.
    Store probabilities in dict pw.
        - key: word
        - value: P(w|sense)
    '''
    #--------------------------------------------
    pw = {}
    pw[word1] = {}
    pw[word2] = {}
    
    # Sense 1
    for w in uniquewc[word1]:
        pw[word1][w] = (uniquewc[word1][w]+1)/(n1+num_vocab)
        # If this word is exclusive to sense 1, still account for it in terms of sense 2
        if w not in pw[word2]:
            pw[word2][w] = (1)/(n2+num_vocab) # add zero in num
        
    # Sense 2
    for w in uniquewc[word2]:
        pw[word2][w] = (uniquewc[word2][w]+1)/(n2+num_vocab)
        if w not in pw[word1]:
            pw[word1][w] = (1)/(n1+num_vocab)
    
    
    #--------------------------------------------
    # Calculate the probabilities of instances of the pseudoword being one word sense or the other
    # Accuracy = correct/totw
    #--------------------------------------------
    totw = 0 # total test windows
    correct = 0 # test windows where prediction was correct
    predicted = {} # predicted word senses for each context window
    
    for window in testw:
        # Reset probability variables for next test window, with P(word(i))
        p1 = (num_doc1/tot_docs)
        p2 = (num_doc2/tot_docs)
        for word in window:
            # If there is a probability for a word from the test set, then multiply the final prob variable by word's prob
            if word in pw[word1]:
                p1 *= pw[word1][word]
                p2 *= pw[word2][word]
            else:
                p1 *= 1
                p2 *= 1
        
        # Get most likely word sense one test window at a time
        maxp=max(p1, p2)
        predicted_sense = ''
        if maxp == p1:
            predicted_sense = word1
        else:
            predicted_sense = word2
        if actual[' '.join(window)] == predicted_sense:
            correct += 1
        
        # Store actual and predicted senses for user to check
        result = "actual: {}, predicted: {}".format(actual[' '.join(window)], predicted_sense)
        predicted[' '.join(window)] = result
        totw += 1
    
    #--------------------------------------------
    # Print accuracy and write out results to file
    #--------------------------------------------
    print('Accuracy ({}): {}%'.format(pseudoword, int(100*(correct/totw))))
    
    with open("results-{}.json".format(pseudoword), 'w') as file:
        file.write(json.dumps(predicted, indent=4))


#================================================
# Call method and take in words as arguments
#================================================
wsd(sys.argv[1], sys.argv[2])
