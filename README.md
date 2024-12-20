# calender-python
 python

# Michaels solution to the problem day 3

## Global variables 
- tree_hit_count - counter for how many times we've hit trees on the weigh down

## Main Loop

read each line
move 3 chars to the right
  - check current char for `#`
    - if yes then increment tree_hit_count
how to jump to next row?
return tree_hit_count or repeat 

if x + 3 > char then x+3 - char - 1
y_max = input.split new line.length

--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.