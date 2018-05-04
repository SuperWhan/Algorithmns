import Queue
import sys
inFile = open(sys.argv[1], "r")
array = inFile.read()
inFile.close()

class Node:
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right
    def children(self):
        return((self.left, self.right))


def array_help(lis):
    new_lis = []
    while lis[0] != '\n':
        new_lis = new_lis + [(lis.count(lis[0]),lis[0])]
        lis = lis.replace(lis[0],'')
    return new_lis

huff_lis = array_help(array)

def huff_tree (lis):
    temp = Queue.PriorityQueue()
    for value in lis:
        temp.put(value)
    while temp.qsize()>1:
        right, left = temp.get(),temp.get()
        node = Node(left, right)
        temp.put((left[0]+right[0] , node))
    return temp.get()

huff_tree = huff_tree(huff_lis)
def code_with_character(temp_node,code,new_lis) :
    if (temp_node.right in huff_lis) and type(temp_node.left[1]) == type (temp_node):
        new_lis = new_lis + [(temp_node.right[1] , code + '0')]
        return code_with_character(temp_node.left[1] , code + '1', new_lis)

    elif (temp_node.left in huff_lis) and type(temp_node.right[1]) == type (temp_node):
        new_lis = new_lis + [(temp_node.left[1],code + '1')]
        return code_with_character(temp_node.right[1],code + '0',new_lis)

    elif type(temp_node.left[1]) == type (temp_node) and type(temp_node.right[1]) == type (temp_node):
        new_lis = new_lis + code_with_character(temp_node.left[1] , code + '1', []) + code_with_character(temp_node.right[1],code + '0',[])
        return new_lis

    elif (temp_node.right in huff_lis) and (temp_node.left in huff_lis):
        new_lis = new_lis + [(temp_node.right[1], code+'0')] + [(temp_node.left[1],code + '1')]
        return new_lis

b_list = Queue.PriorityQueue()
final_list = []
for value in code_with_character(huff_tree[1],'',[]):
    b_list.put(value)
while b_list.qsize()>0:
    final_list = final_list + [b_list.get()]
print_list = []
for i in final_list:
    print_list = print_list + [i[0] + ':' + i[1]]

outfile = open("output.txt","w")
for i in print_list[:-1]:
    outfile.write (i + '\n')
outfile.write(print_list[-1].rstrip())
outfile.close()
