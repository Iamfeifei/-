def passwordAuth(string):
    temp = []
    if len(string) <= 8:
        return 'NG'
    condition1, condition2, condition3, condition4 = 0, 0, 0, 0
    for i in string:
        if ord('a') <= ord(i) <= ord('z'):
            condition1 = 1
        elif ord('A') <= ord(i) <= ord('Z'):
            condition2 = 1
        elif ord('0') <= ord(i) <= ord('9'):
            condition3 = 1
        else:
            condition4 = 1
    if condition1 + condition2 + condition3 + condition4 < 3:
        return 'NG'
    subSeq = []
    # 切出长度为3的子串
    for i in range(len(string)):
        subSeq.append(string[i:i + 3])
    # set()把重复的删去，如果有重复的会变短，有重复子串就会输出NG
    if len(set(subSeq)) < len(subSeq):
        return 'NG'

    return 'OK'


print(passwordAuth(input()))
