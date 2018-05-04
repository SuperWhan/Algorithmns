import sys
inFile = open(sys.argv[1], "r")
array = inFile.read()
inFile.close()

def string_helper (stri):
    new_lis = []
    str_1 = stri[0]
    for i in range (1,len(stri)):
        str_1 =  str_1 + stri[i]
        if stri[i] == '\n':
            new_lis = new_lis + [str_1]
            str_1 = ''
    return new_lis
# make string easier to compare

better_array = string_helper(array)

def check_helper (stri):
    str_l = ''
    for i in range (len(stri)):
        if stri[i] == ' ':
            str_l = stri[i+3:]
            str_l = str_l[:-1]
	    return str_l
# changed "paul : 2\n" to "2", used for compare two elements' key

def max_find (a, b, c):
    if int(a) >= int(b) and int(a) >= int(c):
        return a
    elif int(b) >=int(a)  and int(b) >= int(c):
        return b
    else:
        return c
# this is for the finding the max Element

def Max_heapfy (stri_lis,i):
    if i == 0:
        return stri_lis
    if len(stri_lis) % 2 == 1:
        right = check_helper(stri_lis[i])
        left = check_helper(stri_lis [i-1])
        parent = check_helper(stri_lis [(i/2)-1])
        large = max_find(left, right, parent)
        if large == left:
            stri_lis[i-1], stri_lis[(i/2)-1] = stri_lis[(i/2)-1], stri_lis[i-1]
            return Max_heapfy(stri_lis,i-2)
        elif large == right:
            stri_lis[i], stri_lis[(i/2)-1] = stri_lis[(i/2)-1] ,stri_lis[i]
            return Max_heapfy(stri_lis,i-2)
        else:
            return Max_heapfy(stri_lis,i-2)# this is for max_heapfy the odd numbers of elements string
    if len(stri_lis) % 2 == 0:
        if i == (len(stri_lis) - 1) and int(check_helper(stri_lis[i])) >= int(check_helper(stri_lis[(i-1)/2])):
            stri_lis[(i-1)/2],stri_lis[i] = stri_lis[i],stri_lis[(i-1)/2]
            return Max_heapfy(stri_lis, i-1)
        elif i == (len(stri_lis) - 1):
            return Max_heapfy(stri_lis, i-1)
        else:
            right = check_helper(stri_lis[i])
            left = check_helper(stri_lis [i-1])
            parent = check_helper(stri_lis [i/2-1])
            large = max_find(left, right, parent)
            if large == left:
                stri_lis[i-1], stri_lis[(i/2)-1] = stri_lis[(i/2)-1], stri_lis[i-1]
                return Max_heapfy(stri_lis,i-2)
            elif large == right:
                stri_lis[i], stri_lis[(i/2)-1] = stri_lis[(i/2)-1] ,stri_lis[i]
                return Max_heapfy(stri_lis,i-2)
            else:
                return Max_heapfy(stri_lis,i-2)# this is for the even numbers of elements string


def Insert(S,x):
    S.append(str(x) + '\n') # use the format like: Insert(better_array, 'alan : 40'), better_array is my whole set of all ements included.

def Maximum(S):
    Max_heapfy(S, len(S)-1)
    return S[0]

def Extract_Max(S):
    Max_heapfy(S, len(S)-1)
    temp = S[0]
    S.pop(0)
    return(temp)

Final_array = Max_heapfy(better_array,len(better_array)-1)

outfile = open ("output.txt","w")
for i in Final_array[:-1]:
    outfile.write(Extract_Max(Final_array))
outfile.write(Final_array[-1].rstrip())
outfile.close()
