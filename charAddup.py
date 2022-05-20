while True:
    try:
        s1, s2 = input().split()
        s = list(s1 + s2)
        # 奇子串排序
        s[::2] = sorted(s[::2])
        # 偶子串排序
        s[1::2] = sorted(s[1::2])

        dic = {'0': '0', '1': '8', '2': '4', '3': 'C', '4': '2', '5': 'A', '6': '6', '7': 'E', '8': '1', '9': '9',
               'a': '5', 'b': 'D', 'c': '3', 'd': 'B', 'e': '7', 'f': 'F', 'A': '5', 'B': 'D', 'C': '3', 'D': 'B',
               'E': '7', 'F': 'F', }
        for i in range(len(s)):
            if s[i] in dic.keys():
                s[i] = dic[s[i]]
        print(''.join(s))
    except:
        break
