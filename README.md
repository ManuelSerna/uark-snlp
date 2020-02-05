# uark-snlp
This repository contains my programming projects for my statistical natural language processing (SNLP) course (CSCE 5543) at the University of Arkansas in the of fall of 2019.

## Collocations
This programming assignment processes a text file full of reviews to extract collocations. First, the `count_bigrams.py` program will remove any words that include: digits, special characters, stop words imported from a txt file, as well as a minimum count requirement to increase accuracy. Next, the program in `get_collocations.py` calculates the chi-square values for each token and the top 100 values should indicate the top 100 collocations.

## Word Sense Disambiguation
This programming assignment "disambiguates" word senses for a pseudoword (two words with varying similarity concatenated together). The accuracies for each pair of words that were disambiguated are displayed in the file `test_results.txt`.

## LM
This programming assignment builds a language model in order to generate Shakespearean-sounding text. This project takes in works from Shakespeare and stores bigram and unigram counts (which are normalized in order to make more accurate calculations). Then the project calculates the log prbability of a given sentence. Finally, the program in `svg.py` takes in a bigram from the user and generates the next 8 most likely words with the Shannon Visualization Game.
