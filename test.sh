#!/bin/sh

echo "TRENDING\n"
cat trending_today.in | python3 solution.py > trending.out
echo "VIDEOS WORTH SPREADING\n"
cat videos_worth_spreading.in | python3 solution.py > spreading.out
echo "ME AT ZOO\n"
cat me_at_the_zoo.in | python3 solution.py > zoo.out
echo "KITTENS\n"
cat kittens.in | python3 solution.py > kittens.out
