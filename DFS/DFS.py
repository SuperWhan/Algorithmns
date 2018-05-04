import sys
inFile = open(sys.argv[1], "r")
array = inFile.read()
inFile.close()

temp_lis = array.split('\n')
temp = []
result = set([])

for i in range (len(temp_lis)):
    temp = temp + [temp_lis[i].split(':')]

temp = temp[:-1]
graph = {}
for i in temp:
    if i[1] == '':
        graph.update({i[0]:set([])})
    else:
        graph.update({i[0]:set(i[1].split(' '))})

def dfs(graph, vertex):
    result = [vertex]
    pre_r = graph[vertex]
    if pre_r == set():
        return result
    else:
        for pre in list(pre_r):
            result = result + dfs(graph, pre)
    return result

pre_list = []
for i in temp:
    pre_list = ((dfs(graph, i[0]))[::-1]) +pre_list

final_list=[]
for i in pre_list:
    if i not in final_list:
        final_list.append(i)

outfile = open ("output.txt","w")
for i in final_list:
    outfile.write(i + ' ')
outfile.close()
