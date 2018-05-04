new things strat with comment problem5.
1. renew_final: this function will passing new vertex one by one, then using dijkstra with new vertex and all vertex that already find the shortest path. using dijkstra will change the d_value of all vertex, so we compare the new path and old path, if new path was shorter, then just reweight the path, and renew the final graph.(int(final[i][j]) > node_lis[i].d_val + node_lis[j].d_val) did this work.
and also renew the pre_graph, and pre_final, till all new vertexes are all added.

2. if find the negative number in the added vertex, or run johnson at very first return negative cycle, then just simply return negative cycle.

3. this runs runtime(johnson(initial_graph)) + runtime((# new vertex)*runtime(dijkstra))

4. Goal:
Assume you ran your Johnson's Algorithmns code on an undirected graph to find all pairs shortest path, but
afterwards new vertexes are added to the graph and you want to compute the new all pairs shortest
paths. In other words, find an efficient way to find all pairs shortest paths when new vertexes and
edges are added for an undirected graph. Here “efficient” means that the runtime should be smaller
than rerunning your problem 4 on the new graph from scratch. Your runtime should be approximately
runtime(# old vertexes) + runtime(# added vertexes) = runtime(# total vertexes), where “old vertexes”
and “total vertexes” could be computed directly from problem 4's algorithm.
The first thing in the input file will be the adjacency matrix (same setup as problem 4, except you can
assume it will correspond to an undirected graph). After this will the list of new vertexes in the format
of their corresponding rows in the adjacency matrix (see below for an example).
Your output.txt should contain two all pairs shortest paths: one using only the original matrix (same as
the output would be for problem 4) and one with all the vertexes. (Again, you should not re-run
problem 4 from scratch to get the all pairs shortest paths with all vertexes.) If there are no extra
vertexes, just simply output the same as problem 4 with a single matrix. For each “all pairs shortest
paths”, if a negative cycle is present simply output (without quotes): “Negative cycle”. If this happens
in both the original and new graph, this output should appear twice.
Sample input file #1 (contains adjacency matrix with no “new vertexes”):
0 2 1
2 0 4
1 4 0
Sample output.txt (no trailing spaces after last number):
0 2 1
2 0 3
1 3 0
Sample input file #2 (contains adjacency matrix, with two “new” vertexes):
0 2 1
2 0 4
1 4 0
2000000 4 6 0 1
2 1 3 1 0
Sample output.txt (two matrices, one 3x3 and one 5x5):
0 2 1
2 0 3
1 3 0
0 2 1 3 2
2 0 3 2 1
1 3 0 4 3
3 2 4 0 1
2 1 3 1 0
Sample input file #3 (contains adjacency matrix):
0 2 1
2 0 4
1 4 0
2000000 4 6 0 1
­2 1 3 1 0
Sample output.txt:
0 2 1
2 0 3
1 3 0
Negative cycle
Sample input file #4 (contains adjacency matrix):
0 2 1
2 0 ­4
1 ­4 0
2000000 4 6 0 1
­2 1 3 1 0
Sample output.txt:
Negative cycle
Negative cycle
Sample input file #5 (contains adjacency matrix):
0 2 1
2 0 ­4
1 ­4 0
Sample output.txt (just this line and no other words):
Negative cycle
