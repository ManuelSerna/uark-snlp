#!/bin/bash

set -u
set -e

# First set--easy
echo "Easy set"
python wsd.py night seat
python wsd.py kitchen cough
python wsd.py car bike
echo ""

# Second set--harder
echo "Harder set"
python wsd.py manufacturer bike
python wsd.py big small
python wsd.py huge heavy
echo ""

echo "Done."
