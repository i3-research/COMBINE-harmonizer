#!/bin/bash

cd REDCap

COMBINE-exec-all -f 01-to-redcap-create-dictionary.ipynb
COMBINE-exec-all -f 02-to-redcap-identifier.ipynb

# requires 4 days to finish uploading the data.
COMBINE-exec-all -f 03-to-redcap.ipynb -t 345600

cd ..
