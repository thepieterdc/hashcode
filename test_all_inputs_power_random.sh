#!/bin/sh

cat c.pre | python3 power_randomizator.py > c_powerrandom_out.txt
echo "c done"
cat d.pre | python3 power_randomizator.py > d_powerrandom_out.txt
echo "d done"
cat b.pre | python3 power_randomizator.py > b_powerrandom_out.txt
echo "b done"
cat e.pre | python3 power_randomizator.py > e_powerrandom_out.txt
echo "e done"