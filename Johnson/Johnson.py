import sys
inFile = open(sys.argv[1], "r")
array = inFile.read()
inFile.close()

pre_array = array.split('\n')[:-1]

graph = []
for i in range(0,len(pre_array)):
    graph = graph + [pre_array[i].split(' ')]

class Node:
    def __init__(self, vertex, d_val, pi=None):
        self.vertex = vertex
        self.d_val = d_val
        self.pi = pi

node_lis = []
for i in range(len(graph)):
    node_lis.append(Node(i,2000000))
# num_vertex = len(node_lis)

def Relax(neigh, vertex, weight):
    if vertex.d_val + weight < neigh.d_val:
        neigh.d_val = vertex.d_val + weight
        neigh.pi = vertex.vertex

def neigh_find(vertex, graph):
    neight = []
    for i in range(len(graph)):
        if vertex == i:
            i+=1
            continue
        if int(graph[vertex][i]) < 2000000:
            neight = neight + [i]
    return neight

def extract_min(n_lis):
    pre_lis = []
    for i in n_lis:
        pre_lis = pre_lis + [(i, node_lis[i].d_val)]
    mini = min(pre_lis, key=lambda x: x[1])[0]
    n_lis.remove(mini)
    return mini

def dijkstra(graph, source):
    for i in node_lis:
        i.d_val = 2000000
    node_lis[int(source)].d_val = 0
    S = []
    Q = range(len(graph))
    new_lis = []
    while Q != []:
        u = extract_min(Q)
        S = S + [u]
        for v in neigh_find(u, graph):
            Relax(node_lis[v],node_lis[u],int(graph[u][v]))
    for i in range(len(graph)):
        new_lis = new_lis + [str(node_lis[i].d_val)]
    return new_lis

def bell_man(graph, source):
    node_lis[int(source)].d_val = 0
    k = len(graph)
    for i in range(k-1):
        for x in range(k):
            for y in range(k):
                Relax(node_lis[y], node_lis[x], int(graph[x][y]))
    for x in range(k):
        for y in range(k):
            if node_lis[y].d_val > node_lis[x].d_val + int(graph[x][y]):
                return False
    return True

def johnson(graph):
    num_vertex = len(node_lis)
    super_graph=[[]for i in range(num_vertex)]
    node_preser = []
    new_lis = []
    for i in range(num_vertex):
        super_graph[i] = graph[i] + ['2000000']
    super_graph = super_graph+[['0' for i in range(num_vertex+1)]]
    node_lis.append(Node('super',0))
    num_vertex2 = len(super_graph)
    if bell_man(super_graph,num_vertex) == False:
        return 'Negative cycle'
    for i in node_lis:
        node_preser = node_preser + [i.d_val]
    for u in range(num_vertex2):
        for v in range(num_vertex2):
            if u == v or int(super_graph[u][v]) > 19999:
                continue
            else:
                super_graph[u][v] = str(int(super_graph[u][v]) + node_lis[u].d_val - node_lis[v].d_val)
    for x in range(num_vertex):
        new_lis = new_lis + [dijkstra(super_graph, x)[:-1]]
    for i in range(num_vertex):
        for j in range(num_vertex):
            new_lis[i][j] = str(int(new_lis[i][j]) - node_preser[i] + node_preser[j])
    return new_lis

final = johnson(graph)

if final == "Negative cycle":
    outfile = open ("output.txt","w")
    for i in final:
        outfile.write(i)
    outfile.close()
else:
    outfile = open ("output.txt","w")
    for i in final:
        if i != final[0]:
            outfile.write('\n')
        for j in i:
            outfile.write(j+' ')
    outfile.close()
