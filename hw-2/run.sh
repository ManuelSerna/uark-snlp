#!/bin/bash

set -u
set -e

python preprocess.py night seat
python preprocess.py kitchen cough
python preprocess.py car bike

echo "Done."
