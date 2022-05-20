def fun(string):
    string_list=list(string)
    temp=[]
    for i in string_list:
        if i not in temp:
            temp.append(i)
    print(len(temp))
fun(input())