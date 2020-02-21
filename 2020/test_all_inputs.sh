#!/bin/sh

cat inputs/e_so_many_books.txt | python3 ding.py > outputs/e.txt
echo "e done"
cat inputs/f_libraries_of_the_world.txt | python3 ding.py > outputs/f.txt
echo "f done"
