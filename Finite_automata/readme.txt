1. according to the input file get three valuable: patter1(for forward checking), pattern2(for backward checking) and txt(string need go through)

2.next_status: will go through the each signle character in the pattern and txt, and generate the state, if they are matching, the state will plus one and then checking for previous stage until all pattern in the txt are checked. In a word this function is checking for the pattern and txt, see if the process could move to next stage or need to jump back.

3.table_help: build state table by using the next_status. So we can according to table to "draw" the graph, also could check the pattern with txt based on the table.

4.search: need 2 patterns, since we need to check both forward and backward for one pattern. So first, I build two tables using table_help, table1 and table 2. check pattern1 with txt using table1, check pattern2 with txt using table2, that's means when the state on the table is same as two patterns'length, the result will add that length position of txt. (For example: if you are checking 10th character, and the state meet the len(pattern), means you have a find now. result will get 10-len(pattern), since you need the position where you find first character match.)

5. Goal:
Make a string match program using a finite automata. However, you need to modify it so it finds the
patter either forwards or backwards. The first word in the input file is the pattern (on its own line).
The second word will be the string you are trying to match. Output all indexes where a match starts
happening.
You may assume we will only put the normal 26 English letters in lower case for both the pattern and
string. It is possible for a match to happen twice (if the pattern is symmetric). You should output the
index of this match twice then. Assume indexes start from 0.
Sample input file (all characters on a single line with no spaces between):
abcc
abccbabcc
Corresponding sample output.txt file (spaces separating indexes (no space after final index)):
0 2 5
