while True:
    try:
        string = input()
        lst=[]
        if string.isdigit():
            binary = '{:032b}'.format(int(string))
            i=0
            while i <32:
                lst.append(eval('0b'+binary[i:i+8]))
                i+=8
            for item in lst:
                if item == lst[-1]:
                    print(item,end='')
                else:
                    print(item,end='.')
        else:
            lst = list(string.split('.'))
            res = '0b'
            for item in lst:
                binarytmp = '{:08b}'.format(int(item))
                res =  res + binarytmp
            print(eval(res))
    except:
        break