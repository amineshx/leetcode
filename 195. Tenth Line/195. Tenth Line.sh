#!/bin/bash

#sol 1

sed -n '10p' file.txt


#sol 2

awk 'NR==10' file.txt

#sol 3
nl file.txt | grep -P '^ *10\s' | cut -f2-
