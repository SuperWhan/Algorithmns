1. build the graph based on the input file, in other words, I build a dictionary(which will seem as adjacency list) call graph.

2.dfs: depth first search, help to check the all need for one course, and will based on the graph. like for dfs(graph, 4041), it will come out with all course that need fulfill.for the top (4041) to the last (1133)

3. using dfs function to checking all the course, then will generate a list with all courses and their prerequests. using LILO(last in last out) to merge the reverse of those course and their prerequests, and drop the overlaped courses. (forexample: if you are merge [4041,1933,2021,1133], with [1933,1133,1001], first reverse thiese two lists: [1133,2021,1933,4041] and [1001,1133,1933], then LILO: [1001,1133,1933,2021,4041].)

4. Goal:
You may assume there are no circular prerequisites (i.e. class A requires class B. Class B requires class
C. Class C requires class A). You may assume all classes that are prerequisites of another are listed.
The courses can be any string (not necessarily numbers)
Sample input file (course identifier before “:”. Prerequisites after “:” with spaces between):
1001:
1133:
2011:
1933:1133
4041:1933 2011
Sample output.txt (valid class ordering with spaces between (no space after final class)):
1133 2011 1933 4041 1001 
