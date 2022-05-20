while True:
    try:
        l = input().split()
        head = l[1]
        rm = l[-1]
        l = l[2:-1]#把要插入的链表切出来
        res = [head]
        for i in range(0, len(l), 2):

            # i = i*2
            # if i>len(l):
            #     break
            a = l[i]
            b = l[i+1]
            res.insert(res.index(b)+1, a)

        res.remove(rm)
        print(' '.join(res)+" ")
    except:
        break