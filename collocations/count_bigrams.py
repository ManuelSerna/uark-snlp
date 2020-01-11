#************************************************
'''
    Natural Language Processing Homework #1
    Part 1: Generate bigrams--preprocessing
    Manuel Serna-Aguilera
    
This program will preprocess the text file we want to generate the top 100 collocations for. To increase the accuracy of the collocations list, we remove any words that include digits or special characters, stop words (according to an imported list), as well as a minimum count requirement to account for "one-off" bigrams.
'''
#************************************************
import collections
import json
import string

'''
Extract stop words and put in a list.
'''
stop_words = [line.rstrip('\n') for line in open("stop_words.txt")]

'''----------------------------------------------
Check if word i and i+1 are valid words using the is_valid method.
Consider:
    i.  stop words
    ii. strings do not have only letters (we should not see digits or special chars)

With this, we won't add a bad word or its count.
Then, add valid word's count to dict, insert if it's new.

Input: var "input_string" will be a single word.
----------------------------------------------'''
def is_valid(input_string):
    # Check for digits
    if any(char.isdigit() for char in input_string):
        return False
    
    # Check for stop words with a loop
    for stop_word in stop_words:
        if stop_word == input_string:
            return False
    
    # Return true if all checks fail
    return True



'''
Read text input file and create list where each word is an element.
'''
file_name = 'amazon_reviews.txt'
#file_name = 'test.txt'
text = open(file_name, 'r')
text_str = text.read()
text_str = text_str.replace('&quot', '').translate(str.maketrans('', '', string.punctuation)).lower()
words = text_str.split() # list of all words from text

'''
Get:
    i.   bigrams and their counts (dictionary)
    ii.  individual words and their counts (dictionary)
    iii. total number of words (number)
'''
bigram_freq = {}
word_counts = {}

for i in range(len(words)-1):    
    # Check if word i is valid 
    if is_valid(words[i]):
        # Add to count regardless if it will form a good bigram with word i+1
        try:
            word_counts[words[i]] += 1
        except KeyError:
            word_counts[words[i]] = 1
        # Now that word i is valid, check if bigram (i, i+1) is also valid. If so, add to bigram dict, or insert if new.
        if is_valid(words[i+1]):
            key = words[i] + ' ' + words[i+1]
            try:
                bigram_freq[key] += 1
            except KeyError:
                bigram_freq[key] = 1

# Finally, produce total counts by what has been counted in filtered tokens dict.
tot_words = 0
for t in word_counts:
    tot_words += word_counts[t]

'''
Sort dictionaries by count.
'''
# bigrams
bigram_freq = sorted(bigram_freq.items(), key=lambda kv: kv[1], reverse=True)
bigram_freq = collections.OrderedDict(bigram_freq)
# words
word_counts = sorted(word_counts.items(), key=lambda kv: kv[1], reverse=True)
word_counts = collections.OrderedDict(word_counts)

'''
Nest dictionaries.
'''
data = {
    "bigrams" : bigram_freq,
    "tokens" : word_counts,
    "total" : tot_words
}

'''
Combine all three dictionaries into a json object.
'''
with open("data.json", 'w') as file:
    file.write(json.dumps(data, indent=4))
