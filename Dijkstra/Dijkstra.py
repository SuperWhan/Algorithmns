import sys
inFile = open(sys.argv[1], "r")
array = inFile.read()
inFile.close()

pre_array = array.split('\n')[:-1]
start = int((pre_array[0].split(' '))[0])
end = int((pre_array[0].split(' '))[1])

num_vertex = len(pre_array[1].split(' '))

graph = []
for i in range(1,len(pre_array)):
    graph = graph + [pre_array[i].split(' ')]

class Node:
    def __init__(self, vertex, d_val, pi=None):
        self.vertex = vertex
        self.d_val = d_val
        self.pi = pi

node_lis = []
for i in range(num_vertex):
    node_lis.append(Node(i,2000000))


def Relax(neigh, vertex, weight):
    if vertex.d_val + weight < neigh.d_val:
        neigh.d_val = vertex.d_val + weight
        neigh.pi = vertex.vertex

def neigh_find(vertex):
    neight = []
    for i in range(num_vertex):
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
    node_lis[int(source)].d_val = 0
    S = []
    Q = range(num_vertex)
    while Q != []:
        u = extract_min(Q)
        S = S + [u]
        for v in neigh_find(u):
            Relax(node_lis[v],node_lis[u],int(graph[u][v]))

dijkstra(graph, start)

output = ''
i = end
while node_lis[i].pi != start:
    output = output + str(node_lis[i].pi) +' '
    i = node_lis[i].pi

output = str(node_lis[end].d_val)+': '+ str(node_lis[start].vertex) + output[::-1] +' ' +str(node_lis[end].vertex)

outfile = open ("output.txt","w")
for i in output:
    outfile.write(i)
outfile.close()
