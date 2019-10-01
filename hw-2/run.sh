#!/bin/bash

set -u
set -e

python wsd.py night seat
python wsd.py kitchen cough
python wsd.py car bike

echo "Done."
