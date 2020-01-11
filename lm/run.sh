#!/bin/bash

set -u
set -e

echo "Storing unigram and bigram frequencies."
echo "Calculating bigram probabilities..."
python3 get_normal.py
echo "Done."
echo ""

echo "Input sentence (only lower-case letters w/o punctuation):"
read var1
python3 log_prob.py "$var1"
echo ""

echo "Input bigram in order to calculate the next most likely 8 words."
read var2
python3 svg.py "$var2"
echo ""

echo "Done."
