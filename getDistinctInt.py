def getDistinctInt(integer):
    listA = list(integer)
    listA.reverse()
    temp = []
    for i in listA:
        if i not in temp:
            temp.append(i)
    output = ''
    for j in range(len(temp)):
        output += temp[j]
    return output

integer = input()
print(getDistinctInt(integer))