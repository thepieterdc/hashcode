#!/bin/sh

cat c.pre | python3 script.py > c_out.txt
echo "c done"
cat d.pre | python3 script.py > d_out.txt
echo "d done"
cat e.pre | python3 script.py > e_out.txt
echo "e done"
cat b.pre | python3 script.py > b_out.txt
echo "b done"
