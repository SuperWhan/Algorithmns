import sys
inFile = open(sys.argv[1], "r")
array = inFile.read()
inFile.close()

array = array.split('\n')
pattern1 = array[0]
txt = array[1]
pattern2 = pattern1[::-1]

def next_status(patn, state, chara):
    leng = len(patn)
    count=0
    if state<leng and chara == patn[state]:
        return state + 1
    for nexts in range(state,0,-1):
        if patn[nexts-1] == chara:
            while count < nexts-1:
                if patn[count] != patn[state-nexts+1+count]:
                    break
                count = count + 1
            if count == nexts - 1:
                return nexts
    return 0

def table_help (patn):
    leng = len(patn)
    table = [[0 for i in range (26)] for j in range (leng+1)]
    for state in range(leng+1):
        for x in range(26):
            table[state][x] = next_status(patn, state, chr(x+97))
    return table

def search(patn1, patn2, t):
    table1 = table_help(patn1)
    table2 = table_help(patn2)
    state1 = 0
    state2 = 0
    result = ''
    for x in range (len(t)):
        state1 = table1[state1][ord(t[x])-97]
        state2 = table2[state2][ord(t[x])-97]
        if state1 == len(patn1):
            result = result + str(x - len(patn1) + 1)
        if state2 == len(patn2):
            result = result + str(x - len(patn1) + 1)
    return result

final_result = search (pattern1,pattern2,txt)


outfile = open ("output.txt","w")
for i in final_result[:-1]:
    outfile.write(i + ' ')
outfile.write(final_result[-1].rstrip())
outfile.close()
