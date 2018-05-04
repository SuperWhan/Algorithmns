import sys
inFile = open(sys.argv[1], "r")
array = inFile.read().split(' ')
inFile.close()


new_array = array[:-1] + [array[len(array)-1].replace('\n','')]

def bucket_sort(lis,i):
    buckets = [[] for x in range(26)]
    for j in range(26):
        for value in lis:
            if value[i] == chr(65+j) or value[i] == chr(97+j):
                buckets[j] = buckets[j] + [value]
    new_lis = []
    for j in range(len(buckets)):
        if len(buckets[j]) > 10:
            new_lis = buckets[:-len(buckets)+j] + bucket_sort(buckets[j], i+1) + buckets[j+1:]
        elif buckets[j] != []:
            new_lis = new_lis + insertion_sort(buckets[j])
    return new_lis


def insertion_sort(lis):
    for i in range (1, len(lis)):
        key = lis[i]
        j = i - 1
        while j>=0 and key < lis[j]:
            lis[j+1] = lis[j]
            j -= 1
        lis[j+1] = key
    return lis

final_lis = bucket_sort(new_array,0)
outfile = open("output.txt","w")
for i in final_lis[:-1]:
    outfile.write(i + ' ')
outfile.write(final_lis[-1].rstrip())
outfile.close
