#!/bin/bash
# Cleaning output of all the .ipynb in the current directory.

for j in `ls -al *.ipynb|awk '{print $9}'|grep -E '^[0-9]+-'`
do
	echo -e "\x1b[1;33m${j}\x1b[m"
	jupyter nbconvert --clear-output --inplace "${j}"
	echo ""
done
