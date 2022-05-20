def countChar (string):
    count = 0
    s1, s2 = string.split()
    for i in s1:
        if i == s2:
            count +=1
    return count
temp = input()
print(countChar(temp))