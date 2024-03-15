#!/bin/bash

if [[ $# -ne 3 ]]; then
    echo "usage: new.sh <cs1030-assignments> <problemname> <basename>"
    exit 2
fi

# doc
mkdir -p $1/$2/doc
touch $1/$2/doc/doc.md

# starter
mkdir $1/$2/_starter
touch $1/$2/_starter/$3.py

# solution
touch $1/$2/$3.py

# setup problem test script from template
mkdir $1/$2/tests
#touch $1/$2/$3/tests/test_$4.py
#topics=$(echo "$2" | cut -c14-)
classname=$(sed -r 's/(^|_)([a-z])/\U\2/g' <<< $3)
sed -e "s/\${filename}/$3.py/" -e "s/\${classname}/$classname/" test.py.template > $1/$2/tests/test_$3.py
