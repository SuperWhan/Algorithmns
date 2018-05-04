1. get start and end valubale and graph based on the txt file provided.

2. make a calss call node, which will have 3 valubale, vertex, d_val and pi. vertex is the name of node, d_val is the d.value of vertex, amd pi is the path to the neighber. 2000000 seem as infinity, d.value will initial as 2000000, but start.dvalue will initial as 0.

3. Relax: relax function will change the d.value if the from node dvalue plus weight between the from node and to node is greater than the to node dvalue, then change the dval of to node. and also set the to node pi to from node.

4. find neigh: find all neighbors from 1 vertex

5. extract_min: extract the vertex with minimum d_value from a node list.

6. Dijkstra: will find all path from the source node to all vertex, and change all vertexes' d value and pi. according to the d value we can know the distance between the start node end node, and according to the pi value we can know the path.

7. Goal:
Implement Dijkstra's algorithm to find the shortest path to every other vertex. The input text file will
contain the graph represented as an adjacency matrix. Values of 2 million will represent “infinity” edge
weight (when there is no edge between the verticies). You can assume all shortest paths will be less
than 2 million.
The first line in the input file is the source vertex, one space, then the destination vertex (with the first
row of the adjacency matrix being vertex “0”, the second row being vertex “1”, and so on). Afterwards
is the adjacency matrix (which will be square). Your output.txt should contain the shortest path length
from this source to destination vertex followed by a “:”. After the “:” should be the actual list of
vertexes you should travel through for this shortest path.
Sample input file (fire line always source and destination vertex, afterwards is adjacency matrix):
0 1
0 2000000 4
2 0 7
2000000 3 0
Sample output.txt (7 is the shortest path length (before “:”). 0 2 1 is the actual path (after “:”)):
7: 0 2 1
