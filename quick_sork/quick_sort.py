import sys
inFile = open(sys.argv[1], "r")
array = inFile.read().split(' ')
inFile.close()

temp_lis = array[0].split('\n')
lis = [temp_lis[1]] + array[1:-1] + [array[len(array)-1][:-1]]
ith = temp_lis[0]

def quick_sort(lis, above, below, equal):
    if(len(lis)==1 or len(lis)==0):
        return lis
    pivot = lis[0]
    for value in lis:
        if int(value) > int(pivot):
            above = above + [value]
        elif int(value) < int(pivot):
            below = below + [value]
        else:
            equal = equal + [value]
    new_lis = quick_sort(below,[],[],[]) + equal + quick_sort(above,[],[],[])
    return new_lis

sorted_lis = quick_sort(lis,[],[],[])
num_is = sorted_lis[int(ith)-1]

outfile = open("output.txt","w")
outfile.write(num_is)
outfile.close()
