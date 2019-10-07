#!/bin/bash

set -u
set -e

echo "Word disambiguation test results." >> test_results.txt
echo "" >> test_results.txt

# First set--easy
python wsd.py night seat >> test_results.txt
python wsd.py kitchen cough >> test_results.txt
python wsd.py car bike >> test_results.txt

# Second set--harder
python wsd.py manufacturer bike  >> test_results.txt
python wsd.py big small >> test_results.txt
python wsd.py huge heavy >> test_results.txt

echo "Done."
