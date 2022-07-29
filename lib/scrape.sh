#!/bin/bash
python ao3_get_fanfics.py $*
python extras/csv_to_txts.py fanfics.csv
