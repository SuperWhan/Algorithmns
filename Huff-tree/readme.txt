So, for this problem, I used class to modifiy the tree.

first make a class node, which just contains left and right child.

array_help function is counting the numbers of each characters and put them in to a tuple, just like (45,'a'), so 45 is the number of times 'a' appears.

huff_tree is building a tree, that add from smallest to the largest, and using huffman code algorithms

code_with_character is generating the code and bind the code with the characters, it recursively walk through the tree, and get a list of chracters and its' huffman code. like ('a','0')

the rest aprat is just to make the list easier to print and print them out.

for running code, just use:

./run.sh input.txt
