#!/bin/sh

cat c.pre | python3 randomizator.py > c_random_out.txt
echo "c done"
cat d.pre | python3 randomizator.py > d_random_out.txt
echo "d done"
cat b.pre | python3 randomizator.py > b_random_out.txt
echo "b done"
cat e.pre | python3 randomizator.py > e_random_out.txt
echo "e done"