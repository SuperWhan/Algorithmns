1. most part like Dijkstra, extract_min, Relax and neigh_find are already defined in problem3, so Im not gonna explain again. There're some little fix on the dijkstra, since we did not return anything in problem3, but we do need for problem4, so I just return all vertex with the d_val that changed from this vertex. for example. if using the 
0 2000000 4
2 0 7
2000000 3 0
as our example, the dijkstra(graph,0) will return [0,7,4], 7 and 4 are the d_val for vertex_1 and vertex_2

2. Bellman, using for finding the negative cycle, since we can't checkout the negative cycle by using dijkstra. It did most same thing as dijkstra, just since when we relax all vertex but still have the situtation that vertex + weight is smaller than neigh.d_val, then we could know that there's a negative cycle.

3.johnson: start with adding a 'super' node. from super node to all node weight is 0, and it self as the start point, run dijsktra and bellman, to get all d_val for all vertex and bell_man will check the negative cycle., reweight the graph, by using formula, and get a new graph, which i call super_graph. Then dijkstra will generate a list this list will all add into new_lis, so there will have all d_val from all vertex, by using reweight graph(super_graph). Finally, using d_val of all vertex, new_lis and the formular: thi(u,v) - h(u) + h(v)(reweighted's weight - d_val of from vertex - d_val of to vertex)

4. Goal:
Implement Johnson's algorithm to find all pairs shortest paths. The input text file will contain the graph
represented as an adjacency matrix. Values of 2 millino will represent “infinity” edge weights (i.. when
there is no edge between vertexes). You can assume all pairs of shortest paths will be less than 2
million.
Your output.txt should contain a matrix of all pairs shortest paths (just the distances). If there is a
negative cycle present, output.txt should contain just the words (without quotes): “Negative cycle”.
The matrix for shortest paths should have spaces between the numbers and a single row on one line
(similar to the input file). The vertex order must also be the same as the input text file, so the first row
in the input text file must correspond to the shortest paths from the first vertex in output.txt.
Sample input file #1 (contains adjacency matrix):
0 2000000 4
2 0 7
2000000 3 0
Sample output.txt (no trailing spaces after last number):
0 7 4
2 0 6
5 3 0
Sample input file #2 (contains adjacency matrix):
0 2000000 ­4
­1 0 7
2000000 ­2 0
Sample output.txt (just this line and no other words):
Negative cycle
