#!/bin/bash

set -u
set -e

echo "Generating bigrams."
python count_bigrams.py

echo "Generated data file."
echo "Now generating collocations using chi-squared method."
python get_collocations.py

echo "Done."
