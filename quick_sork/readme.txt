so I used quick sort to handle this problem

in quick sort function, I set 4 arguments, the input list, above, below and equal

set first element to pivot

find big numbers goes above

find small numbers goes below

equal numbers stay at middle

recursively call the function to sort the above and below part, and add them together.

get the ith elements.

That's it, we done!

Goal:
Use selection (i.e. average runtime of O(n)) to find the ith smallest number. The first number in the
text file (on its own line) will be “i”. The second line will the the array of number which you want to
find the ith smallest. You may assume the array contains only integers.
Sample output.txt (single number only):
4
Sample input.txt (first line will be the integer “i”, second line will be array with spaces between
elements (no space after last)):
7
4 5 8 2 4 7 5 0 8 2 3 9 23 48 ­12 49

for running code, just use:

./run.sh input.txt
